import os
import click

from energinetml.cli.utils import discover_project
from energinetml.cli.cluster import create_cluster, change_cluster
from energinetml.settings import COMMAND_NAME
from energinetml.core.project import MachineLearningProject
from energinetml.core.model import (
    Model,
    DEFAULT_FILES_INCLUDE,
    DEFAULT_FILES_EXCLUDE,
)


# Constants  TODO Move to Project class?
MODEL_FILES = ('__init__.py', 'model.json', 'model.py')


# -- Input parsing and validation --------------------------------------------


def _parse_input_model_name(ctx, param, value):
    """
    TODO
    """
    if value is None:
        value = click.prompt(
            text='Please enter a model name',
            type=str,
        )
    return value


# -- CLI Command -------------------------------------------------------------


@click.command()
@discover_project(MachineLearningProject)
@click.option('--name', '-n',
              required=False, default=None, type=str,
              callback=_parse_input_model_name,
              help='Model name (must be unique in project)')
@click.option('--cluster', '-c',
              required=False, default=None,
              type=click.Choice(['new', 'existing', 'no'], case_sensitive=False),
              help=(
                  'Whether to create a new Compute Cluster for the model, '
                  'attach an existing cluster, or no cluster setup.'
              ))
@click.pass_context
def init_model(ctx, name, cluster, project):
    """
    Create a new, empty machine learning model.
    \f

    TODO Verify name complies to naming conventions
    TODO Length of ComputeTarget name must be <= 16

    :param click.Context ctx:
    :param str name:
    :param bool cluster:
    :param MachineLearningProject project:
    """

    # -- Target folder -------------------------------------------------------

    path = project.default_model_path(name)

    # Confirm overwrite files if they exists
    for filename in MODEL_FILES:
        if os.path.isfile(os.path.join(path, filename)):
            click.echo('File already exists: %s'
                       % os.path.join(path, filename))
            if not click.confirm('Really override existing %s?' % filename):
                raise click.Abort()

    # Create empty folder is necessary
    if not os.path.isdir(path):
        os.makedirs(path)

    # -- Create model --------------------------------------------------------

    model = Model.create(
        path=path,
        name=name,
        experiment=name,
        compute_target=None,
        vm_size=None,
        files_include=DEFAULT_FILES_INCLUDE,
        files_exclude=DEFAULT_FILES_EXCLUDE,
    )

    click.echo('-' * 79)
    click.echo('Initialized the model at: %s' % path)
    click.echo('')
    click.echo((
        'Next step is to implement your model script! I have created an '
        'empty model template for you. It is called %s and is located in '
        'the model directory. Also, remember to add your model\'s '
        'dependencies to requirements.txt (located at the root '
        'of your project).'
    ) % Model.SCRIPT_FILE_NAME)
    click.echo('')
    click.echo('Use "%s model ..." to interact with your model afterwards.'
               % COMMAND_NAME)
    click.echo('-' * 79)

    # -- Compute cluster -----------------------------------------------------

    if cluster is None:
        cluster = click.prompt(
            text=(
                'Would you like to setup a new compute cluster for your model, '
                'or use an existing cluster?'
            ),
            type=click.Choice(['new', 'existing', 'no'], case_sensitive=False),
        )

    if cluster == 'new':
        ctx.invoke(create_cluster, model=model)
    elif cluster == 'existing':
        ctx.invoke(change_cluster, model=model)
