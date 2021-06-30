import click

from energinetml.cli.utils import discover_model
from energinetml.backend import default_backend as backend
from energinetml.settings import PACKAGE_NAME


@click.command()
@discover_model()
@click.option('--cluster-name', 'cluster_name',
              required=False, default=None, type=str,
              help='Name of compute cluster, if creating a new cluster')
def change(model, cluster_name):
    """
    Switch to use another (existing) compute cluster.
    \f

    :param energinetml.Model model:
    :param str cluster_name:
    """
    workspace = backend.get_workspace(
        subscription_id=model.project.subscription_id,
        resource_group=model.project.resource_group,
        name=model.project.workspace_name,
    )

    existing_clusters = backend.get_compute_clusters(workspace)
    existing_clusters_mapped = {c.name: c for c in existing_clusters}
    existing_cluster_names = [c.name for c in existing_clusters]

    if not existing_clusters:
        click.echo('No compute clusters exists in workspace "%s".'
                   % workspace.name)
        click.echo('Run "%s cluster create" to create a new cluster.'
                   % PACKAGE_NAME)
        raise click.Abort()

    while cluster_name not in existing_cluster_names:
        cluster_name = click.prompt(
            text='Please enter name of compute cluster to use',
            type=click.Choice(existing_cluster_names),
            default=model.compute_target,
        )

    click.echo('Using cluster "%s" from now on.' % cluster_name)

    cluster = existing_clusters_mapped[cluster_name]

    _update_model_properties(
        model=model,
        cluster_name=cluster_name,
        vm_size=cluster.vm_size,
    )


def _update_model_properties(model, cluster_name, vm_size):
    """
    :param energinetml.Model model:
    :param str cluster_name:
    :param str vm_size:
    """
    model.compute_target = cluster_name
    model.vm_size = vm_size
    model.save()
