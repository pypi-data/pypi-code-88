"""Implementation of several functions to validate the folder to upload"""
import importlib
import json
import os
import sys
from json.decoder import JSONDecodeError
from pathlib import Path

from deepchain import log
from deepchain.cli.apps_utils import get_app_info

# from deepchain.utils.constants import TAGS_KEY
from deepchain.utils.exceptions import AppNotFoundError, CheckpointNotFoundError


def _check_checkpoint_files(app_name: str):
    """
    Check if some files are present if the checkpoint folder
    """

    app_dir = Path(get_app_info(app_name))
    checkpoint_dir = app_dir.joinpath("checkpoint")
    if not checkpoint_dir.is_dir():
        raise FileNotFoundError(f"You must have a checkpoint folder in the {app_dir} folder")

    model_found = _check_file_extension(checkpoint_dir)
    if not model_found:
        raise CheckpointNotFoundError


def _check_file_extension(folder_path: Path) -> bool:
    """Check if file of extension list are found in folder"""
    model_found = False
    for file in folder_path.glob("*"):
        base_file = os.path.basename(file)
        _, ext_ = os.path.splitext(base_file)

        if ext_ != ".py":
            model_found = True
            break
    return model_found


def _check_app_files(app_name: str) -> bool:
    """
    Check if the name of the app has not been modified to be upload
    on the plateform

    Args:
        app_name (str): [description]

    Raises:
        AppNotFoundError: [description]
        NotADirectoryError: [description]

    Returns:
        bool: indicate if the json file is ok.
    """
    app_dir = Path(get_app_info(app_name))

    if not app_dir.is_dir():
        raise AppNotFoundError(app_name)

    if not app_dir.joinpath("src").is_dir():
        raise NotADirectoryError("The main folder you should named 'src'")

    _check_init(app_dir)
    _check_init(app_dir.joinpath("src"))
    _check_app(app_dir.joinpath("src"))
    tags_ok = _check_json(app_dir.joinpath("src"))
    _check_module(app_dir, app_name)

    return tags_ok


def _check_init(app_dir: Path) -> None:
    """Check if init file is in folder"""
    path_init = app_dir.joinpath("__init__.py")
    if not path_init.is_file():
        raise FileNotFoundError("The app folder must be a module and contains __init__.py file")


def _check_app(app_dir: Path) -> None:
    """Check if app file if in the app folder"""
    path_app = app_dir.joinpath("app.py")
    if not path_app.is_file():
        similar_file = _find_similar_file(app_dir, "app")
        message = "The app filename must be app.py"
        if similar_file is not None:
            message += f", found this similar file instead : {similar_file}"

        raise FileNotFoundError(message)


def _check_json(app_dir: Path) -> bool:
    """Check if json file for tags if in the src folder"""
    tags_ok = True
    path_json = app_dir.joinpath("tags.json")
    if not path_json.is_file():
        message = "The tags.json should be in the src folder"
        raise FileNotFoundError(message)

    try:
        with open(str(path_json), "r+") as file:
            tags = json.load(file)
    except JSONDecodeError as err:
        msg = "Invalid tags.json file, check if you use double quote \" and not single quote ' "
        raise TypeError(msg) from err

    # key = list(tags.keys())
    # key = sorted(key)

    # if not (key == sorted(TAGS_KEY)):
    #    message = f"tags.json file only accept the following keys : {'-'.join(TAGS_KEY)}"
    #    raise KeyError(message)

    for k, v in tags.items():
        if not isinstance(v, list):
            raise TypeError(
                "The value of the json file should be of type list, even empty, except for device."
            )
        if k == "tasks":
            if len(v) == 0:
                log.warning("Don't find any tasks in the tags.json file.")
                tags_ok = False
        elif k == "device":
            if v[0] not in ["gpu", "cpu"]:
                raise TypeError('The "device" tags only takes value in "gpu"/"cpu"')

    return tags_ok


def _check_module(app_dir: Path, app_name: str) -> None:
    """Check if app module contains App class"""
    # append current path to the pkg to find the app
    # as a module

    sys.path.append(str(app_dir.parent))
    mod = importlib.import_module(app_name + ".src.app")
    avail_members = dir(mod)
    sys.path.pop(-1)

    if "App" not in avail_members:
        raise ModuleNotFoundError("You must have a App class in your app.py module")


def _find_similar_file(path_folder: Path, pattern: str) -> str:
    """
    Find python files containing pattern in a specific folder
    """
    for file in path_folder.iterdir():
        filename = file.name
        if (filename.__contains__(pattern)) and (filename.endswith("py")):
            return filename

    return None
