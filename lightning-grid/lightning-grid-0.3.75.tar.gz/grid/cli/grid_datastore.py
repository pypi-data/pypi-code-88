import os
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import click

from grid import rich_click
from grid.cli.grid_run import get_credentials
from grid.client import Grid


def parse_name_from_source(ctx, _, name: Optional[str] = None) -> str:
    """Parses datastore name from source if name isn't provided"""
    if name:
        return name

    source = ctx.params['source']
    try:
        parse_result = urlparse(source)
    except ValueError:
        raise click.ClickException("Invalid source for datastore, please input only a local filepath or valid url")

    path = Path(parse_result.path)
    base = path.name.split(".")[0]
    return base.lower().strip()


@click.group(invoke_without_command=True)
@click.pass_context
def datastore(ctx) -> None:
    """Manages Datastore workflows."""
    client = Grid()

    if ctx.invoked_subcommand is None:
        client.list_datastores()


@datastore.command()
@rich_click.argument('session_name', nargs=1, help="The name of the session.")
@click.pass_context
def resume(ctx, session_name: str):
    """Resumes uploading a datastore."""
    client = Grid()
    if session_name == "list":
        client.list_resumable_datastore_sessions()
        return

    client.resume_datastore_session(session_name)


@datastore.command(cls=rich_click.deprecate_grid_options())
@click.option(
    '--source',
    required=True,
    help="""Source to create datastore from. This could either be a local directory (e.g: /opt/local_folder) or a remote
    HTTP URL pointing to a TAR file (e.g: http://some_domain/data.tar.gz)."""
)
@click.option('--name', type=str, required=False, help='Name of the datastore')
@click.option('--credential', type=str, required=False, help='Grid credential ID that will store this datastore.')
@click.option(
    '--compression',
    type=bool,
    required=False,
    help='Compresses datastores with GZIP when flag is passed.',
    default=False,
    is_flag=True
)
@click.pass_context
def create(ctx, source: str, name: str, credential: Optional[str] = None, compression: bool = False) -> None:
    """Creates a datastore."""
    client = Grid()
    client.check_is_blocked()

    credential = get_credentials(client=client, grid_credential=credential)

    if not name:
        name = parse_name_from_source(source)

    client.upload_datastore(source=source, credential_id=credential['credentialId'], name=name, compression=compression)


@datastore.command()
@click.pass_context
def list(ctx) -> None:
    """Lists datastores."""
    client = Grid()
    client.list_datastores()


@datastore.command(cls=rich_click.deprecate_grid_options())
@click.option('--name', type=str, required=True, help='Name of the datastore')
@click.option('--version', type=int, required=True, help='Version of the datastore')
@click.option('--credential', type=str, required=True, help='Credential Id for this datastore')
@click.pass_context
def delete(ctx, name: str, version: int, credential: str) -> None:
    """Deletes a datastore."""
    client = Grid()
    client.delete_datastore(name=name, version=version, credential_id=credential)
