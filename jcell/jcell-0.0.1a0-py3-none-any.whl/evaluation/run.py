import os
import json
import argparse
import sys
import requests

import warnings
import numpy as np
import torch

from .src.test import test
from .src import loadimage, imageProvider, saveimage
from .src import Decoder, list_gpus

from .src import save_defaults_argparse, load_defaults_argparse


def list_models():
    resource_file = os.path.expanduser(os.path.join("~", ".jcell", "jcellrc"))
    resource_line = ""
    if os.path.exists(resource_file):
        f = open(resource_file, "r")
        resource_line = f.read()
        f.close()
    else:
        print(
            "Pre-trained models not found. Please, do jcell-update for downloading the latest version."
        )

    if resource_line != "":
        path_jcell = os.path.expanduser(os.path.join(resource_line, "models"))
        current_models_path = os.path.join(path_jcell, "models.json")
        current_models = (
            json.load(open(current_models_path))
            if os.path.exists(current_models_path)
            else {}
        )

        if "version" in current_models:
            current_models.pop("version")
        current_models = list(current_models.keys())
    else:
        current_models = []

    return current_models


def list_images(path_list):
    images = []
    if path_list:
        for image in path_list:
            if os.path.isdir(image):
                provider = imageProvider(image)
                images += [
                    os.path.join(image, files) for files in provider._files
                ]
            else:
                if not os.path.exists(image):
                    raise ValueError("Invalid path or file {}".format(image))
                try:
                    loadimage(image)
                    images += [image]
                except Exception:
                    try:
                        file = open(image, "r")
                        images += file.readlines()
                    except Exception:
                        raise ValueError(
                            "The argument --input must be a path to an image, a text file, or a folder with several images in it."
                        )
        images = [x.rstrip() for x in images]  # valid path only
    return images


def jcell_eval(
    input,
    model="",
    post="MAP",
    post_param={},
    use_gpu=[-1],
    confidence=0.0,
    is_3D=False,
    crop_size=0,
    adaptive_area_filter=False,
):
    args_dict = locals().copy()
    args_dict["3D"] = args_dict.pop("is_3D")
    args_dict["overwrite"] = True
    args_dict["AAF"] = args_dict.pop("adaptive_area_filter")
    args_dict["output"] = os.path.expanduser(
        os.path.join("~", ".jcell", "output", "")
    )
    args_dict["output_type"] = ["instances", "probability"]
    assert isinstance(post, str) and post in [
        "MAP",
        "WTS",
        "TH",
    ], "Post-processing must be one of the following [MAP, TH, WTS]"
    if not isinstance(input, str):
        assert isinstance(
            input, np.ndarray
        ), "Input must be either a string or np.array"
        temporal_path = os.path.expanduser(
            os.path.join("~", ".jcell", "image.tif")
        )
        saveimage(input, temporal_path)
        args_dict["input"] = temporal_path

    if model == "":
        args_dict["probability"] = args_dict.pop("input")

    if isinstance(model, torch.Tensor):
        temporal_path = os.path.expanduser(
            os.path.join("~", ".jcell", "model.pth")
        )
        model_dict = {
            "arch": type(model).__name__,
            "net": model.state_dict(),
            "normalization": "percentile_norm",
        }
        torch.save(model_dict, temporal_path)

    def args2list(args):
        cmd_args = []
        for key, value in args.items():
            if key == "args_dict":
                continue
            elif isinstance(value, str) and value == "":
                continue
            elif isinstance(value, bool):
                if value:
                    cmd_args += ["--{}".format(key)]
            elif isinstance(value, dict):
                cmd_args += [
                    "--{}={}".format(key, str(value).replace(" ", ""))
                ]
            elif isinstance(value, list):
                cmd_args += ["--{}".format(key)]
                for val in value:
                    cmd_args += ["{}".format(val)]
            else:
                cmd_args += ["--{}={}".format(key, value)]
        return cmd_args

    custom_folder = os.getcwd()
    args, _ = os.path.split(__file__)
    os.chdir(args)
    sys.path[0] = args
    args = os.path.join(args, "run.py")

    sys.argv = [args] + args2list(args_dict)
    parser = argparse.ArgumentParser(description="Parameters", add_help=False)
    parser.add_argument(
        "-h",
        "--help",
        action="store_true",
        help="Show this help message.",
    )
    main(parser, custom_folder)
    os.chdir(custom_folder)
    sys.path[0] = custom_folder

    list_images = [
        os.path.join(args_dict["output"], f)
        for f in os.listdir(args_dict["output"])
    ]
    results = []
    for images in list_images:
        image = loadimage(images)
        results += [image]
    return results


def main(custom_parser=None, current_folder=None):
    if custom_parser is None:
        parser = argparse.ArgumentParser(description="Parameters")
    else:
        parser = custom_parser

    parser.add_argument(
        "--input",
        action="append",
        help="Path to test images. Parameter --input accepts a path to a folder in which case will process every image inside, a path to an image, or a path to a text file containing a path to an image in every line.",
        metavar="/path/to/images",
    )
    parser.add_argument(
        "--probability",
        action="append",
        help="Path to probability map. Parameter --probability accepts a path to a folder in which case will process every probability map inside, a path to an probability map, or a path to a text file containing a path to a probability in every line.",
        metavar="/path/to/probablities_maps",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="",
        help="Path to the model or pretrained model name from {}.".format(
            list_models()
        ),
        metavar="/path/to/models",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="",
        help="Path to the output folder.",
        metavar="/path/to/output/folder/",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allows overwriting the output file if already exists. Otherwise consecutive enumeration will be used.",
    )
    parser.add_argument(
        "--post",
        action="append",
        type=str,
        choices=["MAP", "TH", "WTS"],
        help="Select a post_processing type from [MAP, TH, WTS]. MAP stands for Maximum a Posteriori, TH for Thresholding maps, and WTS for Watershed. MAP is the default if --post is not specified.",
        metavar="MAP",
    )
    parser.add_argument(
        "--post_param",
        action="append",
        help="Post-processing parameters. Follows the expected dictionary for every post-processing. MAP: {'min_area':<integer>,'morph_se':<integer>}. TH:  {'thresh_cell':<float:0-1>, 'thresh_div':<float:0-1>, 'morph_se':<integer>}. WTS: {'thresh_background':<float:0-1>,'thresh_foreground':<float:0-1>}",
        metavar="POSTPARAM",
    )

    parser.add_argument(
        "--use_gpu",
        nargs="?",
        type=int,
        const="1",
        action="append",
        help="Use --use_gpu=1 if want to segment in the first GPU. If not included then segmentation is executed using the CPU. If --use_gpu=0 the all GPUs are used. An specific list of GPUs can be used, i.e. --use_gpu 1 2 3 4.",
        metavar="1",
    )
    parser.add_argument(
        "--output_type",
        nargs="+",
        choices=[
            "image",
            "object_overlay",
            "bound_overlay",
            "boundary",
            "instances",
            "classification",
            "segmentation",
            "instances_rgb",
            "probability",
            "all",
        ],
        help="Select one or more output type from [image, object_overlay, bound_overlay, boundary, instances, classification, segmentation, instances_rgb, probability, all].",
        metavar="all",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=0,
        help="Detection confidence threshold.",
        metavar="0",
    )

    parser.add_argument(
        "--3D",
        action="store_true",
        help="If --3D flag is used then 3D segmentation is performed.",
        dest="is_3D",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="If included shows current version",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--crop_size",
        type=int,
        default=0,
        help=argparse.SUPPRESS,
    )

    parser.add_argument(
        "--AAF",
        action="store_true",
        help="If included then the Adaptive Area Filtering is applied",
        dest="sequence",
    )

    save_defaults_argparse(parser)
    parser = load_defaults_argparse(parser)
    args, not_know_args = parser.parse_known_args()

    if (
        args.help
        or len(not_know_args) > 1
        or (len(not_know_args) == 1 and not os.path.exists(not_know_args[0]))
    ):
        parser.print_help()
        return 0

    if current_folder is None and os.path.exists(not_know_args[0]):
        current_folder = not_know_args[0]

    if not args.verbose:
        warnings.filterwarnings("ignore")
        sys.tracebacklimit = 0

    if args.version:
        print("JCell Instance Segmentation")
        print("California Institute of Technology")
        print("Universidade Federal de Pernambuco")
        print("Version 0.0.1a0")
        sys.exit()

    if args.probability is not None and args.model != "":
        raise ValueError(
            "Please provide either --probability or --model. Both parameters are not allowed at the same time"
        )

    if args.probability is not None:
        args.evaluation = "probability"
    else:
        args.evaluation = "network"

    # open images
    images = list_images(args.input)

    # open probability maps
    pimages = list_images(args.probability)

    if len(images) == 0:
        if len(pimages) == 0:
            raise ValueError("Please provide a valid image path")
        images = pimages

    if args.use_gpu is None:
        args.use_gpu = [-1]

    if not isinstance(args.use_gpu, list):
        args.use_gpu = [args.use_gpu]

    if args.post is None:
        args.post = ["MAP"]

    if args.post_param is None:
        args.post_param = ["{}"]

    if args.output_type is None:
        args.output_type = ["all"]

    args.post = [otype + "_post" for otype in args.post]

    for i in range(len(args.post_param)):
        args.post_param[i] = json.loads(
            args.post_param[i].replace("'", '"'), cls=Decoder
        )

    assert len(args.post) == len(
        args.post_param
    ), "For every --post a --post_param must be provided"

    min_gpu = -1 if len(args.use_gpu) == 1 else 1
    max_gpu = len(list_gpus())
    if any(np.array(args.use_gpu) < min_gpu) or any(
        np.array(args.use_gpu) > max_gpu
    ):
        raise ValueError(
            "Invalid value for --use_gpu. Please, use indexes between 1 and {}. Set --use_gpu=0 for using all GPUs or --use_gpu=-1 if CPU only is desired.".format(
                max_gpu
            )
            if max_gpu > 0
            else "Nvidia GPU not found in this device. Please, set --use_gpu=0 for CPU only"
        )
    args.use_gpu = [gpu - 1 for gpu in args.use_gpu]
    if args.use_gpu[0] == -1:
        args.use_gpu = [gpu for gpu in range(len(list_gpus()))]
    elif args.use_gpu[0] == -2:
        args.use_gpu = [-1]

    args.use_gpu = sorted(args.use_gpu)

    if check_version("models") == 0:
        check_version("datasets")

    test(
        images=images,
        model=args.model,
        original_output=args.output,
        imcropsize=args.crop_size,
        post_list=args.post,
        kwargs_list=args.post_param,
        use_gpu=args.use_gpu,
        output_type=args.output_type,
        prob_image=pimages,
        rotation=True,
        filter_inst=args.confidence,
        is_3D=args.is_3D,
        evaluation=args.evaluation,
        overwrite=args.overwrite,
        default_folder=current_folder,
        verbose=args.verbose,
        sequence=args.sequence,
    )


def check_version(db):
    resource_file = os.path.expanduser(os.path.join("~", ".jcell", "jcellrc"))
    if os.path.exists(resource_file):
        f = open(resource_file, "r")
        resource_line = f.read()
        f.close()

        try:
            updated_models = requests.get(
                "http://jcell.org/{}/{}.json".format(db, db)
            ).json()
            current_models_path = os.path.join(
                resource_line, db, "{}.json".format(db)
            )
            if os.path.exists(current_models_path):
                current_models = json.load(open(current_models_path))
                if (
                    "version" in current_models
                    and current_models["version"] < updated_models["version"]
                ):
                    print(
                        "Some new {} are available in the server. Please, do a jcell-update for updating.".format(
                            db
                        )
                    )
                elif "version" not in current_models:
                    print(
                        "Some new {} are available in the server. Please, do a jcell-update for updating.".format(
                            db
                        )
                    )
                else:
                    return 0
            else:
                print(
                    "Please, do a jcell-update for downloading the {}.".format(
                        db
                    )
                )
        except Exception:
            pass

    else:
        print(
            "Please, do a jcell-update for downloading jcell resources from the server."
        )
    return 1


if __name__ == "__main__":
    main()
