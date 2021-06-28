import tensorflow as tf


def segment_softmax(logits: tf.Tensor, segment_ids: tf.Tensor) -> tf.Tensor:
    logits_max = tf.math.segment_max(logits, segment_ids)

    logits_exp = tf.math.exp(logits - tf.gather(logits_max, segment_ids))

    partitions = tf.gather(tf.math.segment_sum(logits_exp, segment_ids), segment_ids)

    softmax = logits_exp / partitions

    return softmax


def segment_normalize(logits: tf.Tensor, segment_ids: tf.Tensor) -> tf.Tensor:
    partitions = tf.gather(tf.math.segment_sum(logits, segment_ids), segment_ids)

    probabilities = logits / partitions

    return probabilities
