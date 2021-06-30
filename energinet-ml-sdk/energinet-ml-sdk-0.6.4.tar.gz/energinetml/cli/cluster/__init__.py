import click

from .create import create as create_cluster
from .change import change as change_cluster


@click.group()
def cluster_group():
    """
    Manage compute clusters for a model.
    """
    pass


cluster_group.add_command(create_cluster)
cluster_group.add_command(change_cluster)
