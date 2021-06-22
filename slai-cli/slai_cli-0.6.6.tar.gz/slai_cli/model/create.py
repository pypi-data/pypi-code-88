import os
import datetime
import git

from pathlib import Path
from jinja2 import Template
from requests.exceptions import HTTPError
from git import Repo

from slai.clients.project import get_project_client
from slai.clients.cli import get_cli_client

from slai_cli import log
from slai_cli.decorators import requires_slai_project
from slai_cli.exceptions import ModelExistsException, InvalidApiKey


def _create_model_folder_structure(model):
    log.action(f"Generating folder structure for model: {model['name']} ")

    cwd = Path.cwd()
    if not os.path.exists(f"{cwd}/models/{model['name']}/"):
        os.makedirs(f"{cwd}/models/{model['name']}")
        os.makedirs(f"{cwd}/models/{model['name']}/{model['model_version']['name']}")
        os.makedirs(f"{cwd}/handlers/{model['name']}/{model['model_version']['name']}")
    else:
        raise ModelExistsException("model_already_exists")

    log.action("Done.")


def _write_template_file(*, populated_templates, path, filename):
    with open(f"{path}/{filename}", "w") as f_out:
        f_out.write(populated_templates[filename])


def _populate_template_files(model):
    populated_templates = {}
    template_files = ["notebook.ipynb", "handler.py", "test_event.json"]

    pwd = Path(__file__).parent

    template_variables = {
        "SLAI_MODEL_NAME": model["name"],
        "SLAI_MODEL_CREATED_AT": datetime.datetime.now().isoformat(),
        "SLAI_MODEL_VERSION_ID": model["model_version_id"],
        "SLAI_MODEL_ID": model["id"],
        "SLAI_PROJECT_NAME": model["project_name"],
        "SLAI_PROJECT_ID": model["project_id"],
    }

    # populate model template files
    for fname in template_files:
        log.action(f"Generating: {fname} ")
        template_contents = None

        with open(f"{pwd}/templates/{fname}", "r") as f_in:
            template_contents = f_in.read()
            t = Template(template_contents)
            rendered_template = t.render(**template_variables)

            populated_templates[fname] = rendered_template
            log.action("Done.")

    cwd = Path.cwd()
    _write_template_file(
        populated_templates=populated_templates,
        path=f"{cwd}/models/{model['name']}/{model['model_version']['name']}",
        filename="notebook.ipynb",
    )

    _write_template_file(
        populated_templates=populated_templates,
        path=f"{cwd}/handlers/{model['name']}/{model['model_version']['name']}",
        filename="handler.py",
    )

    _write_template_file(
        populated_templates=populated_templates,
        path=f"{cwd}/handlers/{model['name']}/{model['model_version']['name']}",
        filename="test_event.json",
    )


def _commit_model(*, model_name):
    cwd = Path.cwd()
    repo = Repo.init(cwd)
    repo.git.add([f"models/{model_name}/*"])
    repo.git.add([f"handlers/{model_name}/*"])
    repo.index.commit(f"created new model: {model_name}")

    try:
        log.action("Pushing state to git...")
        repo.git.push("origin", "master")
        log.action("Pushed to git.")
    except (ValueError, git.exc.GitCommandError):
        log.warn(
            "WARNING: No remote is configured for this project, not pushing commits."
        )


def _validate_model_name(name):
    raise NotImplementedError


@requires_slai_project
def create_new_model(name, from_model=None):
    project_client = get_project_client(project_name=None)
    project_name = project_client.get_project_name()

    cli_client = get_cli_client()
    try:
        _validate_model_name(name)
    except Exception:
        pass

    try:
        model = cli_client.create_model(project_name=project_name, name=name)
    except HTTPError as e:
        if e.response.status_code == 400:
            error_msg = e.response.json()["detail"]["non_field_errors"][0]
            if error_msg == "duplicate_model_name":
                log.warn(f"Model already exists with name '{name}'")
                return False
            else:
                raise
        elif e.response.status_code == 401:
            log.warn("Invalid client id/secret")
            raise InvalidApiKey

    try:
        _create_model_folder_structure(model=model)
    except ModelExistsException:
        log.warn(f"Invalid model name, model '{name}' already exists.")
        raise

    # fill out all the templates
    _populate_template_files(model=model)

    # commit new model to git repo
    _commit_model(model_name=name)

    return True
