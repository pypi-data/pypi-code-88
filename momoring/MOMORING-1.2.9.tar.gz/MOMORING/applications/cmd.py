import click
from MOMORING.api.create_project import create_project_dir
from MOMORING.api.create_test import create_test_dir


@click.group()
def cmd1():
    pass


@cmd1.command()
@click.option('-p', '--project', default=None, help='Project name.')
def init(project):
    create_project_dir(project)


@click.group()
def cmd2():
    pass


@cmd2.command()
@click.option('-p', '--path', default=None, help='Path of project directory.')
def test(path):
    create_test_dir(path)


def run():
    cli = click.CommandCollection(sources=[cmd1, cmd2])
    cli()
