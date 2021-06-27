import click
from slai_cli import log

__version__ = "0.7.3"


def get_version():
    return __version__


@click.command()
def version():
    log.info(f"Current CLI version: {get_version()}")


@click.command()
@click.argument("name")
@click.argument("version")
def bundle(name, version):
    """Generate a template from a model version."""
