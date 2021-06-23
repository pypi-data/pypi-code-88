"""scaffold module helps for the creation of new apps"""
import os
from argparse import ArgumentParser

from deepchain import log
from deepchain.cli import BaseCLICommand

from .apps_utils import (
    check_app_exist,
    check_app_name,
    get_last_release,
    save_app,
    save_release_tag,
)
from .cli_utils import (
    download_latest_version,
    fetch_latest_version,
    unpack_base_repository,
)


def create_command_factory(args):
    return CreateCommand(args.app_name, args.dir)


class CreateCommand(BaseCLICommand):
    def __init__(self, app_name, directory):
        self.app_name = app_name
        self.dir = directory

    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        scaffold_parser = parser.add_parser(  # type: ignore
            name="create", help="create template for new app"
        )  # type : ignore
        scaffold_parser.add_argument(
            "app_name", action="store", help="this will be the app name in deep-chain"
        )
        scaffold_parser.add_argument(
            "--dir",
            action="store",
            default=os.curdir,
            help="the directory where the app will be created",
        )
        scaffold_parser.set_defaults(func=create_command_factory)

    def run(self):
        """
        Main function to:
            - download latest release
            - create tmp_directory
            - unpack folder
            - remove tmp files
        """

        app_exist, app_path = check_app_exist(self.app_name)
        if app_exist:
            log.warning(
                "App %s already exist at %s. Please choose another app_name",
                self.app_name,
                app_path,
            )
            return
        check_app_name(self.app_name)
        log.info("Download base app.")
        latest_release = fetch_latest_version()
        dest_path = os.path.join(self.dir, self.app_name)
        if get_last_release() != latest_release:
            download_latest_version(latest_release)
            save_release_tag(latest_release["tag_name"])
        unpack_base_repository(dest_path)
        save_app(self.app_name, dest_path)
        return
