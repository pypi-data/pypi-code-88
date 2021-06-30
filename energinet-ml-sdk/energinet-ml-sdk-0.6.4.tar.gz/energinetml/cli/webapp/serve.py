import click

from energinetml.core.project import WebAppProject
from energinetml.cli.utils import discover_project


@click.command()
@discover_project(WebAppProject)
@click.option('--host', default='127.0.0.1', type=str,
              help='Host to serve on (default: 127.0.0.1)')
@click.option('--port', default=8080, type=int,
              help='Port to serve on (default: 8080)')
def serve(host, port, project):
    """
    Serve a HTTP web API for model prediction.
    \f

    :param str host:
    :param int port:
    :param energinetml.core.project.WebAppProject project:
    """
    engine = project.get_engine()
    engine.serve(project)
