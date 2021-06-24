import math

import tensorflow as tf


def tile_dimension(tensor: tf.Tensor, multiple: int, axis: int = -1) -> tf.Tensor:
    rank = tf.rank(tensor)

    axis = axis if axis >= 0 else rank + axis + 1

    multiples = tf.ones(rank + 1, dtype=tf.int32)
    multiples = tf.tensor_scatter_nd_update(multiples, [[axis]], [multiple])

    tensor_tiled = tf.tile(tf.expand_dims(tensor, axis), multiples)

    return tensor_tiled


def flatten(tensor: tf.Tensor, axis: int = -1) -> tf.Tensor:
    start_axis = axis - 1

    shape = tf.shape(tensor)
    shape = tf.concat((shape[:start_axis], [tf.reduce_prod(shape[start_axis:])]), axis=0)
    tensor_flattened = tf.reshape(tensor, shape)

    joined_shape = tensor.shape[start_axis:]

    if None not in joined_shape:
        shape = tensor.shape[:start_axis] + [math.prod(joined_shape)]
        tensor_flattened.set_shape(shape)

    return tensor_flattened
