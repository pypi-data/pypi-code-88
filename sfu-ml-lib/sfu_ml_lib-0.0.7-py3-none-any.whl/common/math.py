import tensorflow as tf


def sample_gumbel(shape: tf.Tensor, eps: float = 1e-20) -> tf.Tensor:
    return -tf.math.log(-tf.math.log(tf.random.uniform(shape) + eps) + eps)


def add_gumbel_sample(log_probabilities: tf.Tensor) -> tf.Tensor:
    return log_probabilities + sample_gumbel(tf.shape(log_probabilities))


def sample_categorical_log_probabilities(log_probabilities: tf.Tensor, axis: int = -1) -> tf.Tensor:
    return tf.argmax(add_gumbel_sample(log_probabilities), axis=axis)


def softmax_masked(tensor: tf.Tensor, mask: tf.Tensor) -> tf.Tensor:
    rank_difference = len(tensor.shape) - len(mask.shape)
    axis = -(rank_difference + 1)

    lengths = tf.reduce_sum(tf.cast(mask, dtype=tf.int32), axis=-1)
    lengths = tf.expand_dims(lengths, axis=-1)

    extra_dims = [1] * rank_difference
    mask_shape = tf.concat((tf.shape(mask), extra_dims), axis=0)
    lengths_shape = tf.concat((tf.shape(lengths), extra_dims), axis=0)

    mask = tf.reshape(mask, mask_shape)
    lengths = tf.reshape(lengths, lengths_shape)

    tensor = tf.where(mask, tensor, -1e9)
    tensor = tf.nn.softmax(tensor, axis=axis)
    tensor = tf.where(lengths > 0, tensor, 0.)

    return tensor
