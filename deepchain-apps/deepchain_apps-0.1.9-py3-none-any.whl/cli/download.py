"""deploy modules helps for the deployement of application on deepchain"""
import os
import shutil
from argparse import ArgumentParser

import requests
from deepchain import log
from deepchain.cli import BaseCLICommand
from deepchain.cli.apps_utils import check_app_name, save_app
from deepchain.cli.cli_utils import get_config_url


def download_command_factory(args):
    return DownloadCommmand(args.app_name, args.app_dir)


class DownloadCommmand(BaseCLICommand):
    def __init__(self, app_name: str, app_dir: str):
        self.app_name = app_name
        self.app_dir = app_dir

    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        download_parser = parser.add_parser(  # type: ignore
            name="download", help="download public app from deepchain  hub"
        )

        download_parser.add_argument(
            "app_name",
            action="store",
            type=str,
            help="app name in the format creatorEmail:appName",
        )
        download_parser.add_argument(
            "app_dir",
            action="store",
            type=str,
            help="destination folder",
        )

        download_parser.set_defaults(func=download_command_factory)

    def run(self):
        """
        Download public app
        """
        url = get_config_url()
        if os.path.exists(f"{self.app_dir}") and len(os.listdir((f"{self.app_dir}"))) > 0:
            log.critical("destination folder is not empty, exiting.")
            return

        check_app_name(self.app_dir)
        os.mkdir(f"{self.app_dir}")
        self.unpack(self.download_tar(url))
        _ = [self.unpack(f"{self.app_dir}/{f}") for f in os.listdir(self.app_dir)]
        save_app(self.app_dir, self.app_dir)

    def download_tar(self, url: str) -> str:
        """Download tar file from the public apps-hub

        Only apps with public tags are available

        Args:
            url (str): url of the API

        Returns:
            [str]: path of the download app
        """
        req = requests.get(f"{url}/public-apps/{self.app_name}")
        if req.status_code != 200:
            print(f"api returning {req.status_code}, exiting.")
            exit(1)
        with open(f"{self.app_dir}/tmp.tar", "wb") as file:
            file.write(req.content)
        return f"{self.app_dir}/tmp.tar"

    def unpack(self, file: str):
        """Unpack tar file in proper folder

        Args:
            file (str): path of the tar file
        """
        dest = self.app_dir
        if file.endswith("_checkpoints.tar"):
            dest = os.path.join(self.app_dir, "checkpoint")
        elif file.endswith("code.tar"):
            dest = os.path.join(self.app_dir, "src")
        shutil.unpack_archive(file, dest)
        os.remove(file)
