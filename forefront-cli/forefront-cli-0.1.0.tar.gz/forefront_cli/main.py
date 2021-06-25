import click

from .init.main import init
from .versions.main import versions
from .deploy.main import deploy
from .logout.main import logout
from .projects.main import projects


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(versions)
cli.add_command(deploy)
cli.add_command(logout)
cli.add_command(projects)
