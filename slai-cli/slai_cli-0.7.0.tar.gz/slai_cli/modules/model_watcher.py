import time
import click

from pathlib import Path

from slai_cli import log
from slai_cli.modules.drive_client import DriveClient
from slai_cli.modules.stoppable_thread import StoppableThread
from slai_cli.constants import MODEL_WATCH_INTERVAL_S
from slai_cli.model.save import save_model
from slai_cli.init.local_config_helper import LocalConfigHelper

CYCLES_PER_DOWNLOAD = 5


class ModelWatcher(StoppableThread):
    def __init__(self, *args, **kwargs):
        self.model_name = kwargs.pop("model_name")
        self.model_client = kwargs.pop("model_client")
        self.model_version = kwargs.pop("model_version")

        self.google_drive_integration_enabled = kwargs.pop(
            "google_drive_integration_enabled"
        )
        self._cleanup()

        super(ModelWatcher, self).__init__(*args, **kwargs)

    def _cleanup(self):
        self.idx = 0

    def pull_current_notebook(self, *, model_name, model_client):
        log.action("Downloading notebook from google drive.")

        local_config_helper = LocalConfigHelper()
        local_model_config = local_config_helper.get_local_model_config(
            model_name=model_name, model_client=model_client
        )
        model_version_id = local_model_config["model_version_id"]

        # if google drive integration is enabled, download the working notebook from drive
        if local_config_helper.drive_integration_enabled:
            cwd = Path.cwd()

            drive_client = DriveClient()
            drive_client.download_latest_model_notebook(
                local_path=f"{cwd}/models/{model_name}/{self.model_version['name']}/notebook.ipynb",
                model_notebook_google_drive_file_id=local_model_config[
                    "model_notebook_google_drive_file_id"
                ],
            )

            log.action("Done.")

        return model_version_id

    def run(self):
        while not self.stopped():
            if self.idx % CYCLES_PER_DOWNLOAD == 0:
                click.clear()

                if self.google_drive_integration_enabled:
                    self.pull_current_notebook(
                        model_name=self.model_name, model_client=self.model_client
                    )

                save_model(model_name=self.model_name)
                self.idx = 0

            self.idx += 1
            time.sleep(MODEL_WATCH_INTERVAL_S)

        self._cleanup()
