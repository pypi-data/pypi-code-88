from typing import Dict, List

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_squared_error,
    mean_squared_log_error,
    median_absolute_error,
    roc_auc_score,
    top_k_accuracy_score,
)
from sklearn.preprocessing import OneHotEncoder
from torch import nn

REGR_LOSS: List[callable] = [nn.SmoothL1Loss, nn.MSELoss, nn.L1Loss]
CLASS_LOSS: List[callable] = [
    nn.CrossEntropyLoss,
    nn.KLDivLoss,
    nn.BCEWithLogitsLoss,
    nn.MSELoss,
    nn.L1Loss,
]
REGR_METRIC: List[callable] = []
CLASS_METRIC: List[callable] = []


def register(plugin):
    def wrapper_register(func):
        plugin.append(func)
        return func

    return wrapper_register


@register(CLASS_METRIC)
def roc_auc(y_true, y_pred_prob):
    """Area Under the Receiver Operating Characteristic Curve (ROC AUC)

    `y_pred_prob` must be prediction probabilities.
    'weighted': Calculate metrics for each label, and find their average weighted by support
    (the number of true instances for each label)
    """
    categories = [list(range(y_pred_prob.shape[1]))]
    return roc_auc_score(encoding_onehot(y_true, categories), y_pred_prob, average="weighted")


@register(CLASS_METRIC)
def f1(y_true, y_pred):
    """weighted average of f1:

    Calculate metrics for each label, and find their average weighted by support
    (the number of true instances for each label)
    """
    return f1_score(y_true, logits_to_labels(y_pred), average="weighted")


# TODO: do we also want a precision for each class?
@register(CLASS_METRIC)
def tpr(y_true, y_pred):
    """True positive rate for each class/label"""
    m = confusion_matrix(y_true, logits_to_labels(y_pred))
    return np.diag(m) / m.sum(axis=0)


@register(CLASS_METRIC)
def balanced_accuracy(y_true, y_pred):
    """average recalls (TPR) from each class"""
    return balanced_accuracy_score(y_true, logits_to_labels(y_pred))


# TODO: decide whether to deprecate this
@register(CLASS_METRIC)
def accuracy(y_true, y_pred):
    # y_true: sparse encoding
    # y_pred: sparse encoding of logits
    return accuracy_score(y_true, logits_to_labels(y_pred))


@register(CLASS_METRIC)
def top_k(y_true, y_pred, k=2):
    # y_true: sparse encoding
    # y_pred: n-class logits
    return top_k_accuracy_score(y_true, y_pred, k=k)


# TODO: how to make a generic pre-processing?
def encoding_onehot(targets, categories):
    onehot_encoder = OneHotEncoder(sparse=False, categories=categories)
    return onehot_encoder.fit_transform(targets.reshape(-1, 1))


def logits_to_labels(predictions):
    return np.argmax(predictions, axis=1)


@register(REGR_LOSS)
def RootMeanSquaredError(y_true, y_pred):
    return mean_squared_error(y_true, y_pred, squared=False)


@register(REGR_LOSS)
def MeanAbsoluteError(y_true, y_pred):
    return mean_absolute_error(y_true, y_pred)


@register(REGR_LOSS)
def MeanSquqredLogError(y_true, y_pred):
    return mean_squared_log_error(y_true, y_pred)


@register(REGR_LOSS)
def MedianAbsoluteError(y_true, y_pred):
    return median_absolute_error(y_true, y_pred)


@register(REGR_LOSS)
def MeanAbsolutePerError(y_true, y_pred):
    return mean_absolute_percentage_error(y_true, y_pred)
