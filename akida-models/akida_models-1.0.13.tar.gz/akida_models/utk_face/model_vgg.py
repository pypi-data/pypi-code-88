#!/usr/bin/env python
# ******************************************************************************
# Copyright 2020 Brainchip Holdings Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ******************************************************************************
"""
VGG model definition for UTKFace regression.
"""

from tensorflow.keras import Model
from tensorflow.keras.layers import Dropout, Flatten, Input
from tensorflow.keras.utils import get_file

# CNN2SNN imports
from cnn2snn import load_quantized_model, quantize

from ..layer_blocks import conv_block, dense_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/vgg/'


def vgg_utk_face(input_shape=(32, 32, 3),
                 weight_quantization=0,
                 activ_quantization=0,
                 input_weight_quantization=None):
    """Instantiates a VGG-like model for the regression example on age
    estimation using UTKFace dataset.

    Args:
        input_shape (tuple): input shape tuple of the model
        weight_quantization (int): sets all weights in the model to have
            a particular quantization bitwidth except for the weights in the
            first layer.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization (int): sets all activations in the model to have a
            particular activation quantization bitwidth.

            * '0' implements floating point 32-bit activations.
            * '1' through '8' implements n-bit weights where n is from 1-8 bits.
        input_weight_quantization (int): sets weight quantization in the first
            layer. Defaults to weight_quantization value.

            * 'None' implements the same bitwidth as the other weights.
            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns:
        tf.keras.Model: a Keras model for VGG/UTKFace
    """
    # Overrides input weight quantization if None
    if input_weight_quantization is None:
        input_weight_quantization = weight_quantization

    img_input = Input(shape=input_shape)

    x = conv_block(img_input,
                   filters=32,
                   kernel_size=(3, 3),
                   name='conv_0',
                   use_bias=False,
                   add_batchnorm=True,
                   add_activation=True)

    x = conv_block(x,
                   filters=32,
                   kernel_size=(3, 3),
                   name='conv_1',
                   padding='same',
                   pooling='max',
                   pool_size=2,
                   use_bias=False,
                   add_batchnorm=True,
                   add_activation=True)

    x = Dropout(0.3)(x)

    x = conv_block(x,
                   filters=64,
                   kernel_size=(3, 3),
                   padding='same',
                   name='conv_2',
                   use_bias=False,
                   add_batchnorm=True,
                   add_activation=True)

    x = conv_block(x,
                   filters=64,
                   kernel_size=(3, 3),
                   padding='same',
                   name='conv_3',
                   pooling='max',
                   pool_size=2,
                   use_bias=False,
                   add_batchnorm=True,
                   add_activation=True)

    x = Dropout(0.3)(x)

    x = conv_block(x,
                   filters=84,
                   kernel_size=(3, 3),
                   padding='same',
                   name='conv_4',
                   use_bias=False,
                   add_batchnorm=True,
                   add_activation=True)

    x = Dropout(0.3)(x)
    x = Flatten()(x)

    x = dense_block(x,
                    units=64,
                    name='dense_1',
                    use_bias=False,
                    add_batchnorm=True,
                    add_activation=True)

    x = dense_block(x, units=1, name='dense_2', add_activation=False)

    model = Model(img_input, x, name='vgg_utk_face')

    if ((weight_quantization != 0) or (activ_quantization != 0) or
        (input_weight_quantization != 0)):
        return quantize(model, weight_quantization, activ_quantization,
                        input_weight_quantization)
    return model


def vgg_utk_face_pretrained():
    """
    Helper method to retrieve a `vgg_utk_face` model that was trained on
    UTK Face dataset.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'vgg_utk_face_iq8_wq2_aq2.h5'
    file_hash = 'c5f7c722c19dd1f2f9743acd8d315b0ef51adb1f2dd42138b1e34c5f81782b96'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)
