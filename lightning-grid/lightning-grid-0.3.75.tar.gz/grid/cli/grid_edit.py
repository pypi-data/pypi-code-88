import asyncio

import click
from google.protobuf.json_format import MessageToJson, Parse

from grid import rich_click
from grid.client import Grid
from grid.v1.cluster_pb2 import *
from grid.v1.cluster_service_pb2 import *
from grid.v1.cluster_service_pb2_grpc import *
from grid.v1.metadata_pb2 import Metadata


@rich_click.group()
def edit() -> None:
    pass


@edit.command()
@rich_click.argument('cluster', type=str)
def cluster(cluster: str):
    """Edit existing cluster"""
    async def f():
        async with Grid.grpc_channel() as conn:
            cluster_service = ClusterServiceStub(conn)
            resp: 'GetClusterResponse' = await cluster_service.GetCluster(GetClusterRequest(id=cluster), )
            cl = resp.cluster
            before = MessageToJson(
                cl,
                including_default_value_fields=True,
            )
            after = click.edit(before)
            if after is None or after == before:
                click.echo("cluster unchanged")
                return
            cl = Cluster()
            Parse(
                text=after,
                message=cl,
            )
            resp: UpdateClusterResponse = await cluster_service.UpdateCluster(UpdateClusterRequest(cluster=cl))
            click.echo(f"{resp.cluster}")

    asyncio.run(f())
