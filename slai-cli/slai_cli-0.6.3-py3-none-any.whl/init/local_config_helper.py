import os
import yaml

from pathlib import Path
from slai_cli import log, constants
from slai_cli.modules.drive_client import DriveClient
from slai.clients.project import get_project_client
from slai.clients.identity import get_identity_client
from slai.clients.cli import get_cli_client


class LocalConfigHelper:
    def __init__(self):
        self.local_path = os.getcwd()
        self.project_client = get_project_client(project_name=None)
        self.identity_client = get_identity_client()
        self.cli_client = get_cli_client()

        self.user_info = self.identity_client.get_user()

        self.drive_integration_enabled = False
        if (
            self.user_info["identity_user_google_auth"] is not None
            and self.user_info["identity_user_google_auth"]["enabled"]
        ):
            self.drive_integration_enabled = True
            self.drive_client = DriveClient()

    def check_local_config(self):
        self.project_name = self.project_client.get_project_name()
        self.project = self.project_client.get_project()
        self.service_name = f"{self.project['name']}-{self.project['id']}"
        self.local_config = self._load_local_config()
        self.google_drive_config = self._load_google_drive_config()

    def get_local_config(self):
        local_config = None

        with open(constants.LOCAL_CONFIG_PATH, "r") as f_in:
            try:
                local_config = yaml.safe_load(f_in)
            except yaml.YAMLError:
                pass

        return local_config

    def get_google_drive_config(self):
        google_drive_config = None

        if os.path.exists(constants.GOOGLE_DRIVE_CONFIG_PATH):
            with open(constants.GOOGLE_DRIVE_CONFIG_PATH, "r") as f_in:
                try:
                    google_drive_config = yaml.safe_load(f_in)
                except yaml.YAMLError:
                    pass

        return google_drive_config

    def get_local_model_config(self, *, model_name, model_client):
        local_config = self.get_local_config()
        google_drive_config = self.get_google_drive_config()
        local_model_config = None

        if model_name not in local_config["models"].keys():
            model_version_id = model_client.model["model_version_id"]

            self.update_local_model_config(
                model_name=model_name,
                model_version_id=model_version_id,
            )

            local_config = self.get_local_config()

        if (
            self.drive_integration_enabled
            and model_name not in google_drive_config["models"].keys()
        ):
            model_version_id = local_config["models"][model_name]["model_version_id"]
            log.action("Uploading template notebook to google drive.")

            cwd = Path.cwd()

            model_google_drive_folder_id = self.drive_client.create_model_folder(
                model_name=model_name,
                project_google_drive_folder_id=google_drive_config[
                    "project_google_drive_folder_id"
                ],
            )

            model_version = self.cli_client.retrieve_model_version_by_id(
                model_version_id=model_version_id
            )

            model_notebook_google_drive_file_id = self.drive_client.upload_model_notebook(
                model_name=model_name,
                model_google_drive_folder_id=model_google_drive_folder_id,
                notebook_path=f"{cwd}/models/{model_name}/{model_version['name']}/notebook.ipynb",
            )

            self.update_google_drive_config(
                model_name=model_name,
                model_version_id=model_version_id,
                model_google_drive_folder_id=model_google_drive_folder_id,
                model_notebook_google_drive_file_id=model_notebook_google_drive_file_id,
            )
            google_drive_config = self.get_google_drive_config()

        local_model_config = local_config["models"][model_name]

        if self.drive_integration_enabled:
            google_drive_model_config = google_drive_config["models"][model_name]
            local_model_config[
                "model_google_drive_folder_id"
            ] = google_drive_model_config["model_google_drive_folder_id"]
            local_model_config[
                "model_notebook_google_drive_file_id"
            ] = google_drive_model_config["model_notebook_google_drive_file_id"]

        return local_model_config

    def update_google_drive_config(
        self,
        *,
        model_name,
        model_version_id,
        model_google_drive_folder_id=None,
        model_notebook_google_drive_file_id=None,
    ):
        google_drive_config = self.get_google_drive_config()

        model_config = {}
        model_config["model_version_id"] = model_version_id

        if model_google_drive_folder_id is not None:
            model_config["model_google_drive_folder_id"] = model_google_drive_folder_id

        if model_notebook_google_drive_file_id is not None:
            model_config[
                "model_notebook_google_drive_file_id"
            ] = model_notebook_google_drive_file_id

        google_drive_config["models"][model_name] = model_config

        with open(constants.GOOGLE_DRIVE_CONFIG_PATH, "w") as f_out:
            yaml.dump(google_drive_config, f_out, default_flow_style=False)

    def update_local_model_config(
        self,
        *,
        model_name,
        model_version_id,
    ):
        local_config = self.get_local_config()

        model_config = {}
        model_config["model_version_id"] = model_version_id

        local_config["models"][model_name] = model_config

        with open(constants.LOCAL_CONFIG_PATH, "w") as f_out:
            yaml.dump(local_config, f_out, default_flow_style=False)

    def checkout_model_version(
        self,
        *,
        model_name,
        model_version_id,
    ):
        local_config = self.get_local_config()
        local_config["models"][model_name]["model_version_id"] = model_version_id

        with open(constants.LOCAL_CONFIG_PATH, "w") as f_out:
            yaml.dump(local_config, f_out, default_flow_style=False)

    def _load_local_config(self):
        if not os.path.exists(constants.LOCAL_CONFIG_PATH):
            log.info("No local configuration found, creating new config file.")

            config_data = {
                "models": {},
            }

            with open(constants.LOCAL_CONFIG_PATH, "w") as f_out:
                yaml.dump(config_data, f_out, default_flow_style=False)

    def _load_google_drive_config(self):
        if (
            not os.path.exists(constants.GOOGLE_DRIVE_CONFIG_PATH)
            and self.drive_integration_enabled
        ):
            log.info(
                "No google drive configuration found, creating new file and uploading configuration"
            )
            project_folder_id = self._create_google_drive_folder()

            config_data = {
                "project_google_drive_folder_id": project_folder_id,
                "models": {},
            }

            with open(constants.GOOGLE_DRIVE_CONFIG_PATH, "w") as f_out:
                yaml.dump(config_data, f_out, default_flow_style=False)

    def _create_google_drive_folder(self):
        log.action("Creating project folder in google drive")

        project_folder_id = self.drive_client.create_project_folder(
            folder_name=f"slai-{self.service_name}"
        )

        log.action("Done.")
        return project_folder_id
