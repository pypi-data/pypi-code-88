from typing import List, Optional, Mapping, Union

import tensorflow as tf
import tensorflow.keras as keras

from sfu_ml_lib.base.metrics import Metric
from sfu_ml_lib.metrics.error import CutoffThreshold


class F1Score(keras.metrics.Metric):
    def __init__(self, num_classes: int, average: str = 'weighted') -> None:
        if average == 'macro':
            metric = Metric.MACRO_F1
        elif average == 'micro':
            metric = Metric.MICRO_F1
        else:
            metric = Metric.WEIGHTED_F1

        super().__init__(name=metric.value, dtype=tf.float32)

        self.num_classes = num_classes
        self.average = average

        self.axis = 0 if self.average != 'micro' else None
        self.init_shape = [self.num_classes] if self.average != 'micro' else []

        self.true_positives = self.create_zero_weights('true_positives', self.init_shape)
        self.false_positives = self.create_zero_weights('false_positives', self.init_shape)
        self.false_negatives = self.create_zero_weights('false_negatives', self.init_shape)
        self.weights_intermediate = self.create_zero_weights('weights_intermediate', self.init_shape)

    def create_zero_weights(self, name: str, shape: List[tf.DType]) -> tf.Variable:
        return self.add_weight(name, shape=shape, initializer=tf.zeros_initializer, dtype=tf.float32)

    def compute_weighted_sum(self, values: tf.Tensor, sample_weight: tf.Tensor) -> tf.Tensor:
        if sample_weight is not None:
            values *= sample_weight[:, tf.newaxis]

        weighted_sum = tf.math.reduce_sum(values, axis=self.axis)

        return weighted_sum

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        self.true_positives.assign_add(self.compute_weighted_sum(y_pred * y_true, sample_weight))
        self.false_positives.assign_add(self.compute_weighted_sum(y_pred * (1. - y_true), sample_weight))
        self.false_negatives.assign_add(self.compute_weighted_sum((1. - y_pred) * y_true, sample_weight))
        self.weights_intermediate.assign_add(self.compute_weighted_sum(y_true, sample_weight))

    def result(self) -> tf.Tensor:
        precision = tf.math.divide_no_nan(self.true_positives, self.true_positives + self.false_positives)
        recall = tf.math.divide_no_nan(self.true_positives, self.true_positives + self.false_negatives)

        mul_value = 2 * precision * recall
        add_value = precision + recall
        f1_score = tf.math.divide_no_nan(mul_value, add_value)

        if self.average == 'weighted':
            weights = tf.math.divide_no_nan(self.weights_intermediate, tf.reduce_sum(self.weights_intermediate))
            f1_score = tf.reduce_sum(weights * f1_score)
        else:
            f1_score = tf.reduce_mean(f1_score)

        return f1_score

    def get_config(self) -> Mapping[str, Union[tf.Tensor, int, bool, float, str]]:
        config = {'num_classes': self.num_classes, 'average': self.average}

        base_config = super().get_config()

        return {**base_config, **config}

    def reset_state(self) -> None:
        self.true_positives.assign(tf.zeros(self.init_shape, tf.float32))
        self.false_positives.assign(tf.zeros(self.init_shape, tf.float32))
        self.false_negatives.assign(tf.zeros(self.init_shape, tf.float32))
        self.weights_intermediate.assign(tf.zeros(self.init_shape, tf.float32))


class MultiClassF1Score(F1Score):
    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        targets = tf.one_hot(y_true, self.num_classes)
        predictions = tf.one_hot(tf.argmax(y_pred, axis=-1), self.num_classes)

        super().update_state(targets, predictions, sample_weight)


class MultiLabelF1Score(F1Score):
    def __init__(
            self,
            num_classes: int,
            average: str = 'weighted',
            from_logits: bool = False,
            adapt_thresholds: bool = False) -> None:

        super().__init__(num_classes, average)

        self.from_logits = from_logits
        self.cutoff_threshold = CutoffThreshold() if adapt_thresholds else None

    def get_thresholds(
            self,
            y_true: tf.Tensor,
            y_pred: tf.Tensor,
            sample_weight: Optional[tf.Tensor] = None) -> tf.Tensor:

        if self.cutoff_threshold is None:
            thresholds = tf.fill((self.num_classes,), tf.convert_to_tensor(.5, dtype=tf.float32))
        else:
            self.cutoff_threshold.update_state(y_true, y_pred, sample_weight)
            thresholds = self.result()

        return thresholds

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        thresholds = self.get_thresholds(y_true, y_pred, sample_weight)

        predictions = tf.sigmoid(y_pred) if self.from_logits else y_pred
        predictions = tf.cast(predictions >= thresholds, dtype=tf.float32)

        super().update_state(y_true, predictions, sample_weight)
