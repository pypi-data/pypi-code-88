#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import random

import tensorflow as tf

from absl import logging

lightseq_ops = None
LIGHTSEQ_PATH = os.path.join(os.path.dirname(__file__), 'liblightseq_op.so')
try:
    lightseq_ops = tf.load_op_library(LIGHTSEQ_PATH)
    print("successfully load lightseq ops")
except tf.errors.NotFoundError as e:
    print("Can not find {}, use tensorflow operators".format(LIGHTSEQ_PATH))
    logging.info("Can not find {}, use tensorflow operators".format(LIGHTSEQ_PATH))
    raise e

@tf.RegisterGradient("LayerNorm")
def layer_norm_grad_func(op, *grads):
    """register backward for layer norm"""
    norm_in = op.inputs[0]
    norm_scale = op.inputs[1]
    norm_bias = op.inputs[2]
    output = op.outputs[0]
    means = op.outputs[1]
    vars = op.outputs[2]
    output_grad = grads[0]
    return lightseq_ops.layer_norm_grad(
        output_grad, norm_scale, norm_bias, means, vars, output
    )

class LSLayerNorm(tf.keras.layers.Layer):
    def __init__(
        self, trainable=True, name="lightseq_layernorm", **kwargs
    ):
        super().__init__(name=name, trainable=trainable)

    def build(self, input_shape):
        param_shape = [input_shape[-1]]
        self.gamma = self.add_weight(
            name="gamma",
            shape=param_shape,
            initializer="ones",
            regularizer=None,
            constraint=None,
            trainable=True,
            dtype="float32",
        )
        self.beta = self.add_weight(
            name="beta",
            shape=param_shape,
            initializer="zeros",
            regularizer=None,
            constraint=None,
            trainable=True,
            dtype="float32",
        )
        self.built = True

    def call(self, inputs, *args, **kwargs):
        output, _, _ = lightseq_ops.layer_norm(
            inputs,
            self.gamma,
            self.beta,
        )
        return output

class LSTransformerEncoderLayer(tf.keras.layers.Layer):
    def __init__(
            self,
            intermediate_size,
            hidden_size,
            hidden_dropout_ratio=0.0,
            ffn_dropout_ratio=0.3,
            attn_dropout_ratio=0.0,
            epsilon=1e-6,
            trainable=True,
            name="encoder_layer",
            heads=8,
            pre_or_postLayerNorm=True,
            **kwargs
    ):

        self.intermediate_size = intermediate_size
        self.hidden_size = hidden_size
        self.hidden_dropout_ratio = hidden_dropout_ratio
        self.ffn_dropout_ratio = ffn_dropout_ratio
        self.attn_dropout_ratio = attn_dropout_ratio
        self.layer_norm_epsilon = epsilon
        self.trainable = trainable
        self.num_heads = heads
        self.pre_or_postLayerNorm = pre_or_postLayerNorm
        super().__init__(name=name, trainable=trainable, **kwargs)

    def build(self, input_shape):
        dtype = tf.float32
        hidden_size = self.hidden_size 
        intermediate_size = self.intermediate_size
        attn_qkvw = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size * 3))), [-1])
        attn_qkvb = tf.zeros((hidden_size * 3))
        attn_ow = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size))), [-1])
        attn_ob = tf.zeros((hidden_size))
        attn_nw = tf.ones((hidden_size))
        attn_nb = tf.zeros((hidden_size))
        inter_w = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, intermediate_size))), [-1])
        inter_b = tf.zeros((intermediate_size))
        output_w = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(intermediate_size, hidden_size))), [-1])
        output_b = tf.zeros((hidden_size))
        ffn_nw = tf.ones((hidden_size))
        ffn_nb =  tf.zeros((hidden_size))
        w = tf.concat([attn_qkvw, attn_qkvb, attn_ow, attn_ob, attn_nw, attn_nb , inter_w, inter_b, output_w, output_b, ffn_nw, ffn_nb], 0)
        n = hidden_size*hidden_size * 4 + hidden_size*9+hidden_size*intermediate_size*2 + intermediate_size
        self.w = self.add_weight(
            name="encoder_weight",
            shape=[n],
            initializer="zero",
            regularizer=None,
            constraint=None,
            trainable=True,
            dtype=dtype,
        )
        self.set_weights([w])

        self.built = True

    def set_weight(self, w):
        self.w = w



    def call(self, inputs, inputs_mask, is_training, *args, **kwargs):
        (output,
         gemm_qkv_inp,
         qkv,
         soft_out,
         ctx_buf_b,
         attn_o_inp,
         ff1_inp,
         relu_inp,
         ff2_inp,
         attn_prob_dropout_mask,
         attn_dropout_mask,
         ffn_activation_dropout_mask,
         ffn_dropout_mask,
         ffn_ln_mean,
         ffn_ln_var,
         attn_ln_mean,
         attn_ln_var)  = lightseq_ops.transformer_encoder_layer(
            inputs,
            inputs_mask,
            self.w,
            num_heads=self.num_heads,
            intermediate_size=self.intermediate_size,
            attn_prob_dropout_ratio=self.attn_dropout_ratio,
            activation_dropout_ratio=self.ffn_dropout_ratio,
            hidden_dropout_ratio=self.hidden_dropout_ratio,
            seed=random.randint(0,100000),
            pre_or_postLayerNorm=self.pre_or_postLayerNorm,
            training_mode=is_training
        )
        return output

@tf.RegisterGradient("TransformerEncoderLayer")
def transformer_encoder_layer_grad_func(op, *grads):
    """register backward for layer norm"""
    inputs, inputs_mask, weight = op.inputs
    (outputs,
     gemm_qkv_inp,
     qkv,
     soft_out,
     ctx_buf_b,
     attn_o_inp,
     ff1_inp,
     relu_inp,
     ff2_inp,
     attn_prob_dropout_mask,
     attn_dropout_mask,
     ffn_activation_dropout_mask,
     ffn_dropout_mask,
     ffn_ln_mean,
     ffn_ln_var,
     attn_ln_mean,
     attn_ln_var) = op.outputs
    grad_out = grads[0]

    activation_dropout_ratio = op.get_attr("activation_dropout_ratio")
    attn_prob_dropout_ratio = op.get_attr("attn_prob_dropout_ratio")
    hidden_dropout_ratio = op.get_attr("hidden_dropout_ratio")
    pre_or_postLayerNorm = op.get_attr("pre_or_postLayerNorm")
    grad_input, grad_weight = lightseq_ops.transformer_encoder_layer_grad(
            grad_out,
            outputs,
            inputs,
            inputs_mask,
            weight,
            gemm_qkv_inp,
            qkv,
            soft_out,
            ctx_buf_b,
            attn_o_inp,
            ff1_inp,
            relu_inp,
            ff2_inp,
            attn_prob_dropout_mask,
            attn_dropout_mask,
            ffn_activation_dropout_mask,
            ffn_dropout_mask,
            ffn_ln_mean,
            ffn_ln_var,
            attn_ln_mean,
            attn_ln_var,
            activation_dropout_ratio=activation_dropout_ratio,
            attn_prob_dropout_ratio=attn_prob_dropout_ratio,
            hidden_dropout_ratio=hidden_dropout_ratio,
            pre_or_postLayerNorm=pre_or_postLayerNorm)
    return [
        grad_input,
        None,  # mask
        grad_weight,
    ]


class LSTransformerDecoderLayer(tf.keras.layers.Layer):
    def __init__(
        self,
        num_heads,
        intermediate_size,
        hidden_size,
        attn_prob_dropout_ratio,
        activation_dropout_ratio,
        hidden_dropout_ratio,
        pre_or_postLayerNorm=True,
        trainable=True,
        predict=False,
        epsilon=1e-8,
        name="decoder_layer",
        **kwargs
    ):
        self.intermediate_size = intermediate_size
        self.hidden_size = hidden_size

        self.attn_prob_dropout_ratio = attn_prob_dropout_ratio
        self.activation_dropout_ratio = activation_dropout_ratio
        self.hidden_dropout_ratio=     hidden_dropout_ratio
        self.layer_norm_epsilon = epsilon
        self.trainable = trainable
        self.num_heads = num_heads
        self.pre_or_postLayerNorm = pre_or_postLayerNorm
        self.predict = predict
        super().__init__(name=name, trainable=trainable, **kwargs)

    def build(self, input_shape):
        dtype = tf.float32
        hidden_size = self.hidden_size 
        intermediate_size = self.intermediate_size
        attn_qkvw = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size * 3))), [-1])
        attn_qkvb = tf.zeros((hidden_size * 3))
        attn_ow = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size))), [-1])
        attn_ob = tf.zeros((hidden_size))
        attn_nw = tf.ones((hidden_size))
        attn_nb = tf.zeros((hidden_size))

        encdec_attn_qw = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size))), [-1])
        encdec_attn_qb = tf.zeros((hidden_size))
        encdec_attn_ow = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size))), [-1])
        encdec_attn_ob = tf.zeros((hidden_size))
        encdec_attn_nw = tf.ones((hidden_size))
        encdec_attn_nb = tf.zeros((hidden_size))

        inter_w = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, intermediate_size))), [-1])
        inter_b = tf.zeros((intermediate_size))
        output_w = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(intermediate_size, hidden_size))), [-1])
        output_b = tf.zeros((hidden_size))
        ffn_nw = tf.ones((hidden_size))
        ffn_nb =  tf.zeros((hidden_size))

        encdec_attn_kvw = tf.reshape(tf.constant(tf.initializers.GlorotUniform()(shape=(hidden_size, hidden_size * 2))), [-1])
        encdec_attn_kvb = tf.zeros((hidden_size * 2))
        w = tf.concat([attn_qkvw, attn_qkvb, attn_ow, attn_ob, attn_nw, attn_nb, encdec_attn_qw, encdec_attn_qb, encdec_attn_ow, encdec_attn_ob, encdec_attn_nw, encdec_attn_nb,inter_w, inter_b, output_w, output_b, ffn_nw, ffn_nb, encdec_attn_kvw, encdec_attn_kvb], 0)
        n = hidden_size*hidden_size * 6 + hidden_size*13 + hidden_size*intermediate_size*2 + intermediate_size + hidden_size*hidden_size*2 + hidden_size * 2
        self.w = self.add_weight(
            name="decoder_weight",
            shape=[n],
            initializer="zero",
            regularizer=None,
            constraint=None,
            trainable=True,
            dtype=dtype,
        )
        self.set_weights([w])

        self.built = True

    def set_weight(self, w):
        self.w = w

    def call(self, dec_input, enc_output, enc_mask, cached_k, cached_v, is_training, predict=False, *args, **kwargs):
        (dec_output,
         gemm_qkv_inp,
         qkv,
         soft_out,
         ctx_buf_b,
         attn_o_inp,
         gemm_q_inp,
         encdec_q,
         encdec_soft_out,
         encdec_attn_score,
         encdec_attn_output,
         ff1_inp,
         relu_inp,
         ff2_inp,
         shared_encdec_kv_out,
         shared_grad_encdec_kv,
         attn_prob_dropout_mask,
         attn_dropout_mask,
         xattn_prob_dropout_mask,
         xattn_dropout_mask,
         ffn_activation_dropout_mask,
         ffn_dropout_mask,
         ffn_ln_mean,
         ffn_ln_var,
         attn_ln_mean,
         attn_ln_var,
         xattn_ln_mean,
         xattn_ln_var,
         new_cached_k,
         new_cached_v) = lightseq_ops.transformer_decoder_layer(
             dec_input,
             enc_output,
             enc_mask,
             cached_k,
             cached_v,
             self.w,
             num_heads=self.num_heads,
             intermediate_size=self.intermediate_size,
             attn_prob_dropout_ratio=self.attn_prob_dropout_ratio,
             activation_dropout_ratio=self.activation_dropout_ratio,
             hidden_dropout_ratio=self.hidden_dropout_ratio,
             pre_or_postLayerNorm=self.pre_or_postLayerNorm,
             training_mode=is_training,
             predict=predict
        )
        return  (dec_output,
                 new_cached_k,
                 new_cached_v)

@tf.RegisterGradient("TransformerDecoderLayer")
def transformer_encoder_layer_grad_func(op, *grads):
    """register backward for layer norm"""
    (dec_input,
     enc_output,
     enc_mask,
     cached_k,
     cached_v,
     weight) = op.inputs

    (dec_output,
     gemm_qkv_inp,
     qkv,
     soft_out,
     ctx_buf_b,
     attn_o_inp,
     gemm_q_inp,
     encdec_q,
     encdec_soft_out,
     encdec_attn_score,
     encdec_attn_output,
     ff1_inp,
     relu_inp,
     ff2_inp,
     shared_encdec_kv_out,
     shared_grad_encdec_kv,
     attn_prob_dropout_mask,
     attn_dropout_mask,
     xattn_prob_dropout_mask,
     xattn_dropout_mask,
     ffn_activation_dropout_mask,
     ffn_dropout_mask,
     ffn_ln_mean,
     ffn_ln_var,
     attn_ln_mean,
     attn_ln_var,
     xattn_ln_mean,
     xattn_ln_var,
     new_cached_k,
     new_cached_v) = op.outputs
    grad_dec_output = grads[0]

    attn_prob_dropout_ratio = op.get_attr("attn_prob_dropout_ratio")
    activation_dropout_ratio = op.get_attr("activation_dropout_ratio")
    hidden_dropout_ratio = op.get_attr("hidden_dropout_ratio")
    pre_or_postLayerNorm = op.get_attr("pre_or_postLayerNorm")


    (grad_dec_input,
     grad_enc_output,
     grad_weight) = lightseq_ops.transformer_decoder_layer_grad(
       grad_dec_output,
       dec_input,
       enc_output,
       enc_mask,
       dec_output,
       weight,
       gemm_qkv_inp,
       qkv,
       soft_out,
       ctx_buf_b,
       attn_o_inp,
       gemm_q_inp,
       encdec_q,
       encdec_soft_out,
       encdec_attn_score,
       encdec_attn_output,
       ff1_inp,
       relu_inp,
       ff2_inp,
       shared_encdec_kv_out,
       attn_prob_dropout_mask,
       attn_dropout_mask,
       xattn_prob_dropout_mask,
       xattn_dropout_mask,
       ffn_activation_dropout_mask,
       ffn_dropout_mask,
       ffn_ln_mean,
       ffn_ln_var,
       attn_ln_mean,
       attn_ln_var,
       xattn_ln_mean,
       xattn_ln_var,
       attn_prob_dropout_ratio=attn_prob_dropout_ratio,
       activation_dropout_ratio=activation_dropout_ratio,
       hidden_dropout_ratio=hidden_dropout_ratio,
       pre_or_postLayerNorm=pre_or_postLayerNorm)
    return [grad_dec_input,
            grad_enc_output,
            None, #enc_mask
            None, #cached_k
            None, #cached_v
            grad_weight]


