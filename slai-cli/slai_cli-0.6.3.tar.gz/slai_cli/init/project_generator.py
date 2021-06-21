import os
import click
import git
import yaml
import shutil

from jinja2 import Template
from pathlib import Path
from shutil import rmtree
from git import Repo
from requests.exceptions import HTTPError

from slai_cli import log
from slai.clients.cli import get_cli_client

from slai_cli.constants import TEMPLATE_REPO_URLS
from slai_cli.exceptions import (
    InvalidPathException,
    ProjectExistsException,
    InvalidApiKey,
)


class ProjectGenerator:
    def __init__(
        self,
        *,
        project_name,
        credentials,
    ):
        self.cli_client = get_cli_client(
            client_id=credentials["client_id"],
            client_secret=credentials["client_secret"],
        )
        try:
            self.cli_client.get_user()
        except HTTPError as e:
            if e.response.status_code == 401:
                raise InvalidApiKey("invalid_credentials")
            else:
                raise

        self.credentials = credentials
        self.project_name = project_name

    def create_new_project(self):
        click.clear()
        log.action(f"Creating a new project with name: {self.project_name}")

        slai_directory_present = Path(".slai").is_dir()
        if slai_directory_present and Path(".slai/config.yml").exists():
            log.warn(
                "You cannot create nested slai projects, try again in another directory."  # noqa
            )
            return

        try:
            local_path = self._create_project_directory()
            os.chdir(local_path)
        except InvalidPathException as e:
            log.warn(f"Invalid project name: {e}\n")
            return

        try:
            # clone template repository
            self._clone_template_repo(local_path=local_path)
        except (RuntimeError):
            return

        try:
            self.project_variables = self._generate_project_variables(self.project_name)
        except (ProjectExistsException, InvalidPathException):
            log.warn(
                f"A project or directory already exists with name '{self.project_name}', aborting."
            )
            project_path = Path(local_path)
            shutil.rmtree(project_path)
            return

        # store profile in project credentials file
        self._store_local_credentials()

        # generate template files
        self._create_project_files(local_path=local_path)

        # initialize git repo and commit
        self._init_git_repo(local_path)

    def _init_git_repo(self, local_path):
        repo = Repo.init(local_path)
        repo.git.add("--all")
        repo.index.commit("initial commit")

    def _create_project_directory(self):
        cwd = os.getcwd()
        local_path = f"{cwd}/{self.project_name}"
        if not os.path.exists(local_path):
            os.makedirs(local_path)

        if os.path.exists(f"{cwd}/{self.project_name}/.slai"):
            raise InvalidPathException("project_already_exists")

        return local_path

    def _store_local_credentials(self):
        cwd = os.getcwd()

        with open(f"{cwd}/.slai/credentials.yml", "w") as f_out:
            yaml.dump(self.credentials, f_out, default_flow_style=False)

    def _generate_project_variables(self, project_name):
        cwd = os.getcwd()
        if os.path.exists(f"{cwd}/{self.project_name}"):
            raise InvalidPathException("directory_exists")

        try:
            self.project = self.cli_client.create_project(name=self.project_name)
        except HTTPError as e:
            if e.response.status_code == 400:
                raise ProjectExistsException("duplicate_project_name")
            elif e.response.status_code == 401:
                raise InvalidApiKey("invalid_credentials")
            else:
                raise

        self.service_name = f"{project_name}-{self.project['id']}"

        variables = {
            "SLAI_SERVICE_NAME": self.service_name,
            "SLAI_PROJECT_ID": self.project["id"],
            "SLAI_PROJECT_NAME": project_name,
        }

        return variables

    def _write_template_file(self, *, project_files, path, filename):
        with open(f"{path}/{filename}", "w") as f_out:
            f_out.write(project_files[filename])

    def _create_project_files(self, *, local_path):
        project_files = {}
        template_files = ["config.yml", "docker-compose.yml"]

        pwd = Path(__file__).parent

        # populate serverless project files
        for fname in template_files:
            log.action(f"Generating: {fname} ")
            template_contents = None

            with open(f"{pwd}/templates/{fname}", "r") as f_in:
                template_contents = f_in.read()
                t = Template(template_contents)
                rendered_template = t.render(**self.project_variables)

                project_files[fname] = rendered_template
                log.action("Done.")

        # write populated template files
        self._write_template_file(
            project_files=project_files,
            path=f"{local_path}/.slai",
            filename="config.yml",
        )

        self._write_template_file(
            project_files=project_files,
            path=f"{local_path}",
            filename="docker-compose.yml",
        )

    def _clone_template_repo(self, local_path):
        log.action("Cloning template repository")

        cloned = False
        for repo_url in TEMPLATE_REPO_URLS:

            try:
                Repo.clone_from(repo_url, local_path)
                rmtree(f"{local_path}/.git")
                cloned = True
                log.action("Done.")
            except git.exc.GitCommandError:
                pass

            if cloned:
                break

        if not cloned:
            log.warn("Unable to clone template repository.")
            raise RuntimeError("unable_to_clone_template_repo")

        return local_path
