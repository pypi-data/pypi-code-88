import os
import sys
import click
import subprocess

from energinetml.core.project import WebAppProject
from energinetml.cli.utils import (
    parse_input_path,
    parse_input_project_name,
    parse_input_resource_group,
    parse_input_service_connection,
    parse_input_webapp_kind,
)


PROJECT_FILES = ('project.json', 'requirements.txt')


# -- CLI Command -------------------------------------------------------------


@click.command()
@click.option('--path', '-p',
              default=None,
              type=click.Path(dir_okay=True, resolve_path=True),
              callback=parse_input_path(PROJECT_FILES),
              help='Project path (default to current)')
@click.option('--name', '-n',
              required=False, default=None, type=str,
              callback=parse_input_project_name(),
              help='Project name')
@click.option('--resource-group', '-r', 'resource_group',
              required=False, default=None, type=str,
              callback=parse_input_resource_group(),
              help='Azure Resource Group')
@click.option('--service-connection', '-s', 'service_connection',
              required=False, default=None, type=str,
              callback=parse_input_service_connection(),
              help='Azure DevOps Service Connection name')
@click.option('--pipelines/--no-pipelines', default=None,
              help='Whether or not to setup DevOps pipelines')
@click.option('--kind', '-k', 'kind',
              required=False, default=None,
              type=click.Choice(['ASGI', 'WSGI']),
              callback=parse_input_webapp_kind(),
              help=(
                      'Kind of web server to use (ASGI or WSGI). '
                      'ASGI for flask, Django, or Falcon. '
                      'WSGI for fastapi.'
              ))
def init(path, name, resource_group, service_connection, kind, pipelines):
    """
    Create a new, empty web app project.
    \f

    :param str path:
    :param str name:
    :param str resource_group:
    :param str service_connection:
    :param energinetml.core.project.WebAppProjectKind kind:
    :param bool pipelines:
    """

    # -- Create project ------------------------------------------------------

    project = WebAppProject.create(
        path=path,
        name=name,
        kind=kind,
    )

    click.echo('Initialized the project at: %s' % path)
    click.echo('-' * 79)

    # -- Clone repo ----------------------------------------------------------

    click.echo('-' * 79)
    click.echo((
        'NOTICE: We need to clone a Git repository containing the '
        'necessary template files. This requires Git to be '
        'installed on your system.'
    ))
    click.echo('-' * 79)

    project.get_template_resolver().resolve(
        project_root_path=path,
        project_name=name,
        service_connection=service_connection,
        resource_group=resource_group,
    )

    click.echo('-' * 79)

    # -- Create DevOps pipelines ---------------------------------------------

    click.echo('Creating Azure DevOps pipelines')

    if pipelines:
        repo = _get_git_repository_name(project)

        _create_pipeline(
            name='%s infrastructure' % project.name,
            yaml_path='.azuredevops/infrastructure.yml',
            repo=repo,
            # yaml_path=os.path.join(project.path, '.azuredevops', 'infrastructure.yml'),
        )

        _create_pipeline(
            name='%s deploy' % project.name,
            yaml_path='.azuredevops/deploy.yml',
            repo=repo,
            # yaml_path=os.path.join(project.path, '.azuredevops', 'deploy.yml'),
        )


# def _commit_and_push():
#     commands = (
#         ('git', 'add', '.'),
#         ('git', 'commit', '-m"Added project files"'),
#         ('git', 'push'),
#     )
#
#     for command in commands:
#         subprocess.check_call(
#             command, stdout=sys.stdout, stderr=subprocess.STDOUT)


def _get_git_repository_name(project):
    """
    :param WebAppProject project:
    :rtype: str
    """
    path = os.getcwd()
    os.chdir(project.path)
    command = ('git', 'config', '--get', 'remote.origin.url')
    output = subprocess.check_output(command, universal_newlines=True)
    os.chdir(path)
    return output.rsplit('/')[-1].strip()


def _create_pipeline(name, yaml_path, repo):
    """
    :param str name:
    :param str yaml_path:
    :param str repo:
    """
    click.echo('Setting up DevOps pipeline: %s' % name)

    command = [
        'az', 'pipelines', 'create',
        '--name', '%s' % name,
        '--branch', 'master',
        '--org', 'https://dev.azure.com/energinet/',
        '--project', 'AnalyticsOps',
        '--repository', repo,
        '--yaml-path', '%s' % yaml_path,
        '--repository-type', 'tfsgit',
        '--skip-first-run', 'true',
    ]

    subprocess.check_call(
        command, stdout=sys.stdout, stderr=subprocess.STDOUT)
