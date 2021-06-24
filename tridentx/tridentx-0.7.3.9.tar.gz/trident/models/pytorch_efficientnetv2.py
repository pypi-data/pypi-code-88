from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import inspect
import math
import os
import uuid
from collections import *
from collections import deque
from copy import copy, deepcopy
from functools import partial
from itertools import repeat
import builtins
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import abc
from torch.nn import init
from torch.nn.parameter import Parameter
from trident.data.vision_transforms import Resize,Normalize

from trident.models.pretrained_utils import _make_recovery_model_include_top
from trident.backend.common import *
from trident.backend.pytorch_backend import to_numpy, to_tensor, Layer, Sequential, fix_layer, get_device, load
from trident.data.image_common import *
from trident.data.utils import download_model_from_google_drive
from trident.layers.pytorch_activations import get_activation, Identity, Relu
from trident.backend.pytorch_ops import *
from trident.layers.pytorch_blocks import *
from trident.layers.pytorch_layers import *
from trident.layers.pytorch_normalizations import get_normalization, BatchNorm2d
from trident.layers.pytorch_pooling import *
from trident.optims.pytorch_trainer import *

__all__ = [ 'EfficientNetV2']

_session = get_session()


_epsilon = _session.epsilon
_trident_dir = _session.trident_dir

def _make_divisible(v, divisor=8, min_value=None):
    """
    This function is taken from the original tf repo.
    It ensures that all layers have a channel number that is divisible by 8
    It can be seen here:
    https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet/mobilenet.py
    :param v:
    :param divisor:
    :param min_value:
    :return:
    """
    if min_value is None:
        min_value = divisor
    new_v = max(min_value, int(v + divisor / 2) // divisor * divisor)
    # Make sure that round down does not go down by more than 10%.
    if new_v < 0.9 * v:
        new_v += divisor
    return new_v

def _se_make_divisible(v, rduction=4,divisor=8, min_value=None):
    return _make_divisible(v=v//rduction,divisor=divisor,min_value=min_value)

DEFAULT_BLOCKS_ARGS =   [
            # t, c, n, s, SE
            [1,  24,  2, 1, 0],
            [4,  48,  4, 2, 0],
            [4,  64,  4, 2, 0],
            [4, 128,  6, 2, 1],
            [6, 160,  9, 1, 1],
            [6, 272, 15, 2, 1],
        ]





def MBConv(oup, stride, expand_ratio, use_se):
        assert stride in [1, 2]
        if use_se:
            return Sequential(
                Conv2d_Block((1,1,), depth_multiplier=expand_ratio, strides=1, auto_pad=True, use_bias=False, normalization='batch', activation=silu),
                DepthwiseConv2d_Block((3,3),depth_multiplier=1,strides=stride,auto_pad=True,normalization='batch', activation=silu),
                SqueezeExcite(activation=silu,se_filters= _se_make_divisible,depth_multiplier=1),
                Conv2d_Block((1, 1,), num_filters=oup, strides=1, auto_pad=True, use_bias=False, normalization='batch', activation=None)
                )
        else:
            return Sequential(
                Conv2d_Block((3, 3), depth_multiplier=expand_ratio, strides=stride, auto_pad=True, normalization='batch', activation=silu),
                Conv2d_Block((1, 1,), num_filters=oup, strides=1, auto_pad=True, use_bias=False, normalization='batch', activation=None)
                )






dirname = os.path.join(_trident_dir, 'models')
if not os.path.exists(dirname):
    try:
        os.makedirs(dirname)
    except OSError:
        # Except permission denied and potential race conditions
        # in multi-threaded environments.
        pass





def EfficientNetV2(width_mult=1., input_shape=(3,224,224),model_name='efficientnet_v2', include_top=True, num_classes=1000, **kwargs):
    """Instantiates the EfficientNet architecture using given scaling coefficients.
        Optionally loads weights pre-trained on ImageNet.
        Note that the data format convention used by the model is
        the one specified in your Keras config at `~/.keras/keras.json`.
    Args
        width_coefficient: float, scaling coefficient for network width.
        depth_coefficient: float, scaling coefficient for network depth.
        default_size: integer, default input image size.
        dropout_rate: float, dropout rate before final classifier layer.
        drop_connect_rate: float, dropout rate at skip connections.
        depth_divisor: integer, a unit of network width.
        activation_fn: activation function.
        blocks_args: list of dicts, parameters to construct block modules.
        model_name: string, model name.
        include_top: whether to include the fully-connected
            layer at the top of the network.

        input_tensor: optional Keras tensor
            (i.e. output of `layers.Input()`)
            to use as image input for the model.
        input_shape: optional shape tuple, only to be specified
            if `include_top` is False.
            It should have exactly 3 inputs channels.

        num-classes: optional number of classes to classify images
            into, only to be specified if `include_top` is True, and
            if no `weights` argument is specified.
    Returns
        A Efficientnet model instance.


    """
    default_block_args = deepcopy(DEFAULT_BLOCKS_ARGS)

    def _initialize_weights(net):
        for m in net.modules():
            if isinstance(m, Conv2d):
                n = m.kernel_size[0] * m.kernel_size[1] * m.num_filters
                m.weight.data.normal_(0, math.sqrt(2. / n))
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, Dense):
                m.weight.data.normal_(0, 0.001)
                m.bias.data.zero_()

    input_channel = _make_divisible(24 * width_mult, 8)
    layers = [Conv2d_Block((3,3),num_filters=input_channel,strides=2,normalization='batch',activation=silu)]
    # building inverted residual blocks

    for t, c, n, s, use_se in default_block_args:
        output_channel = _make_divisible(c * width_mult, 8)
        for i in range(n):
            layers.append(MBConv(output_channel, s if i == 0 else 1, t, use_se))
    layerdict=OrderedDict()
    layerdict['features']=Sequential(*layers)

    # building last several layers
    output_channel = _make_divisible(1792 * width_mult, 8) if width_mult > 1.0 else 1792
    layerdict['conv']=Conv2d_Block((1,1),num_filters=output_channel,normalization='batch',activation=silu)
    layerdict['avgpool'] =AdaptiveAvgPool2d((1, 1))
    layerdict['flatten'] = Flatten()
    layerdict['classifier'] =Dense(num_classes,activation=SoftMax())
    model=ImageClassificationModel(input_shape=input_shape,output=Sequential(layerdict))
    #_initialize_weights(model.model)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenet_labels1.txt'), 'r',
              encoding='utf-8-sig') as f:
        labels = [l.rstrip() for l in f]
        model.class_names = labels
    model.preprocess_flow = [Resize((224,224), keep_aspect=True), Normalize(0, 255),
                             Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])]

    return model


# def EfficientNetV2S(include_top=True, pretrained=True,freeze_features=True, input_shape=(3, 224, 224), classes=1000, **kwargs):
#     if input_shape is not None and len(input_shape) == 3:
#         input_shape = tuple(input_shape)
#     else:
#         input_shape = (3, 224, 224)
#     effb0 = EfficientNet(1.0, 1.0, input_shape, 0.2, model_name='efficientnet-b0', include_top=include_top,
#                          num_classes=classes)
#     if pretrained :
#         download_model_from_google_drive('1bxnoDerzoNfiZZLft4ocD3DAgx4v6aTN', dirname, 'efficientnet-b0.pth')
#         recovery_model = fix_layer(load(os.path.join(dirname, 'efficientnet-b0.pth')))
#         recovery_model = _make_recovery_model_include_top(recovery_model,input_shape=input_shape, include_top=include_top, classes=classes, freeze_features=freeze_features)
#         effb0.model = recovery_model
#     else:
#         effb0.model = _make_recovery_model_include_top( effb0.model, include_top=include_top, classes=classes, freeze_features=True)
#
#     effb0.model .input_shape = input_shape
#     effb0.model .to(get_device())
#     return effb0
#
