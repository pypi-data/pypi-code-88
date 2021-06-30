import click
import random
from unittest.mock import Mock

import azureml
from azureml.core import Experiment

from energinetml.core.files import FileMatcher, temporary_folder
from .backend import AzureBackend
from .logger import AzureMlLogger
from .datasets import DownloadedAzureMLDataStore

from energinetml.settings import PYTHON_VERSION, PACKAGE_NAME, PACKAGE_VERSION


class AzureInteractiveTrainingContext:
    """Azure interactive context that enables an interactive session with Azure ML"""

    def __init__(
        self,
        experiment_name,
        workspace_name,
        subscription_id,
        resource_group,
        dataset_dependecies,
        force_download=False,
    ):
        """
        :param str experiment_name:
        :param str workspace_name:
        :param str subscription_id:
        :param str resource_group:
        :param list[str] dataset_dependecies:
        :param bool force_download:
        """
        backend = AzureBackend()

        az_workspace = backend.get_workspace(
            name=workspace_name,
            subscription_id=subscription_id,
            resource_group=resource_group,
        )

        az_experiment = Experiment(
            workspace=az_workspace,
            name=experiment_name,
        )

        datasets_parsed = [dataset.split(":") for dataset in dataset_dependecies]

        model_class = Mock()
        model_class.data_folder_path = "data"

        datasets = DownloadedAzureMLDataStore.from_model(
            model=model_class,
            datasets=datasets_parsed,
            workspace=az_workspace,
            force_download=force_download,
        )

        try:
            self.az_run = az_experiment.start_logging(snapshot_directory=None)
        except azureml._common.exceptions.AzureMLException as e:
            raise self.backend.parse_azureml_exception(e)

        logger = AzureMlLogger(self.az_run)

        seed = random.randint(0, 10 ** 9)

        tags = {
            "seed": seed,
            PACKAGE_NAME: PACKAGE_VERSION,
            "python-version": PYTHON_VERSION,
            "datasets": dataset_dependecies,
        }

        self.az_run.set_tags(tags)

        self.datasets = datasets
        self.logger = logger
        self.seed = seed

    def stop(self):
        """
        Stops the interactive session with AzureML.
        Takes snapshot and marks the experiment as completed.
        """
        if self.az_run is not None:
            if click.confirm(
                "Do you want to end the job? (Remember to save file before confirming)"
            ):
                files = FileMatcher(".", include=["*.py", "*.ipynb"])
                files = [(name, name) for name in files]
                with temporary_folder(files) as temp_path:
                    self.az_run.take_snapshot(temp_path)

                self.az_run.complete()
                self.az_run = None
                self.logger.run = None
        else:
            print("Context already stopped")
