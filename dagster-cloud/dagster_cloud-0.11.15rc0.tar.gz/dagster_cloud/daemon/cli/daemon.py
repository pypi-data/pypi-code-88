from contextlib import ExitStack, contextmanager

import click
from dagster.cli.workspace.dynamic_workspace import DynamicWorkspace
from dagster.daemon.controller import DagsterDaemonController
from dagster.utils.interrupts import capture_interrupts
from dagster_cloud.daemon.dagster_cloud_api_daemon import DagsterCloudApiDaemon
from dagster_cloud.instance import DagsterCloudAgentInstance


@click.command(
    name="run",
    help="Run the dagster-cloud agent",
)
def run_command():
    with capture_interrupts():
        with DagsterCloudAgentInstance.get() as instance:
            if instance.is_ephemeral:
                raise Exception(
                    "dagster-cloud-daemon can't run using an in-memory instance. Make sure "
                    "the DAGSTER_HOME environment variable has been set correctly and that "
                    "you have created a dagster.yaml file there."
                )

            with ExitStack() as stack:
                grpc_server_registry = stack.enter_context(instance.create_user_code_launcher())
                daemons = [stack.enter_context(DagsterCloudApiDaemon())]

                @contextmanager
                def gen_workspace(_instance):
                    with DynamicWorkspace(grpc_server_registry) as workspace:
                        yield workspace

                with DagsterDaemonController(instance, daemons, gen_workspace) as controller:
                    controller.check_daemon_loop()
