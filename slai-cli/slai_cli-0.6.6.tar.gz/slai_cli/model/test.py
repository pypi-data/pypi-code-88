import requests

from slai.clients.project import get_project_client
from slai.clients.cli import get_cli_client
from slai.clients.model import get_model_client

from slai_cli import log
from slai_cli.errors import handle_error
from slai_cli.modules.docker_client import DockerClient
from slai_cli.modules.deployment_checks import check_handler_imports
from slai_cli.init.local_config_helper import LocalConfigHelper
from slai_cli import constants


def _run_inference(*, model_name, model_version, docker_client):
    docker_client.create_model_environment(model_name=model_name)

    exit_code = docker_client.test_model(
        model_name=model_name,
        model_version=model_version,
    )

    return exit_code


def test_model(*, model_name):
    log.action(f"Testing model: {model_name}")

    project_client = get_project_client(project_name=None)
    project = project_client.get_project()
    project_name = project["name"]
    project_id = project["id"]
    cli_client = get_cli_client()

    try:
        docker_client = DockerClient(project_name=project_name, project_id=project_id)
    except RuntimeError:
        log.warn("ERROR: Unable to connect to docker, is it installed/running?")
        return

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

    local_config_helper = LocalConfigHelper()
    local_config = local_config_helper.get_local_config()

    try:
        model_version_id = local_config["models"][model_name]["model_version_id"]
    except KeyError:
        log.action("No local config set, using default model version.")
        model_version_id = model_client.model["model_version_id"]

    model_version = cli_client.retrieve_model_version_by_id(
        model_version_id=model_version_id
    )

    log.action(f"Using model version: {model_version['name']} <{model_version_id}>")

    # check if model handler imports are valid
    import_return_code = check_handler_imports(
        model_name=model_name, model_version=model_version, docker_client=docker_client
    )

    if import_return_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.warn("Failed failed due to import error.")
        return None

    _ = _run_inference(
        model_name=model_name,
        model_version=model_version,
        docker_client=docker_client,
    )
