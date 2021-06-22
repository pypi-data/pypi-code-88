# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Any, List, Optional

import numpy as np
import pandas as pd

from .types import DataFrameLike


class RawExperimentData:
    """
    A data structure that combines all the pieces of a Dataset required to perform a Machine Learning experiment, such
    as training data (on which the model trains on), validation data (on which we evaluate the model predictability),
    weights data) that each sample from the training data is to be assigned) etc.

    All different possibilities of inputs converge to this class, which presents a unified interface for the
    underlying clients to use, which means that the clients of this class should not care which way the inputs
    were provided to it (e.g. get data script, X + y + w, training_data, validation_data, etc.)

    Note that this class is only the convergence point of all different formats that we support in AutoML. It does not
    ensure that the underlying data is valid, i.e. it is a pre-validation concept.
    """

    def __init__(
        self,
        X: pd.DataFrame,
        y: np.ndarray,
        weights: Optional[np.ndarray] = None,
        X_valid: pd.DataFrame = None,
        y_valid: Optional[np.ndarray] = None,
        weights_valid: Optional[np.ndarray] = None,
        training_data: Optional[DataFrameLike] = None,
        validation_data: Optional[DataFrameLike] = None,
        target_column_name: Optional[str] = None,
        feature_column_names: Optional[np.ndarray] = None,
        weight_column_name: Optional[str] = None,
        validation_size: float = 0,
        cv_splits_indices: Optional[List[List[Any]]] = None,
        n_cross_validations: Optional[int] = None,
    ):
        """
        Initialize a RawExperimentData.

        :param X: The features (or columns) to train the model on.
        :param y: The target column (e.g., labels) to predict.
        :param weights: An optional column representing the weight to be assigned to each sample in X.
        :param X_valid: A validation dataset with the same schema as X.
        :param y_valid: The target column for the data in X_valid.
        :param weights_valid: Weights for the samples in X_valid.
        :param training_data: Optional reference to the complete underlying training dataset on the backing store.
        :param validation_data: An optional validation dataset with the same schema as training_data.
        :param target_column_name: Name of the column to predict. Note that this can be empty when X is a numpy array.
        :param feature_column_names: The names of columns in X or training_data on which to train the model on.
        :param weight_column_name: Column name representing the weights to be assigned to each sample in train data.
        :param validation_size: Fraction of the data to hold out as validation data during model selection.
        :param cv_splits_indices: Optional list of indices in X to use for various cross folds during model selection.
        """
        # data
        self.X, self.y, self.weights = X, y, weights
        self.X_valid, self.y_valid, self.weights_valid = X_valid, y_valid, weights_valid
        self.training_data, self.validation_data = training_data, validation_data

        # metadata & configuration
        self.target_column_name = target_column_name
        self.feature_column_names = feature_column_names
        self.weight_column_name = weight_column_name
        self.validation_size = validation_size
        self.cv_splits_indices = cv_splits_indices
        self.n_cross_validations = n_cross_validations
