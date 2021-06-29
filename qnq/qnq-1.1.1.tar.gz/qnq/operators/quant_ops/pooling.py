# This script contain implentation of operators.
# Author:
#     Albert Dongz
# History:
#     2020.7.16 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing
import torch.nn as nn
from torch.nn.modules.pooling import AdaptiveAvgPool1d
from .quant_base import QuantBase


class QuantMaxPool(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False

    def quantize_params(self):
        pass


class QuantAveragePool(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False

    def quantize_params(self):
        pass


class QuantAdaptiveAvgPool(QuantBase):
    def __init__(self, name, module, bit_width, is_debug=False):
        super().__init__(name, module, bit_width, is_debug)
        self.activation_positive = False

    def quantize_params(self):
        pass


pooling_switch = {
    # nn.MaxPool1d: QuantMaxPool,
    # nn.MaxPool2d: QuantMaxPool,
    # nn.MaxPool3d: QuantMaxPool,
    nn.AvgPool1d:
    QuantAveragePool,
    nn.AvgPool2d:
    QuantAveragePool,
    nn.AvgPool3d:
    QuantAveragePool,
    nn.AdaptiveAvgPool1d:
    QuantAdaptiveAvgPool,
    nn.AdaptiveAvgPool2d:
    QuantAdaptiveAvgPool,
    nn.AdaptiveAvgPool3d:
    QuantAdaptiveAvgPool,
}