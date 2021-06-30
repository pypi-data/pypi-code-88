import click

from energinetml.core.project import WebAppProject
from energinetml.cli.utils import discover_project
from energinetml.core.docker import build_webapp_docker_image


@click.command()
@click.option('--tag', '-t', required=True,
              help='Name and optionally a tag in the ‘name:tag’ format')
@discover_project(WebAppProject)
def build(tag, project):
    """
    Build web app Docker image.
    \f

    :param str tag:
    :param WebAppProject project:
    """
    build_webapp_docker_image(
        project=project,
        tag=tag,
    )
