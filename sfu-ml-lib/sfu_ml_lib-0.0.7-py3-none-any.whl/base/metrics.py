from enum import Enum
from typing import Mapping, Union, MutableMapping, Callable

import numpy as np
import tensorflow as tf


NumericType = Union[int, float]
PrimitiveType = Union[int, float, str, bool]
AggregatorType = Callable[..., NumericType]
MetricKeyType = Union[str, 'Metric']
MetricValueType = Union[NumericType, np.ndarray, tf.Tensor]


TRAIN_PREFIX = 'Training'
VALIDATION_PREFIX = 'Validation'
TEST_PREFIX = 'Test'


class Metric(Enum):
    LOSS = 'Loss'

    ACCURACY = 'Accuracy'
    ROC_AUC = 'ROC AUC'
    PREDICTION_BIAS = 'Prediction Bias'
    CUTOFF_THRESHOLD = 'Cutoff Threshold'

    COSINE_SIMILARITY = 'Cosine Similarity'
    COSINE_DISTANCE = 'Cosine Distance'
    JACCARD_SCORE = 'Jaccard Score'
    CROSS_ENTROPY = 'Cross Entropy'
    MUTUAL_INFORMATION = 'Mutual Information'
    REWARD = 'Reward'

    NOISE_CONTRASTIVE_ESTIMATION = 'Noise Contrastive Estimation'
    NORMALIZED_TEMPERATURE_SCALED_CROSS_ENTROPY = 'Normalized Temperature-Scaled Cross Entropy'

    MEAN_ABSOLUTE_ERROR = 'Mean Absolute Error'
    MEAN_SQUARE_ERROR = 'Mean Square Error'
    PEARSON_CORRELATION = 'Pearson Correlation'

    WEIGHTED_F1 = 'Weighted F1 Score'
    WEIGHTED_PRECISION = 'Weighted Precision'
    WEIGHTED_RECALL = 'Weighted Recall'

    MICRO_F1 = 'Micro F1 Score'
    MICRO_PRECISION = 'Micro Precision'
    MICRO_RECALL = 'Micro Recall'

    MACRO_F1 = 'Macro F1 Score'
    MACRO_PRECISION = 'Macro Precision'
    MACRO_RECALL = 'Macro Recall'

    @property
    def train_value(self) -> str:
        return f'{TRAIN_PREFIX} {self.value}'

    @property
    def validation_value(self) -> str:
        return f'{VALIDATION_PREFIX} {self.value}'

    @property
    def test_value(self) -> str:
        return f'{TEST_PREFIX} {self.value}'


def prefix_metrics_train(metrics: Mapping[MetricKeyType, MetricValueType]) -> MutableMapping[str, NumericType]:
    return prefix_metrics(metrics, TRAIN_PREFIX)


def prefix_metrics_validation(metrics: Mapping[MetricKeyType, MetricValueType]) -> MutableMapping[str, NumericType]:
    return prefix_metrics(metrics, VALIDATION_PREFIX)


def prefix_metrics_test(metrics: Mapping[MetricKeyType, MetricValueType]) -> MutableMapping[str, NumericType]:
    return prefix_metrics(metrics, TEST_PREFIX)


def to_string(key: MetricKeyType) -> str:
    return key.value if isinstance(key, Enum) else key


def prefix_metrics(metrics: Mapping[MetricKeyType, MetricValueType], prefix: str) -> MutableMapping[str, NumericType]:
    return {f'{prefix} {to_string(key)}': value for key, value in metrics.items()}
