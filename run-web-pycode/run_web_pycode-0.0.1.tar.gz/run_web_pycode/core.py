#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/6/21 14:33
# Copyright 2021 LinkSense Technology CO,. Ltd
import configparser
import os
from typing import Union

import requests

config_file_name = ".run_web_pycode_config"
global_config_path = os.path.join(os.path.expanduser("~"), config_file_name)
local_config_path = os.path.join(os.path.dirname(__file__), config_file_name)


def set_proxy(key: str, value: Union[str, None] = None, local: bool = False) -> bool:
    """
    Set request proxy

    Example:
         $ pyw set_proxy https http://127.0.0.1:9999

    Args:
        key: http or https
        value: the proxy value like http://127.0.0.1:9999
        local: set local config . default False. save in ~/..run_web_pycode_config

    Returns:
        True for Success.
    """
    if key not in ["http", "https"]:
        raise KeyError("key must be http or https")
    # get file
    config = configparser.ConfigParser()
    config_path = local_config_path if local else global_config_path
    config.read(config_path)
    if "proxies" not in config:
        config.add_section("proxies")
    # set key value
    if value:
        config["proxies"][key] = value
    else:
        config["proxies"].pop(key, None)
    # save
    with open(config_path, "w", encoding="utf8") as configfile:
        config.write(configfile)
    return True


def read_proxy(no_proxy: bool = False) -> dict:
    """
    Read config to get proxy

    Args:
        no_proxy: return empty dict for True.

    Returns: A dict.

    """
    if no_proxy:
        return {}
    config = configparser.ConfigParser()
    if os.path.exists(global_config_path):
        print("read {}".format(global_config_path))
        config.read(global_config_path)

    if os.path.exists(local_config_path):
        print("read {}".format(local_config_path))
        config.read(local_config_path)

    return dict(config["proxies"] if config.has_section("proxies") else [])


def run_remote_script(url: str, no_proxy: bool = False, timeout: int = 3) -> None:
    """
    Run remote code

    Example:
        $ pyw run https://raw.githubusercontent.com/AngusWG/run-web-pycode/master/tests/a_script.py --timeout 2

    Args:
        url: The code url
        no_proxy: use `pyw set_proxy` to set proxy
        timeout:  request timeout seconds

    Returns:
        None
    """
    proxy_map = read_proxy(no_proxy)
    req = requests.get(url, proxies=proxy_map, timeout=timeout)
    code = req.text

    exec(code)  # noqa:S102
