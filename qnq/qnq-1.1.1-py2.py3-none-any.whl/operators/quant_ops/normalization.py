# This script contain implentation of operators.
# Author:
#     Albert Dongz
# History:
#     2020.7.16 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing
import torch
import torch.nn as nn
import numpy as np
from torch.nn.modules import normalization
from .quant_base import *


class QuantBatchNorm(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False


class QuantLayerNorm(QuantBase):
    def __init__(self, name, module, bit_width, is_debug):
        super().__init__(name, module, bit_width, is_debug)


normalization_switch = {
    nn.BatchNorm1d: QuantBatchNorm,
    nn.BatchNorm2d: QuantBatchNorm,
    nn.BatchNorm3d: QuantBatchNorm,
    nn.LayerNorm: QuantLayerNorm
}