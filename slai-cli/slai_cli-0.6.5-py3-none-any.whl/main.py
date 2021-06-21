import click
import sys

from functools import update_wrapper
from packaging import version as ver

from requests.exceptions import HTTPError
from slai.clients.cli import get_cli_client
from slai_cli import log
from slai_cli.init import commands as init
from slai_cli.model import commands as model
from slai_cli.profile import commands as profile
from slai_cli.decorators import requires_slai_credentials
from slai_cli.errors import handle_error
from slai_cli import get_version, version


def with_profile(f):
    @click.pass_context
    def run(ctx, *args, **kwargs):

        if ctx.invoked_subcommand != "profile":
            _f = requires_slai_credentials(f, **kwargs)
            return ctx.invoke(_f, *args, **kwargs)

    return update_wrapper(run, f)


@click.group()
@click.option("--profile", required=False, default="default", help="Profile to use")
@with_profile
def entry_point(profile):
    cli_client = get_cli_client()
    cli_requirements = cli_client.get_cli_version()

    minimum_required_cli_version = ver.parse(
        cli_requirements["minimum_required_version"]
    )
    current_cli_version = ver.parse(get_version())
    if current_cli_version < minimum_required_cli_version:
        log.info(f"Current CLI version: {current_cli_version}")
        log.info(f"Minimum required CLI version: {minimum_required_cli_version}")
        log.warn(
            "This version of the CLI is out of date, please update with: `pipx upgrade slai-cli` to continue."  # noqa
        )
        sys.exit(1)


def main():
    entry_point.add_command(init.init)
    entry_point.add_command(model.model)
    entry_point.add_command(profile.profile)
    entry_point.add_command(version)

    try:
        entry_point()
    except HTTPError:
        handle_error(error_msg="unknown_http_error")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
