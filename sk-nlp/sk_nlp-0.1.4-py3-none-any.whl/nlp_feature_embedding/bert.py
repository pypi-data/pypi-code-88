# -*- coding:utf-8 -*-
"""
bert基本模型加载
"""

from keras.layers import Layer, Multiply, Subtract, Concatenate
import tensorflow as tf
from bert4keras.backend import keras, K
from bert4keras.models import build_transformer_model
from bert4keras.snippets import sequence_padding
from keras.layers import Lambda
from bert4keras.tokenizers import Tokenizer
from sk_nlp.util import file_conf

batch_size = 128


class MaskLayer(Layer):
    """
    mask 层，屏蔽掉seg_id为0的词语

    """

    def __init__(self, output_dim=768, **kwargs):
        self.output_dim = output_dim
        super(MaskLayer, self).__init__(**kwargs)

    def build(self, input_shape):
        """
        创建层的权重

        :param input_shape:Keras tensor (future input to layer) or list/tuple of Keras tensors
        :return:
        """
        super(MaskLayer, self).build(input_shape)  # 一定要在最后调用它

    def call(self, x):
        return K.tile(K.expand_dims(x, axis=-1), [1, 1, self.output_dim])

    def compute_output_shape(self, input_shape):
        output_shape = list(input_shape)
        output_shape.append(self.output_dim)
        return tuple(output_shape)


class ReverseMaskLayer(Layer):
    """
    反转 mask 层，屏蔽掉seg_id为1的词语

    """

    def call(self, x):
        return tf.cast(
            tf.math.logical_not(
                tf.cast(
                    x,
                    dtype=tf.bool)),
            dtype=tf.float32)

    def compute_output_shape(self, input_shape):
        output_shape = list(input_shape)
        return tuple(output_shape)


class SepLayer(Layer):
    """
    sep mask 层，屏蔽掉sep位置的输出

    """

    def call(self, x):
        return tf.cast(K.equal(x, 102), dtype=tf.float32)

    def compute_output_shape(self, input_shape):
        output_shape = list(input_shape)
        return tuple(output_shape)


def load_bert_model(with_mlm=True, with_pool=False,
                    return_keras_model=True,
                    config_path=file_conf.bert_config_file_path,
                    checkpoint_path=file_conf.bert_checkpoint_path):
    """
    加载bert 模型

    :param with_mlm: 是否正则化
    :param with_pool: 是否池化
    :param return_keras_model: 返回的是keras model 还是 tensorflow 模型
    :param config_path: bert 模型配置文件路径
    :param checkpoint_path: bert 模型路径
    :return:
    """
    bert_model = build_transformer_model(
        config_path=config_path,
        checkpoint_path=checkpoint_path,
        with_mlm=with_mlm,
        with_pool=with_pool,
        return_keras_model=return_keras_model
    )
    return bert_model


def build_model_feature(origin_model, use_cls=False):
    """
    搭建新的句子模型

    :param origin_model: 原始模型，一般为bert
    :param use_cls: 是否使用cls位置的输出
    :return: model：新模型
    """

    layer_name = 'MLM-Norm'
    token_id_layer = origin_model.input[0]
    sep_layer = SepLayer()(token_id_layer)
    sep_mask_layer = MaskLayer()(sep_layer)
    seg_id_layer = origin_model.input[1]
    seg_mask_layer = MaskLayer()(seg_id_layer)
    seg_mask_layer_reverse = ReverseMaskLayer()(seg_mask_layer)
    mask_layer = Subtract()([seg_mask_layer_reverse, sep_mask_layer])
    bert_feature_layer = origin_model.get_layer(layer_name).output
    sen_encoder = Multiply()([bert_feature_layer, mask_layer])
    output = Lambda(lambda x: keras.backend.mean(
        x[:, 1:], axis=1), name='mean-token')(sen_encoder)
    if use_cls:
        output_1 = output
        output_2 = Lambda(
            lambda x: x[:, 0], name='CLS-token')(origin_model.get_layer(layer_name).output)
        output = Concatenate()([output_1, output_2])

    model = keras.models.Model(origin_model.input, output)
    return model


def encoder(model, data_list, dict_path=file_conf.bert_vocab_file_path):
    """
    使用句向量模型，将句子转码成句向量

    :param model: 模型
    :param data_list: 句子列表（没有分词）
    :param dict_path: bert模型词汇表
    :return: data_list中的每个句子对应的句向量列表

    Example
    -------
    >>> origin_model = load_bert_model()
    >>> new_model = build_model_feature(origin_model)
    >>> question_list = ["我爱这个伟大的世界", "欣赏世界的风景"]
    >>> sen_vector_lists = encoder(new_model, question_list)
    >>> print(sen_vector_lists.shape)
    """

    tokenizer = Tokenizer(do_lower_case=True, token_dict=dict_path)  # 建立分词器
    token_ids = []
    segment_ids = []
    for data in data_list:
        token_id, segment_id = tokenizer.encode(data)
        token_ids.append(token_id)
        segment_ids.append(segment_id)
    token_ids = sequence_padding(token_ids)
    segment_ids = sequence_padding(segment_ids, padding=1)
    res = model.predict([token_ids, segment_ids])
    return res


def masked_crossentropy(y_true, y_pred):
    """
    mask掉非预测部分，计算交叉熵

    :param y_true: 真实的Y标签
    :param y_pred: 预测的Y标签
    :return: 损失值
    """

    y_true = K.reshape(y_true, K.shape(y_true)[:2])
    y_mask = K.cast(K.greater(y_true, 0.5), K.floatx())
    loss = K.sparse_categorical_crossentropy(y_true, y_pred)
    loss = K.sum(loss * y_mask) / K.sum(y_mask)
    return loss[None, None]


if __name__ == '__main__':

    """
    测试模块是否正常运行
    """
    origin_model = load_bert_model()
    new_model = build_model_feature(origin_model)
    question_list = ["我爱这个伟大的世界", "欣赏世界的风景"]
    sen_vector_lists = encoder(new_model, question_list)
    print(sen_vector_lists.shape)
