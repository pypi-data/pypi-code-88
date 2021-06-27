from typing import Optional

import tensorflow as tf
from tensorflow.keras.metrics import CategoricalCrossentropy

from sfu_ml_lib.base.metrics import Metric


class MultiClassCrossEntropy(CategoricalCrossentropy):
    def __init__(self, num_classes: int, from_logits: bool):
        super().__init__(name=Metric.CROSS_ENTROPY.value, from_logits=from_logits)
        self.num_classes = num_classes

    def update_state(self, y_true: tf.Tensor, y_pred: tf.Tensor, sample_weight: Optional[tf.Tensor] = None) -> None:
        targets = tf.one_hot(y_true, self.num_classes)
        super().update_state(targets, y_pred, sample_weight)
