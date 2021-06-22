# Copyright (c) 2014-2021 GeoSpock Ltd.

import json

import click

from geospock_cli.exceptions import CLIError
from .config_reader import ConfigReaderAndWriter
from .constants import help
from .group_commands.group_commands import group_commands
from .schema_commands.schema_commands import schema_commands
from .table_commands.table_commands import table_commands


@click.group()
@click.option('--user', default=None)
@click.option('--password', default=None, help=help.flag_password)
@click.option('--endpoint', default=None)
@click.option('--profile', default='default')
@click.option('--ca-cert-file', default=None, help=help.flag_ca_cert_file)
@click.option('--disable-verification', is_flag=True, help=help.flag_disable_verification)
@click.pass_context
def geospock_cli(ctx, user, password, endpoint, profile, ca_cert_file, disable_verification):
    ctx.ensure_object(dict)
    ctx.obj["USER"] = user
    ctx.obj["PASSWORD"] = password
    ctx.obj["ENDPOINT"] = endpoint
    ctx.obj["PROFILE"] = profile
    ctx.obj["CA_CERT_FILE"] = ca_cert_file
    ctx.obj["DISABLE_VERIFICATION"] = disable_verification


@geospock_cli.command()
@click.option('--user', default="")
@click.option('--password', default="", help=help.flag_password)
@click.option('--endpoint', default=None)
@click.option('--profile', default='default')
@click.option('--ca-cert-file', default=None, help=help.flag_ca_cert_file)
@click.option('--disable-verification', is_flag=True, help=help.flag_disable_verification)
def configure(user, password, endpoint, profile, ca_cert_file, disable_verification):
    """Saves configuration details.

    Usage: gsdb configure --user <value> [--password <value>] --endpoint <value>"""
    config_reader = ConfigReaderAndWriter(profile)
    config_reader.write_login(user, password, endpoint, ca_cert_file, disable_verification)
    logout_command = "gsdb{} configuration-clear".format(
        " --profile " + config_reader.profile if config_reader.profile != "default" else "")
    click.secho("Configuration details saved. Use '{}' to remove these details.".format(logout_command), fg="green")


@geospock_cli.command()
@click.pass_context
def configuration_clear(ctx):
    """Removes configuration details."""
    config_reader = ConfigReaderAndWriter(ctx.obj["PROFILE"])
    config_reader.write_logout()
    click.secho("Configuration details removed.", fg="green")


geospock_cli.add_command(group_commands)
geospock_cli.add_command(schema_commands)
geospock_cli.add_command(table_commands)


def wrapped_cli():
    try:
        geospock_cli(obj={})
    except CLIError as e:
        error_message = {"error": e.message}
        click.secho(json.dumps(error_message, indent=2), fg="red")
        exit(e.exit_code)


if __name__ == '__main__':
    wrapped_cli()
