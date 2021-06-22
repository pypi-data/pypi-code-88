# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
"""Methods specific to a Classification task type."""

from typing import Any, Dict, List, Optional, Union

import numpy as np
from sklearn.base import TransformerMixin

from azureml.automl.runtime.shared.score import scoring


def evaluate_classifier(
        y_test: np.ndarray,
        y_pred_probs: np.ndarray,
        metrics: List[str],
        class_labels: np.ndarray,
        train_labels: np.ndarray,
        sample_weight: Optional[np.ndarray] = None,
        y_transformer: Optional[TransformerMixin] = None,
        use_binary: bool = False,
) -> Dict[str, Union[float, Dict[str, Any]]]:
    """
    Given the scored data, generate metrics for classification task

    All class labels for y should come as seen by the fitted model (i.e. if the fitted model uses a
    y transformer the labels should also come transformed).

    All metrics present in `metrics` will be present in the output dictionary with either
    the value(s) calculated or `nan` if the calculation failed.

    :param y_test: The target values (Transformed if using a y transformer)
    :param y_pred_probs: The predicted probabilities for all classes.
    :param metrics: Classification metrics to compute
    :param class_labels: All classes found in the full dataset (includes train/valid/test sets).
        These should be transformed if using a y transformer.
    :param train_labels: Classes as seen (trained on) by the trained model. These values
        should correspond to the columns of y_pred_probs in the correct order.
    :param sample_weight: Weights for the samples (Does not need
        to match sample weights on the fitted model)
    :param y_transformer: Used to inverse transform labels from `y_test`. Required for non-scalar metrics.
    :param use_binary: Compute metrics only on the true class for binary classification.
    :return: A dictionary mapping metric name to metric score.
    """
    return scoring.score_classification(
        y_test, y_pred_probs, metrics, class_labels, train_labels, sample_weight, y_transformer, use_binary
    )
