import click

from grid import rich_click
from grid.client import Grid


@rich_click.command('sync-env', cls=rich_click.deprecate_grid_options())
@click.option('--config', 'config_path', required=False, help='Path to Grid config YML')
def sync_env(config_path: str):
    """
    Synchronize the requirements file with packages and versions
    from the currently active environment
    """
    client = Grid()
    req_file = client.serialize_dependencies(config_path)
    if req_file:
        message = f"""
Environment has been synced with requirements file. Make sure to
commit the file before running the experiments

        git add {req_file}
        git commit -m "{req_file} synced with current environment"
        """
        click.echo(message)
