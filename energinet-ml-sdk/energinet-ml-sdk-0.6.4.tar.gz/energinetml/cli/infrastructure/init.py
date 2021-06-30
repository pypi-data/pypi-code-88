import os
import re
import sys
import click
import tempfile
import subprocess
from jinja2 import Template

from energinetml.settings import (
    TEMPLATES_GIT_URL,
    TEMPLATES_SUBNET_WHITELIST,
    TEMPLATES_IP_WHITELIST,
)


FILES_TO_COPY = (
    '.gitignore',
)

FOLDERS_TO_COPY = (
    '.azuredevops',
    'terraform',
)


# -- Input parsing and validation --------------------------------------------


def _parse_input_path(ctx, param, value):
    """
    TODO
    """
    if value is None:
        value = os.path.abspath(click.prompt(
            text='Enter project location',
            default=os.path.abspath('.'),
            type=click.Path(dir_okay=True, resolve_path=True),
        ))

    # Path points to a file?
    if os.path.isfile(value):
        click.echo('Failed to init project infrastructure.')
        click.echo((
            'The path you provided me with points to a file, and not a '
            'folder. I need a folder to put the project files in. '
            'Check your -p/--path parameter.'
        ))
        click.echo('You provided me with: %s' % value)
        raise click.Abort()

    return value


def _parse_input_project_name(ctx, param, value):
    """
    TODO
    """
    while not value or not re.findall(r'^[a-z][a-z0-9]{,10}$', value):
        if value is not None:
            click.echo('Invalid name provided')

        click.echo((
            'Provisioning cloud resources requires a name for your project '
            'which contains 11 (or less) characters. This name is used as part '
            'of the resource names, can only contain lower case letters '
            'and numbers, and must start with a letter.'
        ))

        value = click.prompt(
            text='Please enter a project name',
            type=click.STRING,
        )

    return value


def _parse_input_resource_group(ctx, param, value):
    """
    TODO
    """
    if value is None:
        value = click.prompt(
            text='Enter resource group name',
            type=str,
        )

    return value


def _parse_input_service_connection(ctx, param, value):
    """
    TODO
    """
    if value is None:
        value = click.prompt(
            text='Enter Azure DevOps service connection name',
            type=str,
        )

    return value


# -- CLI Command -------------------------------------------------------------


@click.command()
@click.option('--path', '-p',
              default=None,
              type=click.Path(dir_okay=True, resolve_path=True),
              callback=_parse_input_path,
              help='Project path (default to current)')
@click.option('--name', '-n', 'project_name',
              default=None,
              type=str,
              callback=_parse_input_project_name,
              help='Project name')
@click.option('--resource-group', '-g', 'resource_group',
              default=None,
              type=str,
              callback=_parse_input_resource_group,
              help='Azure resource group')
@click.option('--service-connection', '-s', 'service_connection',
              default=None,
              type=str,
              callback=_parse_input_service_connection,
              help='Azure DevOps service connection name')
def init_infrastructure(path, project_name, resource_group, service_connection):
    """
    Create infrastructure files for a new AnalyticsOps project.
    \f

    :param str path:
    :param str project_name:
    :param str resource_group:
    :param str service_connection:
    """

    # -- Clone repo ----------------------------------------------------------

    click.echo('-' * 79)
    click.echo((
        'NOTICE: We need to clone a Git repository containing the '
        'necessary template files. This requires Git to be '
        'installed on your system.'
    ))
    click.echo('-' * 79)

    # -- Clone repo ----------------------------------------------------------

    with tempfile.TemporaryDirectory() as clone_path:
        _clone_pipeline_files(
            clone_path=clone_path,
        )

        _parse_cloned_files(
            clone_path=clone_path,
            target_path=path,
            project_name=project_name,
            resource_group=resource_group,
            service_connection=service_connection,
        )


def _clone_pipeline_files(clone_path):
    """
    :param str clone_path:
    """
    click.echo('Cloning "%s" into "%s"' % (TEMPLATES_GIT_URL, clone_path))

    try:
        subprocess.check_call(
            args=['git', 'clone', TEMPLATES_GIT_URL, clone_path],
            stdout=sys.stdout,
            stderr=subprocess.STDOUT,
        )
    except subprocess.CalledProcessError:
        raise click.Abort()


def _parse_cloned_files(clone_path, target_path, project_name,
                        resource_group, service_connection):
    """
    :param str clone_path:
    :param str target_path:
    :param str project_name:
    :param str resource_group:
    :param str service_connection:
    """
    env = {
        'projectName': project_name,
        'resourceGroup': resource_group,
        'serviceConnection': service_connection,
        'subnetWhitelist': TEMPLATES_SUBNET_WHITELIST,
        'ipWhitelist': TEMPLATES_IP_WHITELIST,
    }

    files_to_copy = []
    files_to_copy.extend(os.path.join(clone_path, f) for f in FILES_TO_COPY)

    for folder in FOLDERS_TO_COPY:
        for root, subdirs, files in os.walk(os.path.join(clone_path, folder)):
            for file_name in files:
                files_to_copy.append(os.path.join(root, file_name))

    for file_abs_path in files_to_copy:
        rel_path = os.path.relpath(file_abs_path, clone_path)
        dst_path = os.path.join(target_path, rel_path)

        _copy_file(
            src=file_abs_path,
            dst=dst_path,
            env=env,
        )


def _copy_file(src, dst, env):
    """
    :param str src:
    :param str dst:
    :param typing.Dict[str, str] env:
    """
    dst_folder = os.path.split(dst)[0]

    with open(src) as f:
        template = Template(f.read())
        rendered = template.render(**env)

    if not os.path.isdir(dst_folder):
        os.makedirs(dst_folder)

    with open(dst, 'w') as f:
        f.write(rendered)
