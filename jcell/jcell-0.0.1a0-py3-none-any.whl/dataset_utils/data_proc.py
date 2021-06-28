import os
import sys
import warnings

import argparse
import numpy as np
from tqdm import tqdm

from functools import wraps
import json
import inspect

try:
    from .imageutl import imageProvider, loadimage
except Exception:
    from imageutl import imageProvider, loadimage

warnings.filterwarnings("ignore")


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
            int(os.path.splitext(files[len(image_name) :].split("_")[-1])[0])
            if len(files[len(image_name) :].split("_")) > 1
            and (
                os.path.splitext(files[len(image_name) :].split("_")[-1])[0]
            ).isdecimal()
            else 0
            for files in os.listdir(outpath)
            if ("{}_".format(image_name) in files)
            or ("{}.".format(image_name) in files)
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


def parse_output_augment(output, naming="image", overwrite=False, regexpr=""):
    """
    Parse output path. Naming convention.
    """

    outpath, image_name = os.path.split(output)
    original_outpath = outpath
    outpath = os.path.join(outpath, "images")
    if image_name == "":
        image_name = naming

    create_folders(outpath)
    if not overwrite:
        consecutive_naming = [
            int(os.path.splitext(files[len(image_name) :].split("_")[-2])[0])
            if len(files[len(image_name) :].split("_")) > 1
            and (
                os.path.splitext(files[len(image_name) :].split("_")[-2])[0]
            ).isdecimal()
            else 0
            for files in os.listdir(outpath)
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

    output = os.path.join(original_outpath, image_name)
    return output


def list_images(path_list):
    images = []
    for image in path_list:
        if os.path.isdir(image):
            provider = imageProvider(image)
            images += [os.path.join(image, files) for files in provider._files]
        else:
            try:
                loadimage(image)
                images += [image]
            except Exception:
                try:
                    file = open(image, "r")
                    images += file.readlines()
                except Exception:
                    raise ValueError(
                        "The argument --image must be a path to an image, a text file, or a folder with several images in it."
                    )
    images = [x.rstrip() for x in images]  # valid path only
    return images


def create_folders(folder):
    if not os.path.isdir(folder):
        path, fold = os.path.split(folder)
        if not os.path.isdir(path):
            create_folders(path)
        os.mkdir(folder)


def main():
    parser = argparse.ArgumentParser(
        prog="jcell-dataproc",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
    )
    subparsers = parser.add_subparsers(dest="stage")

    inst2sem_parser = subparsers.add_parser(
        "inst2sem",
        help="Instance to semantic label transformation. Use it along with -h for more options.",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
    )
    inst2sem_parser.add_argument(
        "--input",
        action="append",
        help="Path to instances labels images. Parameter --input accepts a path to a folder in which case will process every image inside, a path to an image, or a path to a text file containing a path to an image in every line.",
        metavar="/path/to/images",
    )
    inst2sem_parser.add_argument(
        "--output",
        type=str,
        default="",
        help="Path to the output folder",
        metavar="/path/to/output/folder/",
    )
    inst2sem_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allows overwriting the output file if already exists. Otherwise consecutive enumeration will be used.",
    )
    inst2sem_parser.add_argument(
        "--se1",
        type=int,
        default=0,
        help="Disk structural element radius for touching class dilation. If --se1=0 no dilation is apply (default: 0).",
        metavar="<integer>",
    )
    inst2sem_parser.add_argument(
        "--se2",
        type=int,
        default=7,
        help="Disk structural element radius for gap class (default: 7)",
        metavar="<integer>",
    )

    augment_parser = subparsers.add_parser(
        "augment",
        help="Offline data agumentation. Use it along with -h for more options.",
        formatter_class=lambda prog: argparse.HelpFormatter(
            prog, max_help_position=100, width=120
        ),
    )
    augment_parser.add_argument(
        "--image",
        action="append",
        help="Path to images. Parameter --image should be a path to a folder in which case will process every image inside.",
        metavar="/path/to/image",
    )
    augment_parser.add_argument(
        "--label",
        action="append",
        help="Path to semantic labels. Parameter --label should be a path to a folder in which case will process every image inside.",
        metavar="/path/to/label",
    )
    augment_parser.add_argument(
        "--output",
        type=str,
        default="",
        help="Path to the output folder",
        metavar="/path/to/output/folder/",
    )
    augment_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allows overwriting the output file if already exists. Otherwise consecutive enumeration will be used.",
    )
    augment_parser.add_argument(
        "--crop_size_x",
        type=int,
        default=0,
        help="Size of random crop in x direction (default: 0)",
        metavar="<integer>",
    )
    augment_parser.add_argument(
        "--crop_size_y",
        type=int,
        default=0,
        help="Size of random crop in y direction (default: 0)",
        metavar="<integer>",
    )
    augment_parser.add_argument(
        "--crop_size_z",
        type=int,
        default=0,
        help="Size of random crop in z direction (default: 0)",
        metavar="<integer>",
    )
    augment_parser.add_argument(
        "--gamma",
        action="store_true",
        help="If --gamma is included, then random gamma correction transformations is applied",
    )
    augment_parser.add_argument(
        "--ignore_empty",
        action="store_true",
        help="if --ignore_empty flag used then empty blocks will be ignored for random crop",
    )

    save_defaults_argparse(augment_parser, "augment")
    augment_parser = load_defaults_argparse(augment_parser, "augment")
    save_defaults_argparse(inst2sem_parser, "inst2sem")
    inst2sem_parser = load_defaults_argparse(inst2sem_parser, "inst2sem")
    parseargs, not_know_args = parser.parse_known_args()
    if len(not_know_args) > 1 or (
        len(not_know_args) == 1 and not os.path.exists(not_know_args[0])
    ):
        parser.print_help()
        exit(0)

    args, _ = os.path.split(sys.argv[0])

    if parseargs.stage == "inst2sem":
        if sys.argv[2] != "-h" and sys.argv[2] != "--help":
            try:
                from .proc2d.inst2sem import inst2sem as inst2sem2d
                from .proc3d.inst2sem import inst2sem as inst2sem3d
            except Exception:
                from proc2d.inst2sem import inst2sem as inst2sem2d
                from proc3d.inst2sem import inst2sem as inst2sem3d

            path_images = list_images(parseargs.input)

            pbar = tqdm(
                total=len(path_images), desc="Instances to Semantic - "
            )
            for image_name in path_images:
                input_path, name = os.path.split(image_name)
                name, ext = os.path.splitext(name)
                if not os.path.isabs(input_path) and len(not_know_args) == 1:
                    input_path = os.path.join(not_know_args[0], input_path)
                elif not os.path.isabs(input_path):
                    input_path = os.path.join(os.getcwd(), input_path)

                output, naming = os.path.split(parseargs.output)
                naming = os.path.splitext(naming)[0]
                output = (
                    os.path.join(input_path, "semantic")
                    if not output or output == input_path
                    else output
                )
                output = (
                    output
                    if os.path.isabs(output)
                    else os.path.join(input_path, output)
                )
                regexpr = ""
                if naming.find("_%") != -1:
                    regexpr = naming.split("_%")[-1]
                    regexpr = regexpr if regexpr.isdecimal() else ""

                    if regexpr == "":
                        warnings.warn("Invalid regular expression")
                    else:
                        naming = naming[: -(len(regexpr) + 2)]

                if len(path_images) > 1:
                    if naming != "":
                        warnings.warn(
                            "Prefix is not allowed for multiple inputs. Saving results in folder {} instead.".format(
                                naming
                            )
                        )

                    output = os.path.join(output, naming)
                    naming = ""

                output = parse_output(
                    os.path.join(output, naming),
                    name,
                    parseargs.overwrite,
                    regexpr,
                )
                output += ext

                pbar.set_description("Instances to Semantic - {}".format(name))
                volume = np.array(loadimage(image_name))
                if (volume.ndim > 3) or (
                    volume.ndim == 3 and list(volume.shape)[2] > 3
                ):
                    inst2sem3d(volume, parseargs.se1, parseargs.se2, output)
                else:
                    inst2sem2d(
                        volume,
                        parseargs.se1,
                        parseargs.se2,
                        output,
                    )
                pbar.update()
            pbar.close()

    elif parseargs.stage == "augment":
        if sys.argv[2] != "-h" and sys.argv[2] != "--help":
            try:
                from .proc2d.augmentation import augmentation as augmentation2d
                from .proc3d.augmentation import augmentation as augmentation3d
            except Exception:
                from proc2d.augmentation import augmentation as augmentation2d
                from proc3d.augmentation import augmentation as augmentation3d

            path_images = list_images(parseargs.image)
            path_labels = list_images(parseargs.label)

            assert len(path_images) == len(
                path_labels
            ), "The number of images does not match the number of labels"

            pbar = tqdm(total=len(path_images), desc="Data Augmentation - ")
            for image_name, label_name in zip(path_images, path_labels):
                iname, iext = os.path.splitext(os.path.split(image_name)[1])
                lname, lest = os.path.splitext(os.path.split(label_name)[1])
                pbar.set_description(
                    "Data Augmentation - {}/{}".format(iname, lname)
                )

                volume = np.array(loadimage(image_name))
                label = np.array(loadimage(label_name))

                input_path = os.path.split(image_name)[0]

                output, naming = os.path.split(parseargs.output)
                output = input_path if not output else output
                output = (
                    output
                    if os.path.isabs(output)
                    else os.path.join(input_path, output)
                )
                name = iname  # "data_aug" if iname != lname else iname
                regexpr = ""
                if naming.find("_%") != -1:
                    regexpr = naming.split("_%")[-1]
                    regexpr = regexpr if regexpr.isdecimal() else ""

                    if regexpr == "":
                        warnings.warn("Invalid regular expression")
                    else:
                        naming = naming[: -(len(regexpr) + 2)]

                if len(path_images) > 1:
                    if naming != "":
                        warnings.warn(
                            "Prefix is not allowed for multiple inputs. Saving results in folder {} instead.".format(
                                naming
                            )
                        )

                    output = os.path.join(output, naming)
                    naming = ""

                output = parse_output_augment(
                    os.path.join(output, naming),
                    name,
                    parseargs.overwrite,
                    regexpr,
                )
                output += iext

                if (volume.ndim > 3) or (
                    volume.ndim == 3 and list(volume.shape)[2] > 3
                ):
                    augmentation3d(
                        volume,
                        label,
                        output,
                        parseargs.crop_size_x,
                        parseargs.crop_size_y,
                        parseargs.crop_size_z,
                        parseargs.gamma,
                        parseargs.ignore_empty,
                        regexpr,
                    )
                else:
                    augmentation2d(
                        volume,
                        label,
                        output,
                        parseargs.crop_size_x,
                        parseargs.crop_size_y,
                        parseargs.gamma,
                        parseargs.ignore_empty,
                        regexpr,
                    )
                pbar.update()
            pbar.close()
    else:
        parser.print_help()


def load_defaults(f):
    attrs = inspect.signature(f)
    attrs = attrs.parameters

    @wraps(f)
    def change_defaults(*args, **kwargs):
        attr_dict = dict()

        # first initialize with default values in the function
        for attr, val in attrs.items():
            if val.default != inspect._empty:
                attr_dict[attr] = val.default

        module = f.__module__
        cls_name = args[0].__class__.__name__ if "self" in attrs else ""
        f_name = f.__name__
        defaults = get_defaults_dict(module, cls_name, f_name)

        # defaults in json file
        for attr, val in defaults.items():
            if attr == "self":
                continue
            attr_dict[attr] = val

        # then begin handling positional arguments
        positional_attrs = list(attrs.keys())
        for attr, val in zip(positional_attrs, args):
            attr_dict[attr] = val

        # last, add keyword arguments
        if kwargs:
            for attr, val in kwargs.items():
                attr_dict[attr] = val

        return f(**attr_dict)

    return change_defaults


def get_defaults_dict(module, cls_name, f_name):
    defaults_folder = os.path.expanduser(os.path.join("~", ".jcell"))
    if not os.path.exists(defaults_folder):
        create_folders(defaults_folder)

    defaults_path = os.path.join(
        defaults_folder, "default_data_processing.json"
    )
    if not os.path.exists(defaults_path):
        json.dump(
            dict(),
            open(defaults_path, "w"),
        )

    defaults = json.load(open(defaults_path))

    name = cls_name + ":" + f_name
    if module not in defaults.keys():
        defaults[module] = dict()

    if name not in defaults[module]:
        defaults[module][name] = dict()

    return defaults[module][name]


def save_defaults(f):
    attrs = inspect.signature(f)
    attrs = attrs.parameters

    @wraps(f)
    def change_defaults(*args, **kwargs):
        attr_dict = dict()

        # first initialize with default values in the function
        for attr, val in attrs.items():
            if val.default != inspect._empty:
                attr_dict[attr] = val.default

        module = f.__module__
        cls_name = ""
        if args:
            cls_name = args[0].__class__.__name__ if "self" in attrs else ""

        f_name = f.__name__
        set_defaults_dict(module, cls_name, f_name, attr_dict)

        return f(*args, **kwargs)

    return change_defaults


def set_defaults_dict(module, cls_name, f_name, attr_dict):
    defaults_folder = os.path.expanduser(os.path.join("~", ".jcell"))
    if not os.path.exists(defaults_folder):
        create_folders(defaults_folder)

    defaults_path = os.path.join(
        defaults_folder, "default_data_processing.json"
    )
    if not os.path.exists(defaults_path):
        json.dump(
            dict(),
            open(defaults_path, "w"),
        )

    defaults = json.load(open(defaults_path))

    name = cls_name + ":" + f_name
    if module not in defaults.keys():
        defaults[module] = dict()

    if name not in defaults[module]:
        defaults[module][name] = attr_dict
        json.dump(
            defaults,
            open(defaults_path, "w"),
        )


def save_defaults_argparse(parser, name):

    defaults, _ = parser.parse_known_args([])
    defaults = vars(defaults)
    defs = dict()
    for k, v in defaults.items():
        if not isinstance(v, bool):
            defs[k] = v

    module = "cmd_line"
    cls_name = name
    f_name = "arguments"
    set_defaults_dict(module, cls_name, f_name, defs)


def load_defaults_argparse(parser, name):

    defaults, _ = parser.parse_known_args([])
    defaults = vars(defaults)

    module = "cmd_line"
    cls_name = name
    f_name = "arguments"
    custom_defaults = get_defaults_dict(module, cls_name, f_name)

    for k, v in custom_defaults.items():
        defaults[k] = v

    parser.set_defaults(**defaults)

    return parser


if __name__ == "__main__":
    main()
