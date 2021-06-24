import tensorflow as tf


class BiRNN(tf.keras.layers.Layer):
    def __init__(self, dim, return_sequences=True, rnn=tf.keras.layers.GRU, **kwargs):
        super(BiRNN, self).__init__(**kwargs)
        self._rnn_fw = rnn(dim, return_sequences=return_sequences, go_backwards=False, **kwargs)
        self._rnn_bw = rnn(dim, return_sequences=return_sequences, go_backwards=False, **kwargs)

    def call(self, seqs, seqs_len, seq_axis=1, batch_axis=0):
        fw_seqs = seqs
        bw_seqs = tf.reverse_sequence(seqs, seqs_len, seq_axis=seq_axis, batch_axis=batch_axis)
        fw_out = self._rnn_fw(fw_seqs)
        bw_out = self._rnn_bw(bw_seqs)
        bw_out = tf.reverse_sequence(bw_out, seqs_len, seq_axis=seq_axis, batch_axis=batch_axis)
        out = tf.concat([fw_out, bw_out], -1)
        return out