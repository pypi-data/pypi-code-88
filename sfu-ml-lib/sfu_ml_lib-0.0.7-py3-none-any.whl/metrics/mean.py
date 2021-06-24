from typing import Callable, Optional, Any

import tensorflow as tf
from tensorflow import Tensor, DType
from tensorflow.keras.metrics import Metric


class Mean(Metric):
    def __init__(
            self,
            function: Callable[[Any, Any, Any], Tensor],
            name: str,
            dtype: DType = tf.float32,
    ) -> None:

        super().__init__(name=name, dtype=dtype)

        self.function = function

        self.mean = self.add_weight('mean', initializer=tf.zeros_initializer, dtype=dtype)
        self.count = self.add_weight('count', initializer=tf.zeros_initializer, dtype=dtype)

    def update_mean(self, values: Tensor, batch_size: Tensor) -> None:
        new_count = self.count + batch_size
        new_mean = (tf.reduce_sum(values) + self.count * self.mean) / new_count

        self.mean.assign(new_mean)

    def update_state(self, y_true, y_pred, sample_weight: Optional[Tensor] = None) -> None:
        values = self.function(y_true, y_pred, sample_weight)
        batch_size = tf.cast(tf.size(values), self.dtype)

        self.update_mean(values, batch_size)
        self.count.assign_add(batch_size)

    def result(self) -> Tensor:
        return self.mean

    def reset_state(self) -> None:
        self.mean.assign(1, tf.zeros((), self.dtype))
        self.count.assign(tf.zeros((), self.dtype))
