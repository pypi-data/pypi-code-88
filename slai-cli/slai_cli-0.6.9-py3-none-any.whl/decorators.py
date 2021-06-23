import click
import sys

from pathlib import Path
from slai_cli import log
from slai_cli.init.local_config_helper import LocalConfigHelper
from slai_cli.profile.configure import get_credentials
from slai.modules.runtime import detect_credentials, detect_runtime
from slai.exceptions import NoCredentialsFound
from os import path


def requires_slai_credentials(callback, *outer_args, **outer_kwargs):
    def wrapper(*args, **kwargs):
        profile_name = outer_kwargs.get("profile", "default")
        runtime = detect_runtime()

        try:
            detect_credentials(runtime=runtime, profile_name=profile_name)
        except NoCredentialsFound:
            log.warn("No credentials detected.")

            try:
                has_api_key = click.confirm("Do you have an api key?")
                if has_api_key:
                    get_credentials(profile_name=profile_name, runtime=runtime)
                else:
                    log.action("Create one at slai.io, then re-run this command.")
                    click.launch("https://slai.io")
                    sys.exit(0)
                    return

            except click.exceptions.Abort:
                log.warn("Aborted.")
                return

        return callback(*args, **kwargs)

    return wrapper


def requires_slai_project(callback):
    def wrapper(*args, **kwargs):

        slai_directory_present = Path(".slai").is_dir()

        if not slai_directory_present:
            log.warn(
                "No project detected in this directory, create one with 'slai init <project_name>'."  # noqa
            )
            return
        elif slai_directory_present and not Path(".slai/config.yml").exists():
            log.warn(
                "No project detected in this directory, create one with 'slai init <project_name>'."  # noqa
            )
            return

        local_config_helper = LocalConfigHelper()
        local_config_helper.check_local_config()

        return callback(*args, **kwargs)

    return wrapper
