import os
import shutil
import requests
import git
import re

from columnar import columnar
from pathlib import Path
from git import Repo

from slai.clients.model import get_model_client
from slai.clients.cli import get_cli_client
from slai.clients.project import get_project_client
from slai_cli.errors import handle_error
from slai_cli.init.local_config_helper import LocalConfigHelper
from slai_cli import log


def _list_model_versions(model_versions):
    headers = ["index", "name", "id", "created"]
    data = [
        [
            index,
            mv["name"],
            mv["id"],
            mv["created"],
        ]
        for index, mv in enumerate(model_versions)
    ]
    try:
        table = columnar(data, headers, no_borders=True)
        log.info(table)
    except IndexError:
        log.warn("No model versions found.")
        return


def _create_local_version_path(
    *, model_name, previous_model_version, new_model_version
):
    log.action("Copying existing model notebook...")

    cwd = Path.cwd()
    os.makedirs(f"{cwd}/models/{model_name}/{new_model_version['name']}")
    os.makedirs(f"{cwd}/handlers/{model_name}/{new_model_version['name']}")

    # copy notebook
    notebook_to_copy = Path(
        f"{cwd}/models/{model_name}/{previous_model_version['name']}/notebook.ipynb"
    )
    new_notebook = Path(
        f"{cwd}/models/{model_name}/{new_model_version['name']}/notebook.ipynb"
    )

    shutil.copy(notebook_to_copy, new_notebook)

    re_sub_version_name = r"([a-zA-Z0-9\-\_]+\/[a-zA-Z0-9\-\_]+\/)[a-zA-Z\-\_]+"
    with open(new_notebook) as f_in:
        notebook_contents = f_in.read()
        new_notebook_contents = re.sub(
            re_sub_version_name, r"\1" + new_model_version["name"], notebook_contents
        )

    with open(new_notebook, "w") as f_out:
        f_out.write(new_notebook_contents)

    # copy handler and test event
    shutil.copytree(
        f"{cwd}/handlers/{model_name}/{previous_model_version['name']}",
        f"{cwd}/handlers/{model_name}/{new_model_version['name']}",
        dirs_exist_ok=True,
    )


def _commit_model_version(*, model_name, model_version_id, model_version_name):
    cwd = Path.cwd()
    repo = Repo.init(cwd)
    repo.git.add([f"models/{model_name}/{model_version_name}"])
    repo.git.add([f"handlers/{model_name}/{model_version_name}"])
    repo.index.commit(f"created model version: {model_name}/{model_version_name}")

    try:
        log.action("Pushing state to git...")
        repo.git.push("origin", "master")
        log.action("Pushed to git.")
    except (ValueError, git.exc.GitCommandError):
        log.warn(
            "WARNING: No remote is configured for this project, not pushing commits."
        )


def checkout_model_version(model_name, version_name=None):
    log.action(f"Retrieving model versions for model: {model_name}")

    project_client = get_project_client(project_name=None)
    project_name = project_client.get_project_name()

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

    cli_client = get_cli_client()

    model_id = model_client.model["id"]
    model_versions = cli_client.list_model_versions(model_id=model_id)
    version_names = {mv["name"]: mv["id"] for mv in model_versions}

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

    log.action(
        f"Current model version is: {model_version['name']} <{model_version_id}>"
    )

    previous_model_version = model_version

    # if a version name was specified, check if a version with that name exists
    if version_name is not None:

        # if so, just update local_config to point to that version
        if version_name in version_names:
            model_version_id_to_checkout = version_names[version_name]
            local_config_helper.checkout_model_version(
                model_name=model_name, model_version_id=model_version_id_to_checkout
            )

            log.action(f"Checked out model version: {version_name}")

        # otherwise, create a new model version with that name
        else:
            model_version = cli_client.create_model_version(
                model_id=model_id, name=version_name
            )
            model_version_id_to_checkout = model_version["id"]
            local_config_helper.checkout_model_version(
                model_name=model_name, model_version_id=model_version_id_to_checkout
            )

            _create_local_version_path(
                model_name=model_name,
                previous_model_version=previous_model_version,
                new_model_version=model_version,
            )

            _commit_model_version(
                model_name=model_name,
                model_version_id=model_version["id"],
                model_version_name=model_version["name"],
            )

            log.action(f"Checked out model version: {model_version['name']}")

    # if no version was specified, allow a user to checkout from existing model versions
    else:
        _list_model_versions(model_versions)
        model_version_index = log.action_prompt(
            "Checkout a version by index", type=int, default=0
        )
        if model_version_index < len(model_versions):
            model_version = model_versions[model_version_index]
            log.action(f"Checked out model version: {model_version['name']}")

            model_version_id_to_checkout = model_version["id"]
            local_config_helper.checkout_model_version(
                model_name=model_name, model_version_id=model_version_id_to_checkout
            )
        else:
            log.warn("Invalid model version.")
