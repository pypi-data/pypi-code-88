import requests

from slai.clients.model import get_model_client
from slai.clients.project import get_project_client
from slai.clients.cli import get_cli_client
from slai_cli.init.local_config_helper import LocalConfigHelper
from slai_cli.modules.docker_client import DockerClient
from slai_cli.errors import handle_error
from slai_cli import log, constants


def _install_requirement_interactively(*, model_name, docker_client, requirement):
    exit_code = docker_client.install_requirement(
        model_name=model_name, requirement=requirement
    )
    if exit_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.warn(f"Failed to install: {requirement}")


def _check_imports(*, model_name, model_version, docker_client):
    exit_code = docker_client.check_trainer_imports(
        model_name=model_name, model_version=model_version
    )

    if exit_code == constants.REQUIREMENTS_RETURN_CODE_MISSING_DEP:
        if log.action_confirm(
            "Looks like a dependency is missing, would you like to add it interactively?"
        ):
            requirement = log.action_prompt(
                "Add python dependency (e.g. numpy==1.20.1): ",
                type=str,
            )
            return _install_requirement_interactively(
                model_name=model_name,
                docker_client=docker_client,
                requirement=requirement,
            )
        else:
            return constants.REQUIREMENTS_RETURN_CODE_EXIT
    elif exit_code == constants.REQUIREMENTS_RETURN_CODE_FILE_NOT_FOUND_ERROR:
        log.warn(
            "Trainer script not found, run `slai model save <model_name>` to generate a training script from your notebook."  # noqa
        )
        return constants.REQUIREMENTS_RETURN_CODE_EXIT
    elif exit_code == constants.REQUIREMENTS_RETURN_CODE_IMPORT_ERROR:
        log.warn("Trainer script failed due to import error.")
        return constants.REQUIREMENTS_RETURN_CODE_EXIT

    return constants.REQUIREMENTS_RETURN_CODE_SUCCESS


def _run_trainer(*, model_name, model_version, docker_client):
    log.info("Checking if model trainer imports are valid...")

    docker_client.create_model_environment(model_name=model_name)
    import_return_code = _check_imports(
        model_name=model_name,
        model_version=model_version,
        docker_client=docker_client,
    )

    while (
        import_return_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS
        and import_return_code != constants.REQUIREMENTS_RETURN_CODE_EXIT  # noqa
    ):
        import_return_code = _check_imports(
            model_name=model_name,
            model_version=model_version,
            docker_client=docker_client,
        )

    if import_return_code == constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.info("Dependencies look valid, running training script...")
        exit_code = docker_client.run_trainer(
            model_name=model_name,
            model_version=model_version,
        )
    else:
        exit_code = import_return_code

    if exit_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.warn(f"Trainer script failed with return code: {exit_code}")
        log.warn("Training failed.")
        return False
    else:
        log.action("Training complete.")
        return True


def train_model(name):
    log.action(f"Training model: {name}")

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
        model_client = get_model_client(model_name=name, project_name=project_name)
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
        model_version_id = local_config["models"][name]["model_version_id"]
    except KeyError:
        log.action("No local config set, using default model version.")
        model_version_id = model_client.model["model_version_id"]

    model_version = cli_client.retrieve_model_version_by_id(
        model_version_id=model_version_id
    )

    log.action(f"Using model version: {model_version['name']} <{model_version_id}>")
    if not log.warn_confirm(
        "If your training script saves a model artifact, this will be uploaded to the slai backend, continue?",  # noqa
    ):
        return

    _ = _run_trainer(
        model_name=name,
        model_version=model_version,
        docker_client=docker_client,
    )
