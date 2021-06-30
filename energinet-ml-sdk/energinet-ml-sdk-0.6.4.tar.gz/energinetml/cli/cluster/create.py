import click
import click_spinner

from energinetml.cli.utils import discover_model
from energinetml.backend import default_backend as backend
from energinetml.settings import DEFAULT_VM_CPU, DEFAULT_VM_GPU


@click.command()
@discover_model()
@click.option('--min-nodes', 'min_nodes',
              required=False, default=None, type=int,
              help='Min. number of compute nodes, if creating a new cluster')
@click.option('--max-nodes', 'max_nodes',
              required=False, default=None, type=int,
              help='Max. number of compute nodes, if creating a new cluster')
@click.option('--cluster-name', 'cluster_name',
              required=False, default=None, type=str,
              help='Name of compute cluster, if creating a new cluster')
@click.option('--specify-vm/--default', 'specify_vm',
              default=None, help=(
                  'Whether to specify exact VM size, or use default for '
                  'either CPU or GPU computation, if creating a new cluster'
              ))
@click.option('--vm-size', 'vm_size',
              required=False, default=None, type=str,
              help='VM Size to use, if using the --specify-vm parameter')
@click.option('--cpu/--gpu', 'cpu',
              default=None, help=(
                  'Whether to use default CPU- og GPU VM-size, if '
                  'using the --default parameter'
              ))
def create(model, min_nodes, max_nodes, cluster_name, specify_vm, vm_size, cpu):
    """
    Create a new compute cluster and attach it to the model.
    \f

    :param energinetml.Model model:
    :param int min_nodes:
    :param int max_nodes:
    :param str cluster_name:
    :param bool specify_vm:
    :param str vm_size:
    :param str cpu:
    """
    workspace = backend.get_workspace(
        subscription_id=model.project.subscription_id,
        resource_group=model.project.resource_group,
        name=model.project.workspace_name,
    )

    vm_size, default_cluster_name = _get_vm_size_and_cluster_name(
        workspace=workspace,
        specify_vm=specify_vm,
        vm_size=vm_size,
        cpu=cpu,
    )

    if min_nodes is None:
        min_nodes = click.prompt(
            text='Please enter minimum nodes available',
            default=0,
            type=int,
        )

    if max_nodes is None:
        max_nodes = click.prompt(
            text='Please enter maximum nodes available',
            default=1,
            type=int,
        )

    if cluster_name is None:
        cluster_name = click.prompt(
            text='Please enter a name for the compute cluster',
            default=default_cluster_name,
            type=str,
        )

    cluster_name = _normalize_cluster_name(cluster_name)
    existing_clusters = backend.get_compute_clusters(workspace)
    existing_cluster_names = [c.name for c in existing_clusters]

    while cluster_name in existing_cluster_names:
        click.echo('Cluster already exists: %s' % cluster_name)
        cluster_name = _normalize_cluster_name(click.prompt(
            text='Please enter a name for the compute cluster',
            type=str,
        ))

    click.echo('Creating compute cluster "%s" using VM Size: %s'
               % (cluster_name, vm_size))

    with click_spinner.spinner():
        backend.create_compute_cluster(
            workspace=workspace,
            name=cluster_name,
            vm_size=vm_size,
            min_nodes=min_nodes,
            max_nodes=max_nodes,
            vnet_resource_group_name=model.project.resource_group,
            vnet_name=model.project.vnet_name,
            subnet_name=model.project.subnet_name,
        )

    _update_model_properties(
        model=model,
        cluster=cluster_name,
        vm_size=vm_size,
    )


def _update_model_properties(model, cluster, vm_size):
    """
    :param energinetml.Model model:
    :param str cluster:
    :param str vm_size:
    """
    model.compute_target = cluster
    model.vm_size = vm_size
    model.save()


# -- Helper functions --------------------------------------------------------


def _get_vm_size_and_cluster_name(workspace, specify_vm, vm_size, cpu):
    """
    :param typing.Any workspace:
    """
    available_vm_sizes = backend.get_available_vm_sizes(workspace)
    available_vm_size_mapped = {vm['name']: vm for vm in available_vm_sizes}

    if specify_vm is None:
        click.echo((
            'You can either specific an exact VM Size, or use a default '
            'VM Size for either CPU or GPU computation.'
        ))
        specify_vm = click.prompt(
            text='How would you like to specify VM Size, or use a default?',
            type=click.Choice(['vmsize', 'default']),
        ) == 'vmsize'

    if specify_vm:
        vm_size, cluster_name = _get_specific_vm_size(workspace, vm_size)
    else:
        vm_size, cluster_name = _get_default_vm_size(cpu)

    while vm_size not in available_vm_size_mapped:
        click.echo('VM Size unavailable: %s' % vm_size)
        vm_size = click.prompt(
            text='Please enter a VM size',
            type=click.Choice(available_vm_size_mapped),
        )

    return vm_size, cluster_name


def _get_specific_vm_size(workspace, vm_size):
    """
    :param typing.Any workspace:
    :param str vm_size:
    :rtype: typing.Tuple[str, str]
    """
    available_vm_sizes = backend.get_available_vm_sizes(workspace)
    available_vm_size_mapped = {vm['name']: vm for vm in available_vm_sizes}

    if vm_size is None:
        vm_size = click.prompt(
            text='Please enter a VM size',
            type=click.Choice(available_vm_size_mapped),
        )

    return vm_size, _normalize_cluster_name(vm_size)


def _get_default_vm_size(cpu):
    """
    :param bool cpu:
    """
    if cpu is None:
        cpu = click.prompt(
            text='Which kind of computing would you like to use?',
            type=click.Choice(['cpu', 'gpu']),
        ) == 'cpu'

    if cpu:
        return DEFAULT_VM_CPU, 'CPU-Cluster'
    else:
        return DEFAULT_VM_GPU, 'GPU-Cluster'


def _normalize_cluster_name(cluster_name):
    """
    :param str cluster_name:
    :rtype: str
    """
    return cluster_name.replace('_', '-')
