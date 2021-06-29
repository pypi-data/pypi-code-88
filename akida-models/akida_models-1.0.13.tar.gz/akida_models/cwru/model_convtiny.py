#!/usr/bin/env python
# ******************************************************************************
# Copyright 2021 Brainchip Holdings Ltd.
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
Convtiny model definition for CWRU classification.
"""

from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Flatten, Softmax
from tensorflow.keras.utils import get_file

from cnn2snn import load_quantized_model

from ..layer_blocks import conv_block, dense_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/convtiny/'


def convtiny_cwru():
    """ Instanciates a CNN for CWRU classification with input shape (32, 32, 1)
    and 10 classes.

    Returns:
        tf.keras.Model: a Keras model for Convtiny/CWRU

    """
    img_input = Input(shape=(32, 32, 1))
    x = conv_block(img_input,
                   filters=32,
                   name='conv_1',
                   kernel_size=(7, 7),
                   padding='same',
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    x = conv_block(x,
                   filters=32,
                   name='conv_2',
                   kernel_size=(7, 7),
                   padding='same',
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    x = Flatten(name='flatten')(x)
    x = dense_block(x, units=64, name='dense_1', add_activation=True)
    x = dense_block(x, units=96, name='dense_2', add_activation=True)
    x = dense_block(x, units=10, name='predictions', add_activation=False)
    x = Softmax(name='act_softmax')(x)

    return Model(img_input, x, name='convtiny_cwru_32_10')


def convtiny_cwru_pretrained():
    """
    Helper method to retrieve a `convtiny_cwru` model that was trained on
    CWRU dataset.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'convtiny_cwru_iq8_wq2_aq4.h5'
    file_hash = '69705f8060a0da8dfde7bd88dab250a06cbcf4e923bba97b5e36132d5166b554'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)
