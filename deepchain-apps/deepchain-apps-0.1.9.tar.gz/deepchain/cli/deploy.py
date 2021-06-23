"""deploy modules helps for the deployement of application on deepchain"""
from argparse import ArgumentParser

from deepchain import log
from deepchain.cli import BaseCLICommand
from deepchain.cli.cli_utils import get_config_url
from deepchain.utils.validation import _check_app_files, _check_checkpoint_files

from .apps_utils import (
    get_app_info,
    get_app_scorenames,
    get_configuration,
    update_app_status,
)
from .cli_utils import get_app_visibility, upload_checkpoint, upload_code


def deploy_command_factory(args):
    return DeployCommand(args.app_name, args.checkpoint)


class DeployCommand(BaseCLICommand):
    def __init__(self, app_name: str, checkpoint: bool):
        self.app_name = app_name
        self.checkpoint = checkpoint

    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        deploy_parser = parser.add_parser(  # type: ignore
            name="deploy", help="deploy your app to deepchain"
        )

        deploy_parser.add_argument(
            "app_name",
            action="store",
            type=str,
            help="app name",
        )
        deploy_parser.add_argument(
            "--checkpoint",
            action="store_true",
            help="use this flag to include checkpoint during upload",
        )

        deploy_parser.set_defaults(func=deploy_command_factory)

    def run(self):
        """
        Check App to be deployed with validation function
        Upload checkpoint if needed
        """
        url = get_config_url()
        configuration = get_configuration()
        pat = configuration["pat"]

        app_name = self.app_name
        app_dir = get_app_info(app_name, kind="dir")
        status = get_app_info(app_name, kind="status")

        if status == "upload":
            msg = f"app {app_name} already uploaded, do you want to replace it? (y/n) "
            answer = input(msg)
            while answer not in ["y", "n"]:
                answer = input(msg)

            if answer == "n":
                return

        log.info("Check files before upload...")
        tags_ok = _check_app_files(app_name)
        if not tags_ok:
            msg = (
                "You didn't provide any tasks in the tags.json, " "do you want to continue ? (y/n) "
            )
            answer = input(msg)
            while answer not in ["y", "n"]:
                answer = input(msg)

            if answer == "n":
                return

        is_public_app = get_app_visibility()
        score_configuration = get_app_scorenames(app_name)
        req = upload_code(
            app_dir, app_name, pat, f"{url}/apps/", score_configuration, is_public_app
        )

        if req.status_code != 200:
            log.debug("%s" % req.content)
            log.warning("api return %s stopping operation.", req.status_code)
            log.warning("App not uploaded.")
            return

        log.info("App has been uploaded.")
        update_app_status(app_name, status="upload")

        if self.checkpoint:
            _check_checkpoint_files(app_name)
            _ = upload_checkpoint(
                app_dir, app_name, pat, f"{url}/apps/", configuration["size_limit"]
            )

        return
