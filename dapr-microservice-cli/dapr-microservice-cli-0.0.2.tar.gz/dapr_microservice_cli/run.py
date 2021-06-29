import click

from .commands import project


@click.group()
def top_cli():

    pass


@top_cli.command()
def version():
    """Display current cli version"""
    click.echo('v0.0.2')


cli = click.CommandCollection(sources=[top_cli, project.cli])


if __name__ == '__main__':
    cli()
