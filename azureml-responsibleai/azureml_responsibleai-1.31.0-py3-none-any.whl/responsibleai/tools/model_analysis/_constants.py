# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Common constants for model analysis."""

import os

DEFAULT_MAXIMUM_ROWS_FOR_TEST_DATASET = 5000
SUBSAMPLE_SIZE = DEFAULT_MAXIMUM_ROWS_FOR_TEST_DATASET


class AzureMLTypes:
    """Strings for AzureML types (Runs and Assets)."""

    MODEL_ANALYSIS = 'azureml.modelanalysis'


class AnalysisTypes:
    """Strings to identify explanations, causal etc."""

    EXPLANATION_TYPE = 'Explanation'
    MODEL_ANALYSIS_TYPE = 'ModelAnalysis'


class PropertyKeys:
    """Keys for properties."""
    _PROPERTY_PREFIX = "azureml."
    ANALYSIS_ID = _PROPERTY_PREFIX + 'AnalysisId'
    ANALYSIS_TYPE = _PROPERTY_PREFIX + 'AnalysisType'
    MODEL_ID = _PROPERTY_PREFIX + 'ModelId'
    TRAIN_SNAPSHOT_ID = _PROPERTY_PREFIX + "TrainSnapshotId"
    TEST_SNAPSHOT_ID = _PROPERTY_PREFIX + "TestSnapshotId"
    VERSION = _PROPERTY_PREFIX + 'VersionForModelAnalysis'

    EXPLANATION_POINTER_FORMAT = _PROPERTY_PREFIX + 'explanation_{0}'


class ExplanationVersion:
    """Supported versions on the explanation Assets.

    This goes with the VERSION = 'versionForModelAnalysis' key
    """
    V_0 = 0


class ModelAnalysisFileNames:
    """Constants for data files in model analysis runs."""
    DATA_PREFIX = "data"
    TRAIN_DATA = os.path.join(DATA_PREFIX, "train_data.parquet")
    TRAIN_Y_PRED = os.path.join(DATA_PREFIX, "train_y_pred.parquet")
    TEST_DATA = os.path.join(DATA_PREFIX, "test_data.parquet")
    TEST_Y_PRED = os.path.join(DATA_PREFIX, "test_y_pred.parquet")
    ALL_DATA = [TRAIN_DATA, TRAIN_Y_PRED, TEST_DATA, TEST_Y_PRED]

    TRAIN_DATA_SUBSAMPLE = os.path.join(
        DATA_PREFIX, "train_data_subsample.json")
    TRAIN_Y_PRED_SUBSAMPLE = os.path.join(
        DATA_PREFIX, "train_y_pred_subsample.json")
    TEST_DATA_SUBSAMPLE = os.path.join(DATA_PREFIX, "test_data_subsample.json")
    TEST_Y_PRED_SUBSAMPLE = os.path.join(
        DATA_PREFIX, "test_y_pred_subsample.json")
    SUBSAMPLE_INDICES_TRAIN = os.path.join(
        DATA_PREFIX, "subsample_indices_train.json")
    SUBSAMPLE_INDICES_TEST = os.path.join(
        DATA_PREFIX, "subsample_indices_test.json")
    ALL_SUBSAMPLES = [
        TRAIN_DATA_SUBSAMPLE,
        TRAIN_Y_PRED_SUBSAMPLE,
        TEST_DATA_SUBSAMPLE,
        TEST_Y_PRED_SUBSAMPLE,
        SUBSAMPLE_INDICES_TRAIN,
        SUBSAMPLE_INDICES_TEST]

    SETTINGS = "settings.pkl"
    DATA_TYPES = "datatypes.pkl"
