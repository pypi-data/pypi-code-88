from typing import List, Optional, Mapping, Any

import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense

from sfu_ml_lib.common import math
from sfu_ml_lib.common import shaping


class MultiHeadDense(Layer):
    def __init__(
            self,
            units: int,
            num_heads: int,
            activation=None,
            use_bias: bool = True,
            kernel_initializer='glorot_uniform',
            bias_initializer='zeros',
            kernel_regularizer=None,
            bias_regularizer=None,
            activity_regularizer=None,
            kernel_constraint=None,
            bias_constraint=None,
            **kwargs) -> None:

        super().__init__(activity_regularizer=tf.keras.regularizers.get(activity_regularizer), **kwargs)

        self.units = units
        self.num_heads = num_heads
        self.use_bias = use_bias

        self.activation = tf.keras.activations.get(activation)
        self.kernel_initializer = tf.initializers.get(kernel_initializer)
        self.bias_initializer = tf.initializers.get(bias_initializer)
        self.kernel_regularizer = tf.keras.regularizers.get(kernel_regularizer)
        self.bias_regularizer = tf.keras.regularizers.get(bias_regularizer)
        self.kernel_constraint = tf.keras.constraints.get(kernel_constraint)
        self.bias_constraint = tf.keras.constraints.get(bias_constraint)

        self.kernel: Optional[Layer] = None
        self.bias: Optional[Layer] = None

    def build(self, input_shape: List[int]) -> None:
        self.kernel = self.add_weight(
            name='kernel',
            shape=[input_shape[-2], self.units, self.num_heads],
            initializer=self.kernel_initializer,
            regularizer=self.kernel_regularizer,
            constraint=self.kernel_constraint,
            dtype=self.dtype,
            trainable=True,
        )

        if self.use_bias:
            self.bias = self.add_weight(
                name='bias',
                shape=[self.units, self.num_heads],
                initializer=self.bias_initializer,
                regularizer=self.bias_regularizer,
                constraint=self.bias_constraint,
                dtype=self.dtype,
                trainable=True,
            )

        self.built = True

    def call(self, inputs: tf.Tensor, **kwargs) -> tf.Tensor:
        outputs = tf.einsum('...ih,ijh->...jh', inputs, self.kernel)

        if self.use_bias:
            outputs = tf.add(outputs, self.bias)

        if self.activation is not None:
            outputs = self.activation(outputs)

        return outputs

    def get_config(self) -> Mapping[str, Any]:
        new_config = {
            'units': self.units,
            'use_bias': self.use_bias,
            'activation': tf.keras.activations.serialize(self.activation),
            'kernel_initializer': tf.initializers.serialize(self.kernel_initializer),
            'bias_initializer': tf.initializers.serialize(self.bias_initializer),
            'kernel_regularizer': tf.keras.regularizers.serialize(self.kernel_regularizer),
            'bias_regularizer': tf.keras.regularizers.serialize(self.bias_regularizer),
            'activity_regularizer': tf.keras.regularizers.serialize(self.activity_regularizer),
            'kernel_constraint': tf.keras.constraints.serialize(self.kernel_constraint),
            'bias_constraint': tf.keras.constraints.serialize(self.bias_constraint)
        }

        config = super().get_config()
        config.update(new_config)

        return config


class MultiHeadAttention(Layer):
    def __init__(
            self,
            num_heads: int,
            temperature: float = 1.,
            key_transformer: Optional[Layer] = None,
            value_transformer: Optional[Layer] = None,
            name: Optional[str] = None) -> None:

        super().__init__(name=name)

        self.num_heads = num_heads
        self.temperature = temperature
        self.key_transformer = key_transformer
        self.value_transformer = value_transformer

        self.coefficient_kernel: Optional[tf.Variable] = None
        self.coefficient_bias: Optional[tf.Variable] = None
        self.dense: Optional[Layer] = None

    def build(self, input_shape: List[int]) -> None:
        attention_size = input_shape[-1]

        self.coefficient_kernel = self.add_weight(
            name='coefficient_kernel',
            shape=(attention_size, self.num_heads),
            initializer=tf.initializers.glorot_uniform(),
            dtype=tf.float32,
            trainable=True,
        )

        self.coefficient_bias = self.add_weight(
            name='coefficient_bias',
            shape=(self.num_heads,),
            initializer=tf.initializers.zeros(),
            dtype=tf.float32,
            trainable=True,
        )

        self.dense = Dense(attention_size)

        self.built = True

    def compute_mask(self, inputs: tf.Tensor, mask: Optional[tf.Tensor] = None) -> Optional[tf.Tensor]:
        if mask is None:
            return None

        mask = tf.reduce_any(mask, axis=-1)

        return mask

    def call(self, inputs: tf.Tensor, mask: Optional[tf.Tensor] = None, training: bool = False) -> tf.Tensor:
        assert self.dense

        if mask is None:
            mask = tf.ones(tf.shape(inputs)[:-1], dtype=tf.bool)

        coefficients = values = shaping.tile_dimension(inputs, self.num_heads)

        if self.key_transformer:
            coefficients = self.key_transformer(coefficients, training=training)

        coefficients = tf.einsum('...ih,ih->...h', coefficients, self.coefficient_kernel)
        coefficients = tf.nn.bias_add(coefficients, self.coefficient_bias)
        coefficients /= self.temperature
        coefficients = math.softmax_masked(coefficients, mask)

        if self.value_transformer:
            values = self.value_transformer(values, training=training)

        values = tf.einsum('...sh,...sih->...ih', coefficients, values)
        values = shaping.flatten(values)
        values = self.dense(values)

        return values


class MultiHeadSelfAttention(Layer):
    def __init__(self, num_heads: int) -> None:
        super().__init__()

        self.num_heads = num_heads

        self.temperature = None

        self.query_layer: Optional[Layer] = None
        self.key_layer: Optional[Layer] = None
        self.value_layer: Optional[Layer] = None
        self.dense: Optional[Layer] = None

    def build(self, input_shape: List[int]) -> None:
        attention_size = input_shape[-1]

        self.temperature = tf.sqrt(tf.cast(attention_size, tf.float32))

        self.query_layer = MultiHeadDense(attention_size, self.num_heads)
        self.key_layer = MultiHeadDense(attention_size, self.num_heads)
        self.value_layer = MultiHeadDense(attention_size, self.num_heads)
        self.dense = Dense(attention_size)

        self.built = True

    def call(self, inputs: tf.Tensor, mask: Optional[tf.Tensor] = None) -> tf.Tensor:
        assert self.query_layer and self.key_layer and self.value_layer and self.dense

        if mask is None:
            mask = tf.ones(tf.shape(inputs)[:-1], dtype=tf.bool)

        inputs = shaping.tile_dimension(inputs, self.num_heads)

        queries = self.query_layer(inputs)
        keys = self.key_layer(inputs)

        coefficients = tf.einsum('...qih,...kih->...qkh', queries, keys)
        coefficients /= self.temperature
        coefficients = math.softmax_masked(coefficients, mask)

        values = self.value_layer(inputs)
        values = tf.einsum('...qkh,...qih->...qih', coefficients, values)
        values = shaping.flatten(values)
        values = self.dense(values)

        return values
