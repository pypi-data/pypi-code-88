import os
import click

from energinetml.core.project import MachineLearningProject
from energinetml.backend import default_backend as backend
from energinetml.settings import DEFAULT_LOCATION, COMMAND_NAME
from energinetml.cli.utils import (
    parse_input_path,
    parse_input_project_name,
    parse_input_subscription_id,
    parse_input_resource_group,
    parse_input_workspace_name,
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
@click.option('--subscription', '-s', 'subscription_id',
              required=False, default=None, type=str,
              callback=parse_input_subscription_id(),
              help='Azure subscription name')
@click.option('--resource-group', '-r', 'resource_group',
              required=False, default=None, type=str,
              callback=parse_input_resource_group(),
              help='Azure Resource Group')
@click.option('--workspace', '-w', 'workspace_name',
              required=False, default=None, type=str,
              callback=parse_input_workspace_name(),
              help='AzureML Workspace name')
@click.option('--location', '-l', 'location',
              default=DEFAULT_LOCATION,
              required=False, type=str,
              help='Azure location (default: %s)' % DEFAULT_LOCATION)
def init_project(path, name, subscription_id, resource_group,
                 workspace_name, location):
    """
    Create a new, empty machine learning project.
    """
    if not os.path.isdir(path):
        os.makedirs(path)

    workspace = backend.get_workspace(
        subscription_id=subscription_id,
        resource_group=resource_group,
        name=workspace_name,
    )

    MachineLearningProject.create(
        path=path,
        name=name,
        subscription_id=subscription_id,
        resource_group=resource_group,
        workspace_name=workspace_name,
        location=location,
        vnet_name=workspace.tags['vnet_name'],
        subnet_name=workspace.tags['subnet_name'],
    )

    click.echo('-' * 79)
    click.echo('Initialized the project at: %s' % path)
    click.echo('Type "%s model init" to add a new model to the project.'
               % COMMAND_NAME)
    click.echo('-' * 79)
