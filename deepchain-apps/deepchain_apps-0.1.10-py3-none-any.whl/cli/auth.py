"""Module that allow the authentification by register the personnal token"""

import getpass
from argparse import ArgumentParser

import yaml
from deepchain.cli import BaseCLICommand

from .apps_utils import _create_config_file, _create_deechpain_folder


def auth_command_factory(args):
    return AuthCommand()


class AuthCommand(BaseCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        login_parser = parser.add_parser(name="login", help="login to deepchain")  # type: ignore
        login_parser.set_defaults(func=auth_command_factory)

    def run(self):
        """
        Login function that create a subdirectory and store the token
        We first create .deepchain folder, then config file if not exist
        The open the file in r+ mode to not erase previous info
        """
        root_path = _create_deechpain_folder()
        path = _create_config_file(root_path)

        with open(path, "r+") as config_file:
            data = yaml.load(config_file, Loader=yaml.SafeLoader)
            data = {} if data is None else data

        data["pat"] = getpass.getpass("PAT:")
        data["size_limit"] = 40

        with open(path, "w") as app_file:
            yaml.dump(data, app_file, Dumper=yaml.SafeDumper)
