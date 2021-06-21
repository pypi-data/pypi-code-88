# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import argparse
import joblib
import json
import logging
import os
import numpy as np
import pandas as pd
import pickle as pkl
import random
from tempfile import TemporaryDirectory
from typing import Any, Dict, List, Optional, Tuple

from azureml._common._error_definition import AzureMLError
from azureml.core import Dataset, Datastore, Model, Run, Workspace
from azureml.exceptions import AzureMLException

from azureml.responsibleai.common._errors.error_definitions import (
    DatasetTooLargeError,
    UnexpectedObjectType
)
from azureml.responsibleai.tools.model_analysis._constants import (
    AnalysisTypes,
    ModelAnalysisFileNames,
    PropertyKeys,
    SUBSAMPLE_SIZE
)
from azureml.responsibleai.tools.model_analysis._aml_init_dto import AMLInitDTO

_logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


def _parse_command_line():
    parser = argparse.ArgumentParser()

    parser.add_argument('--settings_filepath', type=str, required=True,
                        help="Path to the pickled settings")

    return parser.parse_args()


def _check_dataframe_size(df: pd.DataFrame,
                          maximum_size: int,
                          dataset_name: str,
                          arg_name: str):
    if len(df.index) > maximum_size:
        raise AzureMLException._with_error(
            AzureMLError.create(
                DatasetTooLargeError,
                dataset_name=dataset_name,
                actual_count=len(df.index),
                limit_count=maximum_size,
                length_arg_name=arg_name)
        )


def load_dataset(ws: Workspace, dataset_id, snapshot_id) -> pd.DataFrame:
    """Snapshot the dataset if needed and return DataFrame."""
    _logger.info("Checking for snapshot {0} of dataset {1}".format(
        snapshot_id, dataset_id))

    ds = Dataset.get_by_id(workspace=ws, id=dataset_id)

    return ds.to_pandas_dataframe()


def load_mlflow_model(workspace: Workspace, model_id: str) -> Any:
    # Only import mlflow if we were given mlflow param as user might not have added this to RC
    # Ultimately we should run on our own envs which we control
    import mlflow
    mlflow.set_tracking_uri(workspace.get_mlflow_tracking_uri())

    model = Model._get(workspace, id=model_id)
    model_uri = "models:/{}/{}".format(model.name, model.version)
    return mlflow.pyfunc.load_model(model_uri)


def take_subsamples(data: pd.DataFrame,
                    labels: np.ndarray) -> Tuple[pd.DataFrame, pd.DataFrame, List]:
    """This is a naive implementation, it should be replaced with a better implementation."""
    length = data.shape[0]
    indices = list(range(length))
    if SUBSAMPLE_SIZE < length:
        _logger.info("The data contains {} samples which is less than the subsample size {}, "
                     "skipping subsampling.".format(length, SUBSAMPLE_SIZE))
        sample_indices = random.sample(indices, SUBSAMPLE_SIZE)
        sample_indices.sort()
        data_subsample = data.take(sample_indices)
        label_subsample = labels.take(sample_indices)
        data_subsample = data_subsample.reset_index().drop(columns='index')
    else:
        sample_indices = indices
        data_subsample = data
        label_subsample = labels

    return (
        data_subsample,
        label_subsample,
        sample_indices)


def _save_df(
        df: pd.DataFrame,
        dir: str,
        datastore_prefix: Optional[str],
        snapshot_id: str,
        filename: str) -> str:
    if datastore_prefix is None:
        local_path = os.path.join(dir, snapshot_id, filename)
    else:
        local_path = os.path.join(dir, datastore_prefix, snapshot_id, filename)
    common_path = os.path.dirname(local_path)
    if not os.path.exists(common_path):
        os.makedirs(common_path)
    if filename.endswith("json"):
        with open(local_path, "w+") as json_file:
            # Pandas df.to_json does not maintain more than 15 digits of precision
            json.dump(df.to_dict(orient='records'), json_file)
    else:
        df.to_parquet(local_path)
    return local_path


def upload_to_datastore(settings: AMLInitDTO,
                        workspace: Workspace,
                        train_data: pd.DataFrame,
                        test_data: pd.DataFrame) -> None:
    datastore = Datastore.get(workspace, settings.confidential_datastore_name)
    with TemporaryDirectory() as td:
        file_names = [
            _save_df(train_data, td, settings.datastore_prefix,
                     settings.train_snapshot_id, ModelAnalysisFileNames.TRAIN_DATA),
            _save_df(test_data, td, settings.datastore_prefix,
                     settings.test_snapshot_id, ModelAnalysisFileNames.TEST_DATA),
        ]
        datastore.upload_files(files=file_names, relative_root=td)


def upload_to_run(
        run: Run,
        datastore_name: str,
        settings: AMLInitDTO,
        y_pred_train: np.ndarray,
        y_pred_test: np.ndarray,
        train_data_subsample: pd.DataFrame,
        test_data_subsample: pd.DataFrame,
        y_pred_train_subsample: np.ndarray,
        y_pred_test_subsample: np.ndarray,
        subsample_indices_train: list,
        subsample_indices_test: list,
        data_types: Dict) -> None:
    with TemporaryDirectory() as td:
        settings_path = os.path.join(td, ModelAnalysisFileNames.SETTINGS)
        with open(settings_path, 'wb+') as settings_file:
            pkl.dump(settings, settings_file)

        dtypes_path = os.path.join(td, ModelAnalysisFileNames.DATA_TYPES)
        with open(dtypes_path, 'wb+') as dtypes_file:
            pkl.dump(dict(data_types), dtypes_file)

        subsample_indices_train_path = os.path.join(
            td, ModelAnalysisFileNames.SUBSAMPLE_INDICES_TRAIN)
        common_path = os.path.dirname(subsample_indices_train_path)
        if not os.path.exists(common_path):
            os.makedirs(common_path)
        with open(subsample_indices_train_path, 'w+') as subsample_train_file:
            json.dump(subsample_indices_train, subsample_train_file)

        subsample_indices_test_path = os.path.join(
            td, ModelAnalysisFileNames.SUBSAMPLE_INDICES_TEST)
        with open(subsample_indices_test_path, 'w+') as subsample_test_file:
            json.dump(subsample_indices_test, subsample_test_file)

        names = [
            ModelAnalysisFileNames.SETTINGS,
            ModelAnalysisFileNames.DATA_TYPES,
            ModelAnalysisFileNames.TRAIN_Y_PRED,
            ModelAnalysisFileNames.TEST_Y_PRED] + ModelAnalysisFileNames.ALL_SUBSAMPLES
        file_paths = [
            settings_path,
            dtypes_path,
            _save_df(pd.DataFrame(y_pred_train, columns=[settings.target_column_name]), td,
                     settings.datastore_prefix, settings.train_snapshot_id,
                     ModelAnalysisFileNames.TRAIN_Y_PRED),
            _save_df(pd.DataFrame(y_pred_test, columns=[settings.target_column_name]), td,
                     settings.datastore_prefix, settings.test_snapshot_id,
                     ModelAnalysisFileNames.TEST_Y_PRED),
            _save_df(train_data_subsample, td, settings.datastore_prefix, settings.train_snapshot_id,
                     ModelAnalysisFileNames.TRAIN_DATA_SUBSAMPLE),
            _save_df(pd.DataFrame(y_pred_train_subsample, columns=[settings.target_column_name]), td,
                     settings.datastore_prefix, settings.train_snapshot_id,
                     ModelAnalysisFileNames.TRAIN_Y_PRED_SUBSAMPLE),
            _save_df(test_data_subsample, td, settings.datastore_prefix, settings.test_snapshot_id,
                     ModelAnalysisFileNames.TEST_DATA_SUBSAMPLE),
            _save_df(pd.DataFrame(y_pred_test_subsample, columns=[settings.target_column_name]), td,
                     settings.datastore_prefix, settings.test_snapshot_id,
                     ModelAnalysisFileNames.TEST_Y_PRED_SUBSAMPLE),
            subsample_indices_train_path,
            subsample_indices_test_path
        ]

        # TODO error check the response
        run.upload_files(
            names=names,
            paths=file_paths,
            return_artifacts=True,
            timeout_seconds=1200,
            datastore_name=datastore_name)


def create_analysis_asset(run: Run,
                          estimator,
                          train_data: pd.DataFrame,
                          test_data: pd.DataFrame,
                          settings: AMLInitDTO):
    _logger.info("Generating predictions")
    y_pred_train = estimator.predict(train_data[settings.X_column_names])
    y_pred_test = estimator.predict(test_data[settings.X_column_names])
    train_data_subsample, y_pred_train_subsample, sample_indices_train = \
        take_subsamples(data=train_data,
                        labels=y_pred_train)
    test_data_subsample, y_pred_test_subsample, sample_indices_test = \
        take_subsamples(data=test_data,
                        labels=y_pred_test)

    upload_to_datastore(
        settings,
        run.experiment.workspace,
        train_data,
        test_data)
    upload_to_run(
        run=run,
        datastore_name=settings.confidential_datastore_name,
        settings=settings,
        y_pred_train=y_pred_train,
        y_pred_test=y_pred_test,
        train_data_subsample=train_data_subsample,
        test_data_subsample=test_data_subsample,
        y_pred_train_subsample=y_pred_train_subsample,
        y_pred_test_subsample=y_pred_test_subsample,
        subsample_indices_train=sample_indices_train,
        subsample_indices_test=sample_indices_test,
        data_types=train_data.dtypes)


def init_wrapper():
    args = _parse_command_line()

    settings: AMLInitDTO = joblib.load(args.settings_filepath)
    if not isinstance(settings, AMLInitDTO):
        raise AzureMLException._with_error(
            AzureMLError.create(
                UnexpectedObjectType,
                expected='AMLInitDTO',
                actual=str(type(settings))
            )
        )

    _logger.info("Model analysis ID: {0}".format(settings.analysis_id))

    my_run = Run.get_context()
    my_run.add_properties({PropertyKeys.ANALYSIS_ID: settings.analysis_id,
                           PropertyKeys.MODEL_ID: settings.model_id,
                           PropertyKeys.TRAIN_SNAPSHOT_ID: settings.train_snapshot_id,
                           PropertyKeys.TEST_SNAPSHOT_ID: settings.test_snapshot_id,
                           PropertyKeys.ANALYSIS_TYPE: AnalysisTypes.MODEL_ANALYSIS_TYPE})

    _logger.info("Dealing with initialization dataset")
    train_df = load_dataset(my_run.experiment.workspace,
                            settings.train_dataset_id,
                            settings.train_snapshot_id)

    _logger.info("Dealing with evaluation dataset")
    test_df = load_dataset(my_run.experiment.workspace,
                           settings.test_dataset_id,
                           settings.test_snapshot_id)
    _check_dataframe_size(test_df,
                          settings.maximum_rows_for_test_dataset,
                          'test',
                          'maximum_rows_for_test_dataset')

    _logger.info("Loading model")
    if settings.model_loader == "mlflow":
        model_estimator = load_mlflow_model(
            workspace=my_run.experiment.workspace,
            model_id=settings.model_id)
    else:
        model_estimator = settings.model_loader.load_by_model_id(workspace=my_run.experiment.workspace,
                                                                 model_id=settings.model_id)

    create_analysis_asset(my_run, model_estimator, train_df, test_df, settings)
