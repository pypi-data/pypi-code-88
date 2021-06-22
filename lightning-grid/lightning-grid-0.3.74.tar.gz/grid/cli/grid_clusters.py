import asyncio
import json
from typing import Optional

import click
from google.protobuf.json_format import MessageToJson
from rich.table import Table
from rich.text import Text

from grid import rich_click

# Not sure why we have this import Console
# When I import it normally from rich I have
# import issues
from grid.client import Console, credentials_from_env, Grid
from grid.core.formatter import Formatable, print_to_console
from grid.v1.cluster_pb2 import *
from grid.v1.cluster_service_pb2 import *
from grid.v1.cluster_service_pb2_grpc import ClusterServiceStub
from grid.v1.metadata_pb2 import Metadata


class ClusterList(Formatable):
    def __init__(self, clusters: [Cluster]):
        self.clusters = clusters

    def as_json(self) -> str:
        return json.dumps([
            json.loads(MessageToJson(x, including_default_value_fields=True, sort_keys=True)) for x in self.clusters
        ])

    def as_table(self) -> Table:
        table = Table("id", "name", "status", show_header=True, header_style="bold green")
        phases = {
            ClusterState.CLUSTER_STATE_QUEUED: Text("queued", style="bold yellow"),
            ClusterState.CLUSTER_STATE_PENDING: Text("pending", style="bold yellow"),
            ClusterState.CLUSTER_STATE_RUNNING: Text("running", style="bold green"),
            ClusterState.CLUSTER_STATE_FAILED: Text("failed", style="bold red"),
        }
        for cluster in self.clusters:
            table.add_row(
                cluster.metadata.id,
                cluster.metadata.name,
                phases[cluster.status.phase],
            )
        return table


@rich_click.group(invoke_without_command=True)
@click.pass_context
def clusters(ctx: click.Context) -> None:
    if ctx.invoked_subcommand is not None:
        return

    async def list_clusters() -> [Cluster]:
        async with Grid.grpc_channel() as conn:
            resp: 'ListClustersResponse' = await ClusterServiceStub(conn).ListClusters(
                ListClustersRequest(
                    cluster_type_not_in=[
                        ClusterType.CLUSTER_TYPE_LEGACY,
                        ClusterType.CLUSTER_TYPE_UNSPECIFIED,
                    ],
                    phase_not_in=[
                        ClusterState.CLUSTER_STATE_DELETED,
                    ]
                )
            )
            return resp.cluster

    clusters: [Cluster] = asyncio.run(list_clusters())
    print_to_console(ctx, ClusterList(clusters))


default_instance_types = [
    "g2.8xlarge",
    "g3.16xlarge",
    "g3.4xlarge",
    "g3.8xlarge",
    "g3s.xlarge",
    "g4dn.12xlarge",
    "g4dn.16xlarge",
    "g4dn.2xlarge",
    "g4dn.4xlarge",
    "g4dn.8xlarge",
    "g4dn.metal",
    "g4dn.xlarge",
    "p2.16xlarge",
    "p2.8xlarge",
    "p2.xlarge",
    "p3.16xlarge",
    "p3.2xlarge",
    "p3.8xlarge",
    "p3dn.24xlarge",
    "t2.large",
    "t2.medium",
    "t2.xlarge",
    "t2.2xlarge",
    "t3.large",
    "t3.medium",
    "t3.xlarge",
    "t3.2xlarge",
]


@clusters.command()
@click.argument('name', type=str)
@click.option('--external-id', 'external_id', type=str, required=True)
@click.option('--role-arn', 'role_arn', type=str, required=True)
@click.option('--region', 'region', type=str, required=False, default="us-east-1")
@click.option('--instance-types', 'instance_types', type=str, required=False, default=",".join(default_instance_types))
@click.pass_context
def aws(
    ctx: click.Context,
    name: str,
    external_id: str,
    role_arn: str,
    region: str,
    instance_types: str,
) -> None:
    async def f():
        creds = credentials_from_env()
        async with Grid.grpc_channel() as conn:
            return await ClusterServiceStub(conn).CreateCluster(
                CreateClusterRequest(
                    cluster=Cluster(
                        metadata=Metadata(
                            id=name,
                            name=name,
                        ),
                        spec=ClusterSpec(
                            desired_state=CLUSTER_STATE_RUNNING,
                            user_id=creds.user_id,
                            cluster_type=CLUSTER_TYPE_BYOC,
                            driver=ClusterDriver(
                                kubernetes=KubernetesClusterDriver(
                                    aws=AWSClusterDriverSpec(
                                        region=region,
                                        role_arn=role_arn,
                                        external_id=external_id,
                                        instance_types=[InstanceSpec(name=x) for x in instance_types.split(",")]
                                    ),
                                ),
                            )
                        )
                    )
                )
            )

    resp = asyncio.run(f())
    print(MessageToJson(resp.cluster))
