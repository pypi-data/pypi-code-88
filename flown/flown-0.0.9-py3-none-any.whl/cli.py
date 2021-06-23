import os
import click
from mlflow.server import _run_server as mlflow_run_server, BACKEND_STORE_URI_ENV_VAR, ARTIFACT_ROOT_ENV_VAR
from mlflow.utils import cli_args as mlflow_cli_args


@click.group()
def cli():
    """Butterfly Command line interface."""
    pass


@cli.command()
@click.option(
    "--backend-store-uri",
    metavar="PATH",
    # default=DEFAULT_LOCAL_FILE_AND_ARTIFACT_PATH,
    default='project://./mlruns',
    help="URI to which to persist experiment and run data. "
    "`project` scheme required. "
    "The `project` scheme works just like the `file` scheme, "
    "except that it uses uuid instead of incremental int to generate the example-id."
    "(e.g. 'project:///absolute-path/to/dir') or "
    "(e.g. 'project://./relative-path/to/dir'). "
    "By default, data will be logged to the ./mlruns directory.",
)
@click.option(
    "--default-artifact-root",
    metavar="URI",
    help="Path to local directory to store artifacts, for new experiments. "
    "Note that this flag does not impact already-created experiments. "
)
@mlflow_cli_args.PORT
@mlflow_cli_args.HOST
def ui(backend_store_uri, default_artifact_root, port, host):
    """
    Run the MLflow server with Specified ProjectStore directory and Specified Artifact directory.
    :return: None
    """

    print(f"backend_store_uri = {backend_store_uri}")

    # mlflowは環境変数から保存先を取得する
    if backend_store_uri:
        os.environ[BACKEND_STORE_URI_ENV_VAR] = backend_store_uri
    if default_artifact_root:
        os.environ[ARTIFACT_ROOT_ENV_VAR] = default_artifact_root

    mlflow_run_server(file_store_path=backend_store_uri,
                      default_artifact_root=default_artifact_root,
                      port=port, host=host)

    click.echo('See you.')
