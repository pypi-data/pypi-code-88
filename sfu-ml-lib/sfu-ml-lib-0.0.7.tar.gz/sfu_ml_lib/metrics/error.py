from typing import Optional

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.metrics import AUC

from sfu_ml_lib.base.metrics import Metric


class PredictionBias(keras.metrics.Metric):
    def __init__(self) -> None:
        super().__init__(name=Metric.PREDICTION_BIAS.value, dtype=tf.float32)

        self.target_mean = self.add_weight('target_mean', initializer=tf.zeros_initializer)
        self.prediction_mean = self.add_weight('prediction_mean', initializer=tf.zeros_initializer)
        self.count = self.add_weight('count', initializer=tf.zeros_initializer)

    @staticmethod
    def update_mean(mean: tf.Variable, count: tf.Variable, batch_size: tf.Tensor, values: tf.Tensor) -> None:
        new_count = count + batch_size
        new_mean = (tf.reduce_sum(values) + count * mean) / new_count

        mean.assign(new_mean)

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        assert sample_weight is None

        batch_size = tf.cast(tf.shape(y_true)[0], dtype=tf.float32)
        predictions = tf.round(y_pred)

        self.update_mean(self.target_mean, self.count, batch_size, y_true)
        self.update_mean(self.prediction_mean, self.count, batch_size, predictions)

        self.count.assign_add(batch_size)

    def result(self) -> tf.Tensor:
        return self.prediction_mean - self.target_mean

    def reset_state(self) -> None:
        self.target_mean.assign(tf.zeros(()))
        self.prediction_mean.assign(tf.zeros(()))
        self.count.assign(tf.zeros(()))


class CutoffThreshold(keras.metrics.Metric):
    def __init__(self) -> None:
        super().__init__(name=Metric.CUTOFF_THRESHOLD.value, dtype=tf.float32)

        self.auc = AUC()

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        self.auc.update_state(y_true, y_pred, sample_weight)

    def result(self) -> tf.Tensor:
        tpr = tf.math.divide_no_nan(self.auc.true_positives, self.auc.true_positives + self.auc.false_negatives)
        fpr = tf.math.divide_no_nan(self.auc.false_positives, self.auc.false_positives + self.auc.true_negatives)

        index = tf.argmax(tpr - fpr)
        threshold = tf.convert_to_tensor(self.auc.thresholds)[index]

        return threshold

    def reset_states(self) -> None:
        self.auc.reset_states()
