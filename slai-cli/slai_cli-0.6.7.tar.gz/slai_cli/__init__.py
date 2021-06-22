import click
from slai_cli import log

__version__ = "0.6.7"


def get_version():
    return __version__


@click.command()
def version():
    log.info(f"Current CLI version: {get_version()}")
