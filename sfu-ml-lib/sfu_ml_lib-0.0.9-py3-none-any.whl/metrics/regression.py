from typing import Optional

import tensorflow as tf
from tensorflow import keras

from sfu_ml_lib.base.metrics import Metric


class PearsonCorrelation(keras.metrics.Metric):
    def __init__(self) -> None:
        super().__init__(name=Metric.PEARSON_CORRELATION.value, dtype=tf.float32)

        self.target_mean = self.add_weight('target_mean', initializer=tf.zeros_initializer)
        self.target_square_mean = self.add_weight('target_square_mean', initializer=tf.zeros_initializer)
        self.prediction_mean = self.add_weight('prediction_mean', initializer=tf.zeros_initializer)
        self.prediction_square_mean = self.add_weight('prediction_square_mean', initializer=tf.zeros_initializer)
        self.product_mean = self.add_weight('product_mean', initializer=tf.zeros_initializer)
        self.count = self.add_weight('count', initializer=tf.zeros_initializer)

    @classmethod
    def update_mean(cls, mean: tf.Variable, count: tf.Variable, values: tf.Tensor) -> None:
        new_count = count + tf.cast(tf.shape(values)[0], dtype=tf.float32)
        new_mean = (tf.reduce_sum(values) + count * mean) / new_count

        mean.assign(new_mean)

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        self.update_mean(self.target_mean, self.count, y_true)
        self.update_mean(self.target_square_mean, self.count, tf.square(y_true))
        self.update_mean(self.prediction_mean, self.count, y_pred)
        self.update_mean(self.prediction_square_mean, self.count, tf.square(y_pred))
        self.update_mean(self.product_mean, self.count, y_true * y_pred)

        self.count.assign_add(tf.cast(tf.shape(y_true)[0], dtype=tf.float32))

    def result(self) -> tf.Tensor:
        covariance = (self.product_mean - self.target_mean * self.prediction_mean)
        target_standard_deviation = tf.sqrt(self.target_square_mean - tf.square(self.target_mean))
        prediction_standard_deviation = tf.sqrt(self.prediction_square_mean - tf.square(self.prediction_mean))

        pearson_correlation = covariance / (target_standard_deviation * prediction_standard_deviation)

        return pearson_correlation

    def reset_state(self) -> None:
        self.target_mean.assign(tf.zeros(()))
        self.target_square_mean.assign(tf.zeros(()))
        self.prediction_mean.assign(tf.zeros(()))
        self.prediction_square_mean.assign(tf.zeros(()))
        self.product_mean.assign(tf.zeros(()))
        self.count.assign(tf.zeros(()))
