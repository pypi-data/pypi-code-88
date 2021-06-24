from typing import List, Optional

import tensorflow as tf
from tensorflow.keras.layers import Dense, LayerNormalization, Dropout
from tensorflow.keras.layers import Layer
from tensorflow.keras.models import Sequential

from sfu_ml_lib.modules.attention import MultiHeadSelfAttention


class SelfAttentionEncoderLayer(Layer):
    def __init__(self, num_heads: int, dropout_rate: float) -> None:
        super().__init__()

        self.num_heads = num_heads
        self.dropout_rate = dropout_rate

        self.dropout = Dropout(dropout_rate)
        self.layer_normalization_first = LayerNormalization()
        self.layer_normalization_second = LayerNormalization()

        self.attention: Optional[Layer] = None
        self.feed_forward: Optional[Layer] = None

        self.supports_masking = True

    def build(self, input_shape: List[int]) -> None:
        attention_size = input_shape[-1]

        self.attention = MultiHeadSelfAttention(self.num_heads)

        self.feed_forward = Sequential([
            Dense(attention_size, activation=tf.nn.relu),
            Dropout(self.dropout_rate),
            Dense(attention_size),
        ])

        self.built = True

    def call(self, inputs: tf.Tensor, training: bool = False, mask: Optional[tf.Tensor] = None) -> tf.Tensor:
        assert self.attention and self.feed_forward

        attention_output = self.attention(inputs, mask)
        attention_output = self.dropout(attention_output, training=training)
        attention_output = self.layer_normalization_first(inputs + attention_output)

        output = self.feed_forward(attention_output)
        output = self.dropout(output, training=training)
        output = self.layer_normalization_second(attention_output + output)

        return output
