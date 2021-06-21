# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""
Contains the functionality for managing model analyses in Azure Machine Learning.

This module contains methods for retrieving model analyses, dashboards, and snapshotted data.
"""
import joblib
import json
import os
import pandas as pd
import pickle as pkl
import pyarrow.parquet as pq
from tempfile import TemporaryDirectory
from typing import Dict, List, Optional  # noqa: F401

from azureml._base_sdk_common._docstring_wrapper import experimental
from azureml._common._error_definition import AzureMLError
from azureml._restclient.constants import RunStatus
from azureml.core import Datastore, Run, Workspace
from azureml.core.run import RUNNING_STATES
from azureml.data.abstract_datastore import AbstractDatastore
from azureml.exceptions import UserErrorException
from azureml.responsibleai.tools.model_analysis._aml_init_dto import AMLInitDTO
from azureml.responsibleai.tools.model_analysis._constants import PropertyKeys, ModelAnalysisFileNames

from azureml.responsibleai.tools.model_analysis._managers.explanation_manager import ExplanationManager

from azureml.responsibleai.common._errors.error_definitions import (
    AnalysisInitFailedError, AnalysisInitNotCompletedError)


@experimental
class ModelAnalysisRun(Run):
    """Run object containing pointers to other model analyses."""

    def __init__(self, experiment, run_id, *args, **kwargs):
        """
        Initialize a ModelAnalysisRun.

        :param experiment: The experiment associated with the run.
        :type experiment: azureml.core.Experiment
        :param run_id: The ID of the run.
        :type run_id: str
        """
        super().__init__(experiment, run_id, *args, **kwargs)
        self._settings = None  # type: Optional[AMLInitDTO]
        self._output_directory = None  # type: Optional[str]
        self._datastore = None  # type: Optional[Datastore]

    @property
    def settings(self) -> AMLInitDTO:
        """Get the settings used when creating this run."""
        if not self._settings:
            status = self.get_status()
            if status in [RunStatus.FAILED, RunStatus.CANCELED, RunStatus.CANCEL_REQUESTED]:
                raise UserErrorException._with_error(
                    AzureMLError.create(
                        AnalysisInitFailedError,
                        portal_url=str(self.get_portal_url())
                    )
                )
            elif status in RUNNING_STATES:
                raise UserErrorException._with_error(
                    AzureMLError.create(
                        AnalysisInitNotCompletedError,
                        portal_url=str(self.get_portal_url())
                    )
                )
            with TemporaryDirectory() as td:
                self.download_file(ModelAnalysisFileNames.SETTINGS, output_file_path=td)
                self._settings = joblib.load(os.path.join(td, ModelAnalysisFileNames.SETTINGS))
        # Following assert needed for return type
        assert self._settings
        return self._settings

    @property
    def datastore(self) -> AbstractDatastore:
        """
        Get the datastore where the analysis artifacts are stored.

        This may differ from the workspace's default datastore, and may not be accessible in some environments.
        """
        if not self._datastore:
            self._datastore = Datastore.get(self.experiment.workspace, self.settings.confidential_datastore_name)
        return self._datastore

    @property
    def analysis_id(self) -> str:
        """Get the id for this model analysis, used for linking other analyses together."""
        return str(self.settings.analysis_id)

    @property
    def explanation_manager(self) -> ExplanationManager:
        """Get an ExplanationManager for accessing the computed explanations."""
        return ExplanationManager(self.experiment.workspace.service_context,
                                  self.experiment.name,
                                  self.analysis_id)

    @staticmethod
    def get_model_analysis_runs(
            workspace: Workspace,
            model_analysis_id: Optional[str] = None,
            model_id: Optional[str] = None) -> List['ModelAnalysisRun']:
        """
        Fetch the model analysis assets for this workspace.

        :param workspace: The workspace to fetch assets from.
        :param model_analysis_id: The specific model analysis run to fetch.
        :param model_id: Which model to fetch the assets for.
        """
        model_analysis_runs: List['ModelAnalysisRun'] = []
        property_filters = {}
        if model_analysis_id:
            property_filters[PropertyKeys.ANALYSIS_ID] = model_analysis_id
        if model_id:
            property_filters[PropertyKeys.MODEL_ID] = model_id
        for _, experiment in workspace.experiments.items():
            # TODO mark these as type _MODEL_ANALYSIS_RUN_TYPE and pass type=_MODEL_ANALYSIS_RUN_TYPE
            assets = Run.list(experiment=experiment, properties=property_filters, status=RunStatus.COMPLETED)
            # Once these are marked correctly, run.list should return the correct type, but until then we manually case
            model_analysis_runs.extend(
                [ModelAnalysisRun(experiment, asset.id) for asset in assets
                 if PropertyKeys.ANALYSIS_ID in asset.properties])
        return model_analysis_runs

    def download_data(self, output_directory: str = None) -> None:
        """
        Download all the data associated with this model analysis.

        :param output_directory: The directory in which the files will be saved.
        """
        self.datastore.download(target_path=output_directory, prefix=self.settings.train_snapshot_id)
        self.datastore.download(target_path=output_directory, prefix=self.settings.test_snapshot_id)
        self._output_directory = output_directory

    def get_train_data(self, fetch_subsample: bool = False) -> pd.DataFrame:
        """Fetch the training data used for this model analysis."""
        if fetch_subsample:
            return self._get_data_from_run(
                file_name=ModelAnalysisFileNames.TRAIN_DATA_SUBSAMPLE)
        return self._get_data_from_snapshot(
            file_name=ModelAnalysisFileNames.TRAIN_DATA,
            datastore_prefix=self.settings.datastore_prefix,
            snapshot_id=self.settings.train_snapshot_id)

    def get_train_labels(self, fetch_subsample: bool = False) -> pd.DataFrame:
        """Fetch the training labels used for this model analysis."""
        if fetch_subsample:
            return self._get_data_from_run(
                file_name=ModelAnalysisFileNames.TRAIN_Y_PRED_SUBSAMPLE)
        return self._get_data_from_run(
            file_name=ModelAnalysisFileNames.TRAIN_Y_PRED)

    def get_test_data(self, fetch_subsample: bool = False) -> pd.DataFrame:
        """Fetch the test data used for this model analysis."""
        if fetch_subsample:
            return self._get_data_from_run(
                file_name=ModelAnalysisFileNames.TEST_DATA_SUBSAMPLE)
        return self._get_data_from_snapshot(
            file_name=ModelAnalysisFileNames.TEST_DATA,
            datastore_prefix=self.settings.datastore_prefix,
            snapshot_id=self.settings.test_snapshot_id)

    def get_test_labels(self, fetch_subsample: bool = False) -> pd.DataFrame:
        """Fetch the test labels used for this model analysis."""
        if fetch_subsample:
            return self._get_data_from_run(
                file_name=ModelAnalysisFileNames.TEST_Y_PRED_SUBSAMPLE)
        return self._get_data_from_run(
            file_name=ModelAnalysisFileNames.TEST_Y_PRED)

    def get_train_subsample_indices(self) -> List:
        """Fetch the subsample indices of the train data."""
        return self._get_data_from_run(
            file_name=ModelAnalysisFileNames.SUBSAMPLE_INDICES_TRAIN)[0]

    def get_test_subsample_indices(self) -> List:
        """Fetch the subsample indices of the test data."""
        return self._get_data_from_run(
            file_name=ModelAnalysisFileNames.SUBSAMPLE_INDICES_TEST)[0]

    def _get_data_types(self) -> Dict:
        """Fetch the data types for the data."""
        return self._get_data_from_run(
            file_name=ModelAnalysisFileNames.DATA_TYPES)

    def _get_data_from_snapshot(self, file_name: str,
                                datastore_prefix: Optional[str],
                                snapshot_id: str) -> pd.DataFrame:
        if datastore_prefix is not None:
            prefix = '{}/{}'.format(datastore_prefix, snapshot_id)
        else:
            prefix = snapshot_id
        # if a user already called download, see if we can reuse that, else download
        if self._output_directory:
            data_path = os.path.join(os.getcwd(), self._output_directory, prefix, file_name)
            if os.path.isfile(data_path):
                return ModelAnalysisRun._read_file(data_path)
        with TemporaryDirectory() as td:
            self.datastore.download(target_path=td, prefix=prefix)
            path = os.path.join(td, prefix, file_name)
            return ModelAnalysisRun._read_file(path)

    def _get_data_from_run(self, file_name):
        if self._output_directory:
            data_path = os.path.join(os.getcwd(), self._output_directory, file_name)
            if os.path.isfile(data_path):
                return ModelAnalysisRun._read_file(data_path)
        with TemporaryDirectory() as td:
            if os.path.split(file_name)[0] == ModelAnalysisFileNames.DATA_PREFIX:
                temp_data_path = os.path.join(td, ModelAnalysisFileNames.DATA_PREFIX)
                os.makedirs(temp_data_path)
            else:
                temp_data_path = td
            self.download_file(name=file_name, output_file_path=temp_data_path)
            path = os.path.join(td, file_name)
            return ModelAnalysisRun._read_file(path)

    @staticmethod
    def _read_file(data_path: str):
        if data_path.endswith("json"):
            with open(data_path, "r") as file:
                return pd.DataFrame(json.load(file))
        elif data_path.endswith('parquet'):
            return pq.read_table(data_path).to_pandas()
        else:
            with open(data_path, "rb") as data_file:
                return pkl.load(data_file)
