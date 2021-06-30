from typing import Tuple

import click
from click import Context

from mb_tron import __version__
from mb_tron.cli.cmd import generate_account_cmd


@click.group()
@click.option("-c", "--config/--no-config", "config_", default=False, help="Print config and exit")
@click.option("-n", "--node", multiple=True, help="List of JSON RPC nodes, it overwrites node/nodes field in config")
@click.version_option(__version__, help="Show the version and exit")
@click.help_option(help="Show this message and exit")
@click.pass_context
def cli(ctx: Context, config_, node: Tuple[str]):
    ctx.ensure_object(dict)
    ctx.obj["config"] = config_
    ctx.obj["nodes"] = node


cli.add_command(generate_account_cmd.cli)
