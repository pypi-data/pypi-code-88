import click
import time
import requests

from pathlib import Path
from slai.clients.model import get_model_client
from slai.clients.project import get_project_client
from slai.clients.cli import get_cli_client

from slai_cli import log
from slai_cli.errors import handle_error
from slai_cli.init.local_config_helper import LocalConfigHelper
from slai_cli.modules.model_watcher import ModelWatcher
from slai_cli.modules.drive_client import DriveClient
from slai_cli.modules.docker_client import DockerClient
from slai_cli.constants import MODEL_WATCH_INTERVAL_S
from slai_cli.exceptions import RetryException


def _upload_local_notebook(
    local_config_helper, model_client, model_name, model_version
):
    local_model_config = local_config_helper.get_local_model_config(
        model_name=model_name, model_client=model_client
    )
    model_notebook_google_drive_file_id = local_model_config.get(
        "model_notebook_google_drive_file_id"
    )
    model_google_drive_folder_id = local_model_config.get(
        "model_google_drive_folder_id"
    )
    cwd = Path.cwd()

    drive_client = DriveClient()
    model_notebook_google_drive_file_id = drive_client.upload_model_notebook(
        model_name=model_name,
        model_google_drive_folder_id=model_google_drive_folder_id,
        notebook_path=f"{cwd}/models/{model_name}/{model_version['name']}/notebook.ipynb",
        file_id=model_notebook_google_drive_file_id,
    )

    return (
        f"https://colab.research.google.com/drive/{model_notebook_google_drive_file_id}"
    )


def open_model(model_name, watch):
    log.action("Opening notebook in browser.")

    local_config_helper = LocalConfigHelper()
    local_config_helper.check_local_config()

    project_client = get_project_client(project_name=None)
    project = project_client.get_project()
    project_name = project["name"]
    project_id = project["id"]

    cli_client = get_cli_client()

    try:
        model_client = get_model_client(
            model_name=model_name, project_name=project_name
        )
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            error_msg = e.response.json()["detail"]["non_field_errors"][0]
            handle_error(error_msg=error_msg)
            return None
        else:
            raise

    local_model_config = local_config_helper.get_local_model_config(
        model_name=model_name, model_client=model_client
    )

    model_version_id = local_model_config.get("model_version_id")
    if model_version_id is None:
        model_version_id = model_client.model["model_version_id"]

    model_version = cli_client.retrieve_model_version_by_id(
        model_version_id=model_version_id
    )

    log.action(f"Opening model version: {model_version['name']} <{model_version_id}>")

    model_notebook_url = None
    if local_config_helper.drive_integration_enabled:
        model_notebook_url = _upload_local_notebook(
            local_config_helper=local_config_helper,
            model_client=model_client,
            model_name=model_name,
            model_version=model_version,
        )
    else:
        try:
            docker_client = DockerClient(
                project_name=project_name, project_id=project_id
            )
        except RuntimeError:
            log.warn("ERROR: Unable to connect to docker, is it installed/running?")
            return

        try:
            server_started = docker_client.launch_local_notebook_server(
                model_name=model_name
            )
        except RetryException:
            server_started = docker_client.launch_local_notebook_server(
                model_name=model_name
            )

        if server_started:
            model_notebook_url = f"http://localhost:{docker_client.host_port}/notebooks/models/{model_name}/{model_version['name']}/notebook.ipynb"  # noqa
            log.action("Waiting for notebook server to start...")
            time.sleep(5.0)
        else:
            log.warn("Failed to start local notebook server.")
            return

    if model_notebook_url:
        click.launch(f"{model_notebook_url}")
    else:
        log.warn("No remote notebook URL found.")
        return

    if watch and local_config_helper.drive_integration_enabled:
        model_watching_thread = ModelWatcher(
            model_name=model_name,
            model_client=model_client,
            model_version=model_version,
            google_drive_integration_enabled=local_config_helper.drive_integration_enabled,
        )
        model_watching_thread.daemon = True
        model_watching_thread.start()

        while True:
            try:
                time.sleep(MODEL_WATCH_INTERVAL_S)
            except KeyboardInterrupt:
                model_watching_thread.stop()
                model_watching_thread.join()
                break

        log.action("Goodbye.")
