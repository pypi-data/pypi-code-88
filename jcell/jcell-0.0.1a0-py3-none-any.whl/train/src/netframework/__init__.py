from functools import wraps
from .utils.utils import create_folders
import os
import json
import inspect


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

    defaults_path = os.path.join(defaults_folder, "default_training.json")
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

    defaults_path = os.path.join(defaults_folder, "default_training.json")
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


def save_defaults_argparse(parser):

    defaults, _ = parser.parse_known_args([])
    defaults = vars(defaults)
    defs = dict()
    for k, v in defaults.items():
        if not isinstance(v, bool):
            defs[k] = v

    module = "cmd_line"
    cls_name = ""
    f_name = "arguments"
    set_defaults_dict(module, cls_name, f_name, defs)


def load_defaults_argparse(parser):

    defaults, _ = parser.parse_known_args([])
    defaults = vars(defaults)

    module = "cmd_line"
    cls_name = ""
    f_name = "arguments"
    custom_defaults = get_defaults_dict(module, cls_name, f_name)

    for k, v in custom_defaults.items():
        defaults[k] = v

    parser.set_defaults(**defaults)

    return parser
