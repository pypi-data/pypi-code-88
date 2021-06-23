"""Base functions to make the CLI working"""
import configparser
import importlib
import os
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Union

import pkg_resources
import yaml
from deepchain import log
from deepchain.utils.exceptions import (
    AppNotFoundError,
    AppsNotFoundError,
    ConfigNotFoundError,
    InvalidAppName,
)

APPS_PATH = Path.home().joinpath(".deep-chain").joinpath("apps")
CONFIG_PATH = Path.home().joinpath(".deep-chain").joinpath("config")


def display_apps_info(config: Dict) -> None:
    """Display apps infos

    Print a format table with three columns:
    ----------------------------------------
    APP             PATH              STATUS
    ----------------------------------------
    my_app         path/to/app      status

    Args:
        config (Dict): dictionary with directory and status for each app

    Returns:
        None
    """
    data_list = []
    data_list.append(["APP", "PATH", "STATUS"])
    for app, info in config.items():
        data_list.append([app, info["dir"], info["status"]])

    left_len = max(list(map(lambda x: len(x[0]), data_list))) + 5
    middle_len = max(list(map(lambda x: len(x[1]), data_list))) + 5
    right_len = max(list(map(lambda x: len(x[2]), data_list))) + 5

    dash = "-" * (left_len + middle_len + right_len)
    # conditionnal number of space based on string size
    space_string = "{:<%ds}{:^%ds}{:>%ds}" % (left_len, middle_len, right_len)

    for i, data in enumerate(data_list):
        if i == 0:
            print(dash)
            print(space_string.format(data[0], data[1], data[2]))
            print(dash)
        else:
            print(space_string.format(data[0], data[1], data[2]))

    return


def display_public_apps(req_content: List[Dict]) -> None:
    """Print all the public app on deepchain hubs

    Print a format table with two columns:
    --------------------------------------------------------------
    APP                      USERNAME
    --------------------------------------------------------------
    my_app                 user.name@mail.com

    Args:
        Content: Dictionnary Listing all infos about public app
    """

    data_list = []
    data_list.append(["APP", "USERNAME"])
    for app in req_content:
        app_name = app.get("appName", None)
        user_name = app.get("username", None)
        data_list.append([app_name, user_name])

    left_len = max(list(map(lambda x: len(x[0]), data_list))) + 5
    middle_len = max(list(map(lambda x: len(x[1]), data_list))) + 5

    dash = "-" * (left_len + middle_len)
    # conditionnal number of space based on string size
    space_string = "{:<%ds}{:^%ds}" % (left_len, middle_len)

    for i, data in enumerate(data_list):
        if i == 0:
            print(dash)
            print(space_string.format(data[0], data[1]))
            print(dash)
        else:
            print(space_string.format(data[0], data[1]))

    print("\n")
    print(
        "Download app command  :  " + "\033[1m" + "deepchain download username/app app" + "\033[0m"
    )
    print("\n")
    print("Apps' description at : " + "\033[1m" + "https://app.deepchain.bio/hub/apps" + "\033[0m")
    print("\n")


def display_config_info() -> None:
    """
    Display the config where the URL is deployed
    """
    config = configparser.ConfigParser()
    path_config = pkg_resources.resource_filename("deepchain", "cli/config.ini")
    config.read(path_config)
    url = config["APP"]["DEEP_CHAIN_URL"]

    msg = f"App deployed at : {url}"
    dash = "-" * len(msg)
    print(dash)
    print(msg)
    print(dash)


def reset_apps() -> None:
    """
    Remove all apps' files
    """
    apps_config = get_apps_config()

    if len(apps_config) > 0:
        for _, info in apps_config.items():
            try:
                shutil.rmtree(info["dir"])
            except FileNotFoundError:
                pass
        os.remove(str(APPS_PATH))
        APPS_PATH.touch(exist_ok=True)


def remove_app(app_name: str) -> None:
    """Remove the specified app name

    Args:
        app_name (str): app registered in .deepchain/apps

    Raises:
        AppNotFoundError: Error is app nos exists
    """

    data = get_apps_config()

    app_info = data.get(app_name, None)
    if app_info is None:
        raise AppNotFoundError(app_name)

    try:
        shutil.rmtree(app_info["dir"])
    except FileNotFoundError:
        pass

    del data[app_name]
    with open(APPS_PATH, "w") as app_file:
        yaml.dump(data, app_file, Dumper=yaml.SafeDumper)


def get_app_info(app_name: str, kind: str = "dir") -> str:
    """
    Get information of an application.
    Args:
        app_name (str): [description]
        kind (str, optional):Defaults to "dir".
                        - dir : the directory of storage
                        - status : the status of the app (local or upload)

    Raises:
        AppNotFoundError: Error is app nos exists

    Returns:
        str: directory or status
    """
    assert kind in ["dir", "status"], "Can on only select 'dir' or 'status'"

    config = get_apps_config()
    app_info = config.get(app_name, None)

    if app_info is None:
        raise AppNotFoundError(app_name)

    return app_info[kind]


def get_apps_config() -> Dict:
    """Get app config file

    Raises:
        AppsNotFoundError: Error is .deepchain/apps file not exists

    Returns:
        Dict: dictionnary of {app: {dir:_,status:_}}
    """
    if not APPS_PATH.is_file():
        raise AppsNotFoundError

    with open(APPS_PATH, "r") as apps_file:
        data = yaml.load(apps_file, Loader=yaml.SafeLoader)
        data = {} if data is None else data

    return data


def check_app_name(app_name: str):
    """Check app name validity
    App' name should not contain invalid character like '.' as the app will be load
    as a module. Putting a '.' in the name will break the importlib pipeline.
    Args:
        app_name (str): name of the app

    Raises:
        Error if app contains invalid symbol.
    """
    if app_name.__contains__("."):
        raise InvalidAppName(".")


def reformat_app_name(app_name: str) -> str:
    """Reformat app name removing the username part

    Args:
        app_name (str): app_name with format : user.name@mail.xxx/MyAppName

    Returns:
        [str]: reformat name
    """
    if app_name.__contains__("/"):
        new_name = app_name.split("/")[1]
        if new_name.__contains__("."):
            new_name_ = new_name.replace(".", "")
            log.warning("Invalid charater in app_name, reformat %s to %s" % (new_name, new_name_))
            return new_name_
        else:
            return new_name
    else:
        return app_name


def check_app_exist(app_name: str) -> Tuple[bool, Union[str, None]]:
    """Create apps file and check if app exists

    Check if an app has always been created locally on the
    computer

    Args:
        app_name (str): name of the application

    Returns:
        Tuple[bool, str]: return is the app exist and Filename
    """
    root_path = _create_deechpain_folder()
    _ = _create_apps_file(root_path)

    config = get_apps_config()
    app_info = config.get(app_name, None)

    if app_info is not None:
        return True, app_info["dir"]
    else:
        return False, None


def save_app(app_name: str, dest_path: str) -> None:
    """
    Save complete path where the app is stored
    The app can be deploy next from any folder

    Args:
        app_name (str): application name stored in .deepchain/apps
        dest_path (str): folder for registraction of the app
    """
    root_path = _create_deechpain_folder()
    path = _create_apps_file(root_path)
    data = get_apps_config()

    data[app_name] = {"dir": os.path.abspath(dest_path), "status": "local"}
    with open(path, "w") as app_file:
        yaml.dump(data, app_file, Dumper=yaml.SafeDumper)


def update_app_status(app_name: str, status: str = "upload") -> None:
    """update the status of the app

    Args:
        app_name (str): name of application
        status (str, optional): status to update (local/upload). Defaults to "upload".
    """

    path = Path.home().joinpath(".deep-chain").joinpath("apps")
    data = get_apps_config()
    app_info = data.get(app_name, None)
    if app_info is None:
        raise AppNotFoundError(app_name)

    data[app_name]["status"] = status
    with open(path, "w") as app_file:
        yaml.dump(data, app_file, Dumper=yaml.SafeDumper)

    return


def get_app_scorenames(app_name: str) -> List[str]:
    """
    Function to get the score_names of the app and regitrer it
    This function requires to load the module and get the app
    names via a @staticmethod
    """
    app_dir = get_app_info(app_name)
    app_dir = Path(app_dir)  # type: ignore

    sys.path.append(str(app_dir.parent))  # type: ignore
    mod = importlib.import_module(app_name + ".src.app")
    scores = mod.App.score_names()  # type: ignore
    # Remove last element of the path which was added manually
    sys.path.pop(-1)

    return scores


def get_configuration() -> Dict:
    """
    Get personal access token. User must use 'login' function at least once
    Get maximal file size can be uploaded.
    """
    path = Path.home().joinpath(".deep-chain").joinpath("config")
    if not path.is_file():
        raise ConfigNotFoundError

    with open(path, "r") as config_file:
        data = yaml.load(config_file, Loader=yaml.SafeLoader)
        data = {} if data is None else data

    return data


def save_configuration(key: str, val: str):
    """
    Get personal access token. User must use 'login' function at least once
    Get maximal file size can be uploaded.
    """
    path = Path.home().joinpath(".deep-chain").joinpath("config")
    if not path.is_file():
        raise ConfigNotFoundError
    with open(path, "r") as config_file:
        data = yaml.load(config_file, Loader=yaml.SafeLoader)
    with open(path, "w") as config_file:
        data[key] = val
        yaml.dump(data, config_file)


def _create_deechpain_folder() -> Path:
    """create .deepchain folder if not exist"""
    path = Path.home().joinpath(".deep-chain")
    path.mkdir(exist_ok=True)
    return path


def _create_config_file(root_path: Path) -> Path:
    """
    create the config file to store the personal access token
    """
    path = root_path.joinpath("config")
    path.touch(exist_ok=True)
    return path


def _create_apps_file(root_path: Path) -> Path:
    """
    create the apps file to store all the apps
    """
    path = root_path.joinpath("apps")
    path.touch(exist_ok=True)
    return path


def save_release_tag(tag_version: str):
    save_configuration("tag_version", tag_version)


def get_last_release() -> str:
    return get_configuration().get("tag_version")
