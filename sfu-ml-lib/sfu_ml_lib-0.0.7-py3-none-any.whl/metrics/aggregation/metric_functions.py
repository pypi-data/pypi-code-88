from typing import Optional

import numpy as np
import sklearn.metrics as sk_metrics
from scipy import special as sp_scipy
from scipy import stats as sp_stats

from sfu_ml_lib.base.metrics import NumericType, AggregatorType


def logits_to_probabilities_multiclass(logits: np.ndarray) -> np.ndarray:
    return sp_scipy.softmax(logits, axis=-1)


def logits_to_probabilities_multilabel(logits: np.ndarray) -> np.ndarray:
    return sp_scipy.expit(logits, axis=-1)


def logits_to_predictions_multiclass(logits: np.ndarray) -> np.ndarray:
    return np.argmax(logits, axis=-1)


def logits_to_predictions_multilabel(logits: np.ndarray, dtype: np.dtype = np.float32) -> np.ndarray:
    return (logits_to_probabilities_multilabel(logits) > 0.5).astype(dtype)


def cross_entropy_multiclass(targets: np.ndarray, logits: np.ndarray, epsilon=1e-12) -> NumericType:
    probabilities = logits_to_probabilities_multiclass(logits)

    probabilities_clipped = np.clip(probabilities, epsilon, 1. - epsilon)

    nonzero = probabilities_clipped[np.arange(targets.size, dtype=np.int32), targets]

    score = -mean(np.log(nonzero))

    return score


def cross_entropy_multilabel(targets: np.ndarray, logits: np.ndarray, epsilon=1e-12) -> NumericType:
    probabilities = logits_to_probabilities_multilabel(logits)

    probabilities_clipped = np.clip(probabilities, epsilon, 1. - epsilon)

    scores = -targets * np.log(probabilities_clipped) - (1 - targets) * np.log(1 - probabilities_clipped)

    score = -np.mean(np.sum(scores, axis=-1))

    return score


def mean_absolute_error(targets: np.ndarray, predictions: np.ndarray) -> NumericType:
    return float(np.mean(np.abs(targets - predictions)))


def mean_squared_error(targets: np.ndarray, predictions: np.ndarray) -> NumericType:
    return float(np.mean(np.square(targets - predictions)))


def pearson_correlation(targets: np.ndarray, predictions: np.ndarray) -> NumericType:
    correlation, p_value = sp_stats.pearsonr(targets, predictions)

    return correlation


def accuracy(targets: np.ndarray, predictions: np.ndarray) -> NumericType:
    return sk_metrics.accuracy_score(targets, predictions)


def precision(targets: np.ndarray, predictions: np.ndarray, average: Optional[str] = 'weighted') -> NumericType:
    return sk_metrics.precision_score(targets, predictions, average=average, zero_division=0)


def recall(targets: np.ndarray, predictions: np.ndarray, average: Optional[str] = 'weighted') -> NumericType:
    return sk_metrics.recall_score(targets, predictions, average=average, zero_division=0)


def f1_score(targets: np.ndarray, predictions: np.ndarray, average: Optional[str] = 'weighted') -> NumericType:
    return sk_metrics.f1_score(targets, predictions, average=average, zero_division=0)


def jaccard_score(targets: np.ndarray, predictions: np.ndarray, average: Optional[str] = 'weighted') -> NumericType:
    return sk_metrics.jaccard_score(targets, predictions, average=average)


def jaccard_score_multilabel(targets: np.ndarray, predictions: np.ndarray) -> NumericType:
    overlap = np.sum(targets * predictions, axis=1)

    union = np.sum(targets + predictions > 0, axis=1)

    score = float(np.mean(np.divide(overlap, union, out=np.zeros_like(union, dtype=np.float32), where=union != 0)))

    return score


def mean(array: np.ndarray) -> NumericType:
    return float(np.mean(array))


def calculate_thresholds(targets: np.ndarray, probabilities: np.ndarray) -> np.array:
    num_classes = targets.shape[1]

    best_thresholds = np.empty(shape=num_classes, dtype=np.float32)

    for index in range(num_classes):
        precisions, recalls, thresholds = sk_metrics.precision_recall_curve(
            y_true=targets[:, index],
            probas_pred=probabilities[:, index],
        )

        f1_scores_denominator = precisions + recalls
        f1_scores = np.divide(
            2 * precisions * recalls,
            f1_scores_denominator,
            out=np.zeros_like(f1_scores_denominator),
            where=f1_scores_denominator != 0,
        )

        best_thresholds[index] = thresholds[np.nanargmax(f1_scores) - 1]

    return best_thresholds


def calculate_with_optimized_predictions(
        targets: np.ndarray,
        probabilities: np.ndarray,
        function: AggregatorType,
) -> NumericType:

    thresholds = calculate_thresholds(targets, probabilities)

    predictions = probabilities >= thresholds

    score = function(targets, predictions.astype(np.float32))

    return score
