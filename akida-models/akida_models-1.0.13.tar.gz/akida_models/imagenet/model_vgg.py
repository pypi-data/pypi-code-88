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
VGG model definition for ImageNet classification.
"""

from tensorflow.keras import Model, regularizers
from tensorflow.keras.layers import Input, Activation, Dropout, Flatten
from tensorflow.keras.utils import get_file

from cnn2snn import quantize, load_quantized_model

from ..layer_blocks import conv_block, dense_block

BASE_WEIGHT_PATH = 'http://data.brainchip.com/models/vgg/'


def vgg_imagenet(input_shape=(224, 224, 3),
                 classes=1000,
                 include_top=True,
                 pooling=None,
                 weight_quantization=0,
                 activ_quantization=0,
                 input_weight_quantization=None):
    """Instantiates a VGG11 architecture with reduced number of filters in
    convolutional layers (i.e. a quarter of the filters of the original
    implementation of https://arxiv.org/pdf/1409.1556.pdf).

    Args:
        input_shape (tuple, optional): input shape tuple. Defaults to (224, 224,
            3).
        classes (int, optional): optional number of classes to classify images
            into. Defaults to 1000.
        include_top (bool, optional): whether to include the classification
            layers at the top of the model. Defaults to True.
        pooling (str, optional): Optional pooling mode for feature extraction
            when `include_top` is `False`. Defaults to None.

            * `None` means that the output of the model will be the 4D tensor
              output of the last convolutional block.
            * `avg` means that global average pooling will be applied to the
              output of the last convolutional block, and thus the output of the
              model will be a 2D tensor.
        weight_quantization (int, optional): sets all weights in the model to
            have a particular quantization bitwidth except for the weights in
            the first layer. Defaults to 0.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        activ_quantization (int, optional): sets all activations in the model to
            have a particular activation quantization bitwidth. Defaults to 0.

            * '0' implements floating point 32-bit activations.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.
        input_weight_quantization(int, optional): sets weight quantization in
            the first layer. Defaults to weight_quantization value.

            * '0' implements floating point 32-bit weights.
            * '2' through '8' implements n-bit weights where n is from 2-8 bits.

    Returns:
        tf.keras.Model: a Keras model for VGG/ImageNet

    """
    # check if overrides have been provided and override
    if input_weight_quantization is None:
        input_weight_quantization = weight_quantization

    # Define weight regularization
    weight_regularizer = regularizers.l2(4e-5)

    img_input = Input(shape=input_shape)

    # Block 1
    x = conv_block(img_input,
                   filters=16,
                   name='block1_conv1',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    # Block 2
    x = conv_block(x,
                   filters=32,
                   name='block2_conv1',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    # Block 3
    x = conv_block(x,
                   filters=64,
                   name='block3_conv1',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True)

    x = conv_block(x,
                   filters=64,
                   name='block3_conv2',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    # Block 4
    x = conv_block(x,
                   filters=128,
                   name='block4_conv1',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True)

    x = conv_block(x,
                   filters=128,
                   name='block4_conv2',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True,
                   pooling='max',
                   pool_size=(2, 2))

    # Block 5
    x = conv_block(x,
                   filters=128,
                   name='block5_conv1',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True)

    layer_pooling = 'global_avg' if pooling == 'avg' else 'max'
    x = conv_block(x,
                   filters=128,
                   name='block5_conv2',
                   kernel_size=(3, 3),
                   padding='same',
                   kernel_regularizer=weight_regularizer,
                   add_batchnorm=True,
                   add_activation=True,
                   pooling=layer_pooling,
                   pool_size=(2, 2))

    if include_top:
        # Classification block
        x = Flatten(name='flatten')(x)
        x = dense_block(x,
                        units=4096,
                        name='fc1',
                        add_batchnorm=True,
                        add_activation=True)
        x = Dropout(0.5, name='dropout_1')(x)
        x = dense_block(x,
                        units=4096,
                        name='fc2',
                        add_batchnorm=True,
                        add_activation=True)
        x = Dropout(0.5, name='dropout_2')(x)
        x = dense_block(x,
                        units=classes,
                        name='predictions',
                        add_batchnorm=False,
                        add_activation=False)

        act_function = 'softmax' if classes > 1 else 'sigmoid'
        x = Activation(act_function, name=f'act_{act_function}')(x)

    # Create model
    model = Model(img_input, x, name='vgg11_%s_%s' % (input_shape[0], classes))

    if ((weight_quantization != 0) or (activ_quantization != 0) or
        (input_weight_quantization != 0)):
        return quantize(model, weight_quantization, activ_quantization,
                        input_weight_quantization)
    return model


def vgg_imagenet_pretrained():
    """
    Helper method to retrieve a `vgg_imagenet` model that was trained on
    ImageNet dataset.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'vgg11_imagenet_224_iq8_wq4_aq4.h5'
    file_hash = 'e585de7ff31ff4e521b193d4eccd3c00896f9149dacea7ac17af8c0f9d361fb3'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)


def vgg_melanoma_pretrained():
    """
    Helper method to retrieve a `vgg_imagenet` model that was trained on
    SIIM-ISIC Melanoma Classification dataset.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'vgg11_melanoma_iq8_wq4_aq4.h5'
    file_hash = 'e44274cf287529ebb70290bd21b4fc83979929c4ac1247390a6f1ba040ddf260'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)


def vgg_odir5k_pretrained():
    """
    Helper method to retrieve a `vgg_imagenet` model that was trained on
    ODIR-5K dataset.

    The model focuses on the following classes that are a part of the original
    dataset: normal, cataract, AMD (age related macular degeneration) and
    pathological myopia.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'vgg11_odir5k_iq8_wq4_aq4.h5'
    file_hash = 'cb51a5dd2297141f9056d2ec0fbef9d10fbb75fd6f3b38358d8ce8c87f306abb'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)


def vgg_retinal_oct_pretrained():
    """
    Helper method to retrieve a `vgg_imagenet` model that was trained on
    retinal OCT dataset.

    Returns:
        tf.keras.Model: a Keras Model instance.

    """
    model_name = 'vgg11_retinal_oct_iq8_wq4_aq4.h5'
    file_hash = '6f013df344564190ca6d3278f70470f43456590c5059e7b584ac64193591b670'
    model_path = get_file(fname=model_name,
                          origin=BASE_WEIGHT_PATH + model_name,
                          file_hash=file_hash,
                          cache_subdir='models')
    return load_quantized_model(model_path)
