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
from torch.nn.modules.activation import LeakyReLU, PReLU
from .quant_base import QuantBase


class QuantRelu(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = True
        self.weight_fl = -1

    def quantize_params(self):
        pass


class QuantLRelu(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False
        self.weight_fl = -1

    def quantize_params(self):
        pass


class QuantPRelu(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False
        self.weight_fl = -1

    def quantize_params(self):
        pass


class QuantLogSoftmax(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False
        self.weight_fl = -1

    def quantize_params(self):
        pass


activation_switch = {
    # nn.ReLU: QuantRelu,
    # nn.LeakyReLU: QuantLRelu,
    # nn.PReLU: QuantPRelu,
    nn.LogSoftmax:
    QuantLogSoftmax
}