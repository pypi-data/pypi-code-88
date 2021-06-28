import os
import joblib
import tempfile
import shutil
import numpy as np
import time
import math
from typing import Union

from snitch_ai.internal.guid import GUID
from snitch_ai.internal.api_client import ApiClient
from snitch_ai.internal.quality_analysis import QualityAnalysis
from snitch_ai.internal.drift_analysis import DriftAnalysis
from snitch_ai.internal.analysis_status import AnalysisState


def _save_tf_model(model, path):
    path += ".h5"
    model.save(path, save_format="h5")
    return path


def _save_sklearn_model(model, path):
    path += ".joblib"
    joblib.dump(model, path)
    return path


def _save_xgboost_model(model, path):
    path += ".json"
    model.save_model(path)
    return path


def _save_model_to_path(model, path):
    model_type = str(type(model))

    if "tensorflow." in model_type:
        return _save_tf_model(model, path)

    if "sklearn." in model_type:
        return _save_sklearn_model(model, path)

    if "xgboost." in model_type:
        return _save_xgboost_model(model, path)

    raise Exception(f"Unsupported model type: {model_type}")


def _save_dataset_to_path(dataset, path):
    path += ".npz"
    np.savez_compressed(path, dataset)
    return path


def _upload_quality_analysis_file(project_id, version_id, client, file_name, file_path):
    with open(file_path, "rb") as f:
        resp = client.patch(f"project/{project_id}/version/{version_id}", files={file_name: f})
        if resp.status_code != 200:
            raise Exception(f"Error uploading file: {resp.text}")


def _upload_drift_analysis_file(project_id, version_id, drift_id, client, file_name, file_path):
    with open(file_path, "rb") as f:
        resp = client.patch(f"project/{project_id}/version/{version_id}/drift/{drift_id}", files={file_name: f})
        if resp.status_code != 200:
            raise Exception(f"Error uploading file: {resp.text}")


def _wait_on_analysis_completion(analysis: Union[QualityAnalysis, DriftAnalysis]):
    # wait for analysis to complete
    count = 1
    waiting_on_completion = True
    while waiting_on_completion:
        # wait for 2, 4, 8, 16, 32, 32, 32, ... seconds before re-checking
        delay = math.pow(2, min(count, 5))
        count += 1
        time.sleep(delay)

        status = analysis.get_status()

        if status.state == AnalysisState.COMPLETED:
            waiting_on_completion = False
        elif status.state == AnalysisState.ERROR:
            raise Exception(f"The analysis failed due to an error: {status.error}")
        elif status.state == AnalysisState.UNKNOWN:
            raise Exception("Error while waiting on analysis: analysis hasn't been started yet.")


class ProjectVersion:

    def __init__(self, project_id: GUID, version_id: GUID, name: str):
        self.project_id = project_id
        self.version_id = version_id
        self.name = name


    def run_quality_analysis(self, model, train_x, train_y, test_x, test_y) -> QualityAnalysis:
        """
        Runs a Quality analysis using the specified parameters.
        :param model: The model file. Supported types are Tensorflow, SciKit-Learn and XGBoost.
        :param train_x: The training feature dataset in array format.
        :param train_y: The training target dataset in array format.
        :param test_x: The testing feature dataset in array format.
        :param test_y: The testing target dataset in array format.
        :return: A QualityAnalysis object that can be used to obtain status information as well as results of the Quality analysis.
        """
        client = ApiClient()

        # upload files
        temp_dir = tempfile.mkdtemp(prefix="snitch_ai_")
        try:
            if not model is None:
                path = _save_model_to_path(model, os.path.join(temp_dir, "model"))
                _upload_quality_analysis_file(self.project_id, self.version_id, client, "model", path)

            if not train_x is None:
                path = _save_dataset_to_path(train_x, os.path.join(temp_dir, "train_x"))
                _upload_quality_analysis_file(self.project_id, self.version_id, client, "train_x", path)

            if not train_y is None:
                path = _save_dataset_to_path(train_y, os.path.join(temp_dir, "train_y"))
                _upload_quality_analysis_file(self.project_id, self.version_id, client, "train_y", path)

            if not test_x is None:
                path = _save_dataset_to_path(test_x, os.path.join(temp_dir, "test_x"))
                _upload_quality_analysis_file(self.project_id, self.version_id, client, "test_x", path)

            if not test_y is None:
                path = _save_dataset_to_path(test_y, os.path.join(temp_dir, "test_y"))
                _upload_quality_analysis_file(self.project_id, self.version_id, client, "test_y", path)
        finally:
            shutil.rmtree(temp_dir)

        # start analysis
        resp = client.post(f"project/{self.project_id}/version/{self.version_id}/quality/start")
        if resp.status_code != 200:
            raise Exception(f"Error starting quality analysis: {resp.text}")

        quality_analysis = QualityAnalysis(self.project_id, self.version_id)
        _wait_on_analysis_completion(quality_analysis)

        return quality_analysis


    def run_drift_analysis(self, train_x, updated_x) -> DriftAnalysis:
        """
        Runs a Drift analysis using the specified parameters.
        :param train_x: The training feature dataset in array format.
        :param updated_x: The updated feature dataset in array format.
        :return: A DriftAnalysis object that can be used to obtain status information as well as results of the Drift analysis.
        """
        client = ApiClient()

        # create drift analysis
        resp = client.post(f"/project/{self.project_id}/version/{self.version_id}/drift")
        if resp.status_code != 201:
            raise Exception(f"Error creating drift analysis: {resp.text}")

        drift_obj = resp.json()
        drift_id = drift_obj["id"];

        # upload files
        temp_dir = tempfile.mkdtemp(prefix="snitch_ai_")
        try:
            if not train_x is None:
                path = _save_dataset_to_path(train_x, os.path.join(temp_dir, "train_x"))
                _upload_drift_analysis_file(self.project_id, self.version_id, drift_id, client, "train_x", path)

            if not updated_x is None:
                path = _save_dataset_to_path(updated_x, os.path.join(temp_dir, "updated_x"))
                _upload_drift_analysis_file(self.project_id, self.version_id, drift_id, client, "updated_x", path)
        finally:
            shutil.rmtree(temp_dir)

        # start analysis
        resp = client.post(f"project/{self.project_id}/version/{self.version_id}/drift/{drift_id}/start")
        if resp.status_code != 200:
            raise Exception(f"Error starting drift analysis: {resp.text}")

        drift_analysis = DriftAnalysis(self.project_id, self.version_id, GUID(drift_id))
        _wait_on_analysis_completion(drift_analysis)

        return drift_analysis


    def __str__(self):
        return f"Project Version {self.version_id}: {self.name}"
