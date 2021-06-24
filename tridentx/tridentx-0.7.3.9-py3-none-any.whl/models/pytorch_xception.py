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

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from collections import abc
from torch.nn import init
from torch.nn.parameter import Parameter
from trident.models.pretrained_utils import _make_recovery_model_include_top

from trident.backend.common import *
from trident.backend.model import *
from trident.backend.pytorch_backend import to_numpy, to_tensor, Layer, Sequential, fix_layer,load,get_device
from trident.backend.pytorch_ops import *
from trident.data.image_common import *
from trident.data.utils import download_model_from_google_drive
from trident.layers.pytorch_activations import get_activation, Identity, Relu, LeakyRelu
from trident.layers.pytorch_blocks import *
from trident.layers.pytorch_layers import *
from trident.layers.pytorch_normalizations import get_normalization
from trident.layers.pytorch_pooling import *
from trident.optims.pytorch_trainer import ImageClassificationModel
from trident.data.vision_transforms import Resize,Normalize


def EntryBlock():
    layers=OrderedDict()
    layers['conv1'] = Conv2d_Block((3, 3), 32, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch')
    layers['conv2']  = Conv2d_Block((3, 3), 64, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch')

    conv3_residual =Sequential(
        SeparableConv2d_Block((3,3),128,auto_pad=True,use_bias=False,activation=leaky_relu,normalization='batch'),
        SeparableConv2d_Block((3, 3), 128, auto_pad=True, use_bias=False, activation=None, normalization='batch'),
        MaxPool2d((3,3), strides=2, auto_pad=True),
    )

    conv3_direct =Conv2d_Block((1,1),128,strides=2,auto_pad=True,use_bias=False,activation=None,normalization='batch')
    layers['shorcut1'] =ShortCut2d(conv3_residual,conv3_direct,mode='add')

    conv4_residual = Sequential(
        LeakyRelu(),
        SeparableConv2d_Block((3,3), 256,auto_pad=True,use_bias=False,activation=leaky_relu,normalization='batch'),
        SeparableConv2d_Block((3, 3), 256, auto_pad=True, use_bias=False, activation=None, normalization='batch'),
        MaxPool2d((3,3), strides=2, auto_pad=True),
    )

    conv4_direct = Conv2d_Block((1,1),256,strides=2,auto_pad=True,use_bias=False,activation=None,normalization='batch')
    layers['shorcut2'] =ShortCut2d(conv4_residual,conv4_direct,mode='add')

    conv5_residual = Sequential(
        LeakyRelu(),
        SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch'),
        SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=None, normalization='batch'),
        MaxPool2d((3, 3), strides=2, auto_pad=True),
    )

    conv5_direct = Conv2d_Block((1, 1), 728, strides=2, auto_pad=True, use_bias=False, activation=None, normalization='batch')
    layers['shorcut3'] = ShortCut2d(conv5_residual, conv5_direct, mode='add')

    return Sequential(layers, name='entry_block')


def MiddleBlock(name='middle_block'):
    layers=OrderedDict()
    layers['conv1'] =SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch',sequence_rank='acn')
    layers['conv2']= SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch',sequence_rank='acn')
    layers['conv3']= SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch',sequence_rank='acn')
    return ShortCut2d(identity(),Sequential(layers),mode='add',name=name)


def ExitBlock():
    layers = OrderedDict()
    residual =Sequential(
            SeparableConv2d_Block((3, 3), 728, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch',sequence_rank='acn'),
            SeparableConv2d_Block((3, 3), 1024, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch',sequence_rank='acn'),
            MaxPool2d((3,3), strides=2,auto_pad=True))

    direct =Conv2d_Block((1, 1), 1024,strides=2, auto_pad=True, use_bias=False, activation=None, normalization='batch',sequence_rank='acn'),


    layers['shorcut1'] = ShortCut2d(residual, direct, mode='add')
    layers['conv'] =Sequential(
            SeparableConv2d_Block((3, 3), 1536, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch', sequence_rank='cna'),
            SeparableConv2d_Block((3, 3), 2048, auto_pad=True, use_bias=False, activation=leaky_relu, normalization='batch', sequence_rank='cna'),
        )
    layers['avgpool'] = AdaptiveAvgPool2d((1, 1))
    layers['dropout'] = Dropout(0.3)
    return Sequential(layers,name='exit_block')

def XceptionNet(num_middle_blocks=1,repeat=8,model_name='xception_net', include_top=True, num_classes=1000, **kwargs):
    return Sequential(
        EntryBlock(),
        For(range(num_middle_blocks), lambda i:
            Sequential(
                For(range(repeat), lambda j:
                    MiddleBlock()),name='middle_block{0}'.format(i))),
        ExitBlock(),
        Flatten(),
        Dense(num_classes),
        SoftMax(),
    name=model_name)

def XceptionNet41(include_top=True, pretrained=True,freeze_features=True, input_shape=( 3, 299, 299), classes=1000, **kwargs):
    if input_shape is not None and len(input_shape) == 3:
        input_shape = tuple(input_shape)
    else:
        input_shape = (3, 224, 224)
    effb0 = XceptionNet(num_middle_blocks=1,repeat=8,model_name='xception_net41', include_top=True, num_classes=1000)
    if pretrained == True:
        download_model_from_google_drive('1bxnoDerzoNfiZZLft4ocD3DAgx4v6aTN', dirname, 'efficientnet-b0.pth')
        recovery_model = fix_layer(load(os.path.join(dirname, 'efficientnet-b0.pth')))
        recovery_model = _make_recovery_model_include_top(recovery_model, include_top=include_top, classes=classes, freeze_features=freeze_features)
        effb0.model = recovery_model
    else:
        effb0.model = _make_recovery_model_include_top( effb0.model, include_top=include_top, classes=classes, freeze_features=True)

    effb0.model .input_shape = input_shape
    effb0.model .to(_device)
    return effb0




