import base64
import json
import requests
import git

from pathlib import Path
from requests.exceptions import HTTPError
from git import Repo

from slai_cli import log
from slai_cli.modules.deployment_checks import check_handler_imports
from slai_cli.decorators import requires_slai_project
from slai_cli.exceptions import InvalidHandlerSyntax
from slai_cli.modules.docker_client import DockerClient
from slai_cli import constants
from slai_cli.errors import handle_error
from slai_cli.init.local_config_helper import LocalConfigHelper

from slai.clients.cli import get_cli_client
from slai.clients.model import get_model_client
from slai.clients.project import get_project_client


def _merge_requirements(model_artifact_requirements, model_handler_requirements):
    requirements = {}
    for req, version in model_artifact_requirements.items():
        requirements[req] = version

    for req, version in model_handler_requirements.items():
        requirements[req] = version

    return requirements


def _create_model_deployment(*, model_client, model_version, docker_client):
    cwd = Path.cwd()
    model = model_client.model
    model_name = model["name"]

    handler_path = f"{cwd}/handlers/{model['name']}/{model_version['name']}/handler.py"
    log.action(f"Deploying model handler stored at: {handler_path}")
    log.warn(
        "Currently, slai can only check for syntax/import errors, ensure your handler script has been tested!"  # noqa
    )

    # check for syntax errors in the model handler
    try:
        handler_source = open(handler_path, "r").read() + "\n"
        compile(handler_source, handler_path, "exec")
    except SyntaxError:
        raise InvalidHandlerSyntax("invalid_model_handler")

    handler_data = base64.b64encode(handler_source.encode("utf-8")).decode()

    try:
        model_artifact = model_client.get_latest_model_artifact(
            model_version_id=model_version["id"]
        )
    except HTTPError as e:
        if e.response.status_code == 400:
            error_msg = e.response.json()["detail"]["non_field_errors"][0]
            handle_error(error_msg=error_msg)
            return None
        else:
            raise

    # check model requirements in local container
    model_artifact_requirements = {}
    docker_client.create_model_environment(model_name=model_name)
    import_return_code = docker_client.check_model_requirements(
        model_name=model_name, requirements=model_artifact["artifact_requirements"]
    )
    if import_return_code == constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        model_artifact_requirements = model_artifact["artifact_requirements"]

    # check if model handler imports are valid
    import_return_code = check_handler_imports(
        model_name=model_name, model_version=model_version, docker_client=docker_client
    )

    if import_return_code != constants.REQUIREMENTS_RETURN_CODE_SUCCESS:
        log.warn("Deployment failed due to import error.")
        return None

    log.action("Model handler imports look valid.")
    model_handler_requirements = docker_client.generate_model_handler_requirements(
        model_name=model_name, model_version=model_version
    )

    requirements = _merge_requirements(
        model_artifact_requirements, model_handler_requirements
    )

    # requirements look valid, deploy model
    log.action("Deploying model...")
    try:
        model_deployment = model_client.create_model_deployment(
            model_artifact_id=model_artifact["id"],
            model_handler_data=handler_data,
            requirements=requirements,
        )
    except HTTPError as e:
        if e.response.status_code == 400:
            error_msg = e.response.json()["detail"][0]
            handle_error(error_msg=error_msg)
            return None
        else:
            raise

    return model_deployment


def _commit_deployment(*, model_name, model_version_name):
    cwd = Path.cwd()
    repo = Repo.init(cwd)
    repo.git.add([f"models/{model_name}/*"])
    repo.git.add([f"handlers/{model_name}/*"])
    repo.index.commit(f"deployed model: {model_name}/{model_version_name}")

    try:
        log.action("Pushing state to git...")
        repo.git.push("origin", "master")
        log.action("Pushed to git.")
    except (ValueError, git.exc.GitCommandError):
        log.warn(
            "WARNING: No remote is configured for this project, not pushing commits."
        )


@requires_slai_project
def deploy_model(*, model_name, version):
    log.action("Deploying model to slai backend.")

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
    local_model_config = local_config_helper.get_local_model_config(
        model_name=model_name, model_client=model_client
    )

    model_version_id = local_model_config.get("model_version_id")
    if model_version_id is None:
        model_version_id = model_client.model["model_version_id"]

    model_version = cli_client.retrieve_model_version_by_id(
        model_version_id=model_version_id
    )

    log.action(f"Using model version: {model_version['name']} <{model_version_id}>")

    try:
        model_deployment = _create_model_deployment(
            model_client=model_client,
            model_version=model_version,
            docker_client=docker_client,
        )
        if model_deployment is not None:
            log.action(
                f"Created new model deployment:\n{json.dumps(model_deployment, sort_keys=True, indent=4)}"  # noqa
            )
            log.action("Done.")

            # commit changes to git repo
            _commit_deployment(
                model_name=model_name, model_version_name=model_version["name"]
            )

    except InvalidHandlerSyntax:
        log.warn(
            "ERROR: Cannot deploy a model handler with syntax/import errors, please check your handler.py"  # noqa
        )
