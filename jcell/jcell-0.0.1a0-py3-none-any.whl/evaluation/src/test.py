import os
import warnings

import numpy as np
import torch
from tqdm import tqdm

import torch.nn.functional as F
from skimage.color import label2rgb
from torch.autograd import Variable

import torchvision.transforms as transforms
from skimage.measure import regionprops


from . import (
    loadnet,
    loadimage,
    saveimage,
    get_architecture,
    parse_cuda,
    list_gpus,
    get_size,
    ToTensorImage,
    SplitImage,
    Normalize,
    NormalizePercentile,
    MAP_post,
    TH_post,
    WTS_post,
    create_folders,
    iou_mat,
    visualization2D,
    visualization3D,
)


def input_channels(image, model_channel, is_3D=False):
    """
    Change the number of channels from inputs
    """
    # 2D cases
    if not is_3D:
        if image.ndim == 3 and image.shape[2] > 1 and model_channel == 1:
            image = image[:, :, 0]
            warnings.warn("WARNING: Choosing first channel from image.")
            return image[:, :, np.newaxis]

        elif image.ndim == 2 and model_channel == 1:
            return image[:, :, np.newaxis]

        elif image.ndim == 2 and model_channel == 3:
            return np.repeat(image[:, :, np.newaxis], 3, 2)

        elif image.ndim == 3 and image.shape[2] == 1 and model_channel == 3:
            return np.repeat(image, 3, 2)

        elif image.ndim == 3 and image.shape[2] >= 3 and model_channel == 3:
            return image[:, :, :3]

    # 3D cases
    else:
        if image.ndim == 4 and image.shape[2] == 3 and model_channel == 1:
            image = image[:, :, 0, :]
            warnings.warn("WARNING: Choosing first channel from volume.")
            return image[:, :, np.newaxis, :]

        elif image.ndim == 3 and model_channel == 1:
            return image[:, :, np.newaxis, :]

        elif image.ndim == 3 and model_channel == 3:
            return np.repeat(image[:, :, np.newaxis, :], 3, 2)

        elif image.ndim == 4 and image.shape[2] == 1 and model_channel == 3:
            return np.repeat(image, 3, 2)

        elif image.ndim == 4 and image.shape[2] >= 3 and model_channel == 3:
            return image[:, :, :3, :]

    return image


def parse_output(output, naming="image", overwrite=False, regexpr=""):
    """
    Parse output path. Naming convention.
    """

    outpath, image_name = os.path.split(output)
    if image_name == "":
        image_name = naming

    create_folders(outpath)
    if not overwrite:
        consecutive_naming = [
            files.replace("_overlay", "") if "_overlay." in files else files
            for files in os.listdir(outpath)
            if "{}_".format(image_name) in files
        ]
        consecutive_naming = [
            files.replace("_rgb", "") if "_rgb." in files else files
            for files in consecutive_naming
            if "{}_".format(image_name) in files
        ]
        consecutive_naming = [
            int(os.path.splitext(files[len(image_name) :].split("_")[-2])[0])
            if len(files[len(image_name) :].split("_")) > 1
            and (
                os.path.splitext(files[len(image_name) :].split("_")[-2])[0]
            ).isdecimal()
            else 0
            for files in consecutive_naming
            if "{}_".format(image_name) in files
        ]
        max_naming = max(consecutive_naming) if consecutive_naming else -1
        image_name = (
            ("{}_{:0" + regexpr + "d}").format(image_name, max_naming + 1)
            if (max_naming != -1) or (max_naming == -1 and regexpr != "")
            else image_name
        )

    else:
        image_name = os.path.splitext(image_name)[0]

    output = os.path.join(outpath, image_name)
    return output


def test(
    images,
    model,
    original_output,
    imcropsize,
    post_list,
    kwargs_list,
    use_gpu,
    output_type,
    prob_image=None,
    rotation=False,
    filter_inst=0.00001,
    is_3D=False,
    evaluation="network",
    overwrite=False,
    default_folder="",
    verbose=False,
    normalize=True,
    sequence=False,
):
    t_imcropsize = imcropsize
    post_required = (
        len(
            [
                value
                for value in output_type
                if value
                in [
                    "object_overlay",
                    "bound_overlay",
                    "boundary",
                    "instances",
                    "classification",
                    "segmentation",
                    "instances_rgb",
                    "all",
                ]
            ]
        )
        > 0
    )

    if evaluation == "network":  # load model
        # load weight vector
        net_state, architecture_name, normalization_type = loadnet(model)
        normalize = normalization_type == "percentile_norm"

        if type(net_state).__name__ == "OrderedDict":
            # number of input channels
            try:
                model_channels = net_state["down1.conv.conv1.0.weight"].size(1)
            except:
                model_channels = net_state[
                    "down1.conv.conv1.0.initial_mapping.weight"
                ].size(1)

            # number of output classes
            try:
                nclasses = net_state["final.weight"].size(0)
            except:
                nclasses = net_state["final.0.weight"].size(0)
            # create architecture structure
            net, architecture_name, processing_dimensions = get_architecture(
                architecture_name, model_channels, nclasses
            )
            # load weights
            net.load_state_dict(net_state)
        else:
            raise ValueError("Uncompatible model.")

        device, use_parallel = parse_cuda(use_gpu)
        if device != torch.device("cpu"):
            torch.cuda.set_device(min(use_gpu))

        net = net.to(device)
        if use_parallel:
            net = torch.nn.DataParallel(net, device_ids=use_parallel)
        gpus = list_gpus()
        min_free_gpu = 1024
        if len(use_gpu) > 1:
            min_free_gpu = (
                min([free["total"] - free["used"] for free in gpus()])
                if len(gpus) > 0
                else None
            )
        elif len(use_gpu) == 1:
            min_free_gpu = gpus[use_gpu[0]]["total"] - gpus[use_gpu[0]]["used"]

    pbar = tqdm(
        total=len(images), desc="Segmenting - ", position=0, leave=True
    )
    for itn, image in enumerate(images):
        try:
            # Loading image and setting output path
            if verbose:
                print("Setting up output path")
            original_input = image
            input_path, input_name = os.path.split(image)
            input_name = os.path.splitext(input_name)[0]
            if not os.path.isabs(input_path) and len(default_folder) == 1:
                input_path = os.path.join(default_folder[0], input_path)
            elif not os.path.isabs(input_path):
                input_path = os.path.join(os.getcwd(), input_path)

            output, output_name = os.path.split(original_output)
            output = input_path if not output else output
            output = (
                output
                if os.path.isabs(output)
                else os.path.join(input_path, output)
            )
            regexpr = ""
            if output_name.find("_%") != -1:
                regexpr = output_name.split("_%")[-1]
                regexpr = regexpr if regexpr.isdecimal() else ""

                if regexpr == "":
                    warnings.warn("Invalid regular expression")
                else:
                    output_name = output_name[: -(len(regexpr) + 2)]

            if len(images) > 1:
                if output_name != "":
                    warnings.warn(
                        "Prefix is not allowed for multiple inputs. Saving results in folder {} instead.".format(
                            output_name
                        )
                    )

                output = os.path.join(output, output_name)
                output_name = ""

            output = parse_output(
                os.path.join(output, output_name),
                input_name,
                overwrite,
                regexpr,
            )

            if verbose:
                print("Loading image")
            pbar.set_description("Segmenting - {}".format(input_name))
            image = np.array(loadimage(image))

            if is_3D and image.ndim == 4 and image.shape[3] < image.shape[2]:
                image = image.transpose((0, 1, 3, 2))
            elif is_3D and image.ndim == 3:
                index = np.argmin(image.shape)
                new_order = tuple(
                    [ind for ind in range(3) if ind != index] + [index]
                )
                image = image.transpose(new_order)

            original_image = image.copy()

            if evaluation == "network":
                # change number of channels if required
                image = input_channels(image, model_channels, is_3D)

            original_size = image.shape

            # Loading probability map
            probability_name = ""
            original_probability_name = ""
            if evaluation == "probability":  # no forward required
                if verbose:
                    print("Loading probability map")
                assert (
                    len(prob_image) > 0
                ), "Please, provide either a probability map or an image/model pair for segmenting"
                probability_name = prob_image[itn]
                original_probability_name = probability_name
                if probability_name is None:
                    raise ValueError(
                        "Please, provide either a probability map or an image/model pair for segmenting"
                    )

                probability_map = np.array(loadimage(probability_name))
                probability_name = os.path.splitext(
                    os.path.split(probability_name)[1]
                )[0]
                if probability_map.dtype == np.dtype("uint8"):
                    probability_map = probability_map.astype("float") / 255

            # If forward required
            if evaluation == "network":
                if verbose:
                    print("Setting up transformation")

                # Automatically setting the best crop size
                imcropsize = get_size(
                    architecture_name, original_size, min_free_gpu, is_3D
                )
                if t_imcropsize != 0:
                    imcropsize = [t_imcropsize for f in imcropsize]

                # Applying image transformations
                transform_test = transforms.Compose(
                    (
                        [NormalizePercentile(is_3D=is_3D)]
                        if normalize
                        else [Normalize()]
                    )
                    + [
                        SplitImage(imcropsize, is_3D=is_3D),
                        ToTensorImage(is_3D),
                    ]
                )

                if verbose:
                    print("Transforming image")
                image = transform_test(image)
                if (
                    (not is_3D and len(image.shape) < 4)
                    or is_3D
                    and len(image.shape) < 5
                ):
                    image = image[np.newaxis, ...]

                # forward block
                tdc = len(use_parallel) if use_parallel else 1
                if verbose:
                    print("Setting up parallel forward {}".format(tdc))
                with torch.no_grad():
                    if verbose:
                        print("Computing number of forwards")
                    probability_map = np.zeros(
                        (image.shape[0], nclasses) + tuple(image.shape[2:])
                    )
                    total_forwards = int(np.ceil(float(image.shape[0]) // tdc))
                    pbar2 = tqdm(
                        total=total_forwards * 4
                        if rotation
                        else total_forwards,
                        desc="Chunked image",
                        position=1,
                        leave=False,
                    )

                    rot_chunk_out = list()
                    for i in range(total_forwards):
                        if verbose:
                            print("Forward {}".format(i))
                        chunk = image[
                            i * tdc : min((i + 1) * tdc, image.shape[0]), ...
                        ]
                        chunk = Variable(chunk.to(device), requires_grad=False)
                        chunk_out = net(chunk)
                        pbar2.update()

                        # If average of rotations is required
                        if rotation:
                            rotation_dim = 5 if is_3D else 4
                            rotation_axes = [3, 4] if is_3D else [2, 3]

                            chunk_out = chunk_out[..., np.newaxis]
                            for t in range(3):
                                if verbose:
                                    print(
                                        "Forward {} rotation {}".format(i, t)
                                    )
                                chunk = torch.rot90(chunk, 1, rotation_axes)
                                rot_chunk_out = net(chunk)

                                rot_chunk_out = torch.rot90(
                                    rot_chunk_out, -(t + 1), rotation_axes
                                )

                                rot_chunk_out = rot_chunk_out[..., np.newaxis]
                                chunk_out = torch.cat(
                                    (chunk_out, rot_chunk_out), rotation_dim
                                )
                                pbar2.update()

                            chunk_out = chunk_out.mean(
                                rotation_dim, keepdim=False
                            )

                        probability_map[
                            i * tdc : min((i + 1) * tdc, image.shape[0]), ...
                        ] = (chunk_out.detach().cpu().numpy())
                    pbar2.close()

                    # Undo transformation, if applies
                    if verbose:
                        print("Merging image")
                    for i in range(len(transform_test.transforms)):
                        if hasattr(
                            transform_test.transforms[i],
                            "uncall",
                        ):
                            probability_map = transform_test.transforms[
                                i
                            ].uncall(probability_map)

                    # Softmax of probability map
                    if verbose:
                        print("Softmax")
                    probability_map = F.softmax(probability_map, dim=1)
                    probability_map = (
                        probability_map.data[0].detach().cpu().numpy()
                    )

                    probability_map = (
                        probability_map.transpose((1, 2, 0))
                        if not is_3D
                        else probability_map.transpose((2, 3, 1, 0))
                    )

                    del chunk, chunk_out, rot_chunk_out
                    if itn == len(images) - 1:
                        if verbose:
                            print("Releasing GPU memory")
                        del net, net_state
                    torch.cuda.empty_cache()

            if "new_order" in locals():
                new_order = list(np.argsort(new_order))
                original_image = original_image.transpose(tuple(new_order))
                probability_map = probability_map.transpose(
                    tuple(new_order + [3])
                )

            original_probability = probability_map.copy()

            # Post-processing, allowed more than one post-processing
            pbar2 = tqdm(
                total=len(post_list) * 5,
                desc="Applying post-processing -",
                position=1,
                leave=False,
            )
            for post, kwargs in zip(post_list, kwargs_list):
                pbar2.set_description(
                    "Applying post-processing - {}".format(post)
                )
                if len(post_list) == 1:
                    postname = ""
                else:
                    postname = "_" + post

                if post_required:
                    if verbose:
                        print("Applying post-processing")
                    post_method = eval(post + "()")
                    (
                        seg,
                        classif,
                        region,
                        new_probability_map,
                        _argmax,
                    ) = post_method(output=probability_map, **kwargs)

                    pbar2.update()

                    size = seg.shape
                    # Perform sequential analysis
                    if sequence:
                        squantile = 0.1
                        props = regionprops(seg)
                        areas = np.array([a.area for a in props])
                        median = np.mean(areas)

                        # instances that appeared for the first time
                        removed_inst = False
                        for r in range(seg.max() - 1):
                            if areas[r] < median * squantile:
                                seg[seg == (r + 1)] = 0
                                removed_inst = True

                        if removed_inst:
                            seg = np.reshape(
                                np.unique(seg, return_inverse=1)[1], size
                            )

                    # confidence filtering
                    if filter_inst > 0:
                        if verbose:
                            print("Confidence filtering")
                        regionfilt = np.zeros_like(region, dtype=np.uint8)
                        ccomp = seg
                        numcc = seg.max()
                        sum_dim = 3 if is_3D else 2

                        for i in range(1, numcc + 1):
                            acell = (
                                (ccomp == i).astype("float")
                                * np.sum(
                                    new_probability_map[..., 1:], axis=sum_dim
                                ).astype("float")
                            ).sum() / ((ccomp == i).astype("float")).sum()
                            if acell >= filter_inst:
                                regionfilt += (ccomp == i).astype("uint8") * (
                                    acell * 255
                                ).astype("uint8")

                        seg = seg * (regionfilt >= filter_inst).astype("uint8")
                        classif = classif * (regionfilt >= filter_inst).astype(
                            "uint8"
                        )
                        region = region * (regionfilt >= filter_inst).astype(
                            "uint8"
                        )
                    seg = np.reshape(np.unique(seg, return_inverse=1)[1], size)

                    pbar2.update()
                    if original_probability_name == original_input:
                        original_image = None

                    visualization_func = (
                        visualization3D if is_3D else visualization2D
                    )
                    (
                        image_overlay,
                        boundary_overlay,
                        boundary,
                        seg_rgb,
                    ) = visualization_func(
                        seg, output_type, original_image, verbose
                    )

                pbar2.update()
                if verbose:
                    print("Saving results")
                if original_image is not None and (
                    ("image" in output_type) or ("all" in output_type)
                ):
                    ext = (
                        "tif"
                        if original_image.dtype == np.dtype("uint16")
                        else "png"
                    )
                    saveimage(
                        original_image,
                        "{}{}_image.{}".format(output, postname, ext),
                    )

                if ("object_overlay" in output_type) or ("all" in output_type):
                    saveimage(
                        (image_overlay * 255).astype("uint8"),
                        "{}{}_object_overlay.png".format(output, postname),
                    )

                if ("bound_overlay" in output_type) or ("all" in output_type):
                    saveimage(
                        (boundary_overlay * 255).astype("uint8"),
                        "{}{}_bound_overlay.png".format(output, postname),
                    )

                if ("boundary" in output_type) or ("all" in output_type):
                    saveimage(
                        (boundary * 255).astype("uint8"),
                        "{}{}_boundary.png".format(output, postname),
                    )

                if ("classification" in output_type) or ("all" in output_type):
                    saveimage(
                        classif,
                        "{}{}_classification.png".format(output, postname),
                    )
                    saveimage(
                        _argmax,
                        "{}{}_MAP.png".format(output, postname),
                    )

                if ("segmentation" in output_type) or ("all" in output_type):
                    saveimage(
                        (region * 255).astype("uint8"),
                        "{}{}_segmentation.png".format(output, postname),
                    )

                if ("instances_rgb" in output_type) or ("all" in output_type):
                    saveimage(
                        (seg_rgb * 255).astype("uint8"),
                        "{}{}_instances_rgb.png".format(output, postname),
                    )

                if ("probability" in output_type) or ("all" in output_type):
                    saveimage(
                        (original_probability * 255).astype("uint8"),
                        "{}{}_probability.tif".format(output, postname),
                    )

                if ("instances" in output_type) or ("all" in output_type):
                    saveimage(
                        seg.astype("uint16"),
                        "{}{}_instances.tif".format(output, postname),
                    )
                pbar2.update()
            pbar2.close()
        except Exception as e:
            print(
                "The following error was raised while processing {}:".format(
                    original_input
                )
            )
            print(e)

        pbar.update()
    pbar.close()
