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
from torch.nn.modules.conv import ConvTranspose1d
from .quant_base import QuantBase


# support dilation convolution
class QuantConv(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False


class QuantConvTranspose(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False


convolution_switch = {
    nn.Conv1d: QuantConv,
    nn.Conv2d: QuantConv,
    nn.Conv3d: QuantConv,
    nn.ConvTranspose1d: QuantConvTranspose,
    nn.ConvTranspose2d: QuantConvTranspose,
    nn.ConvTranspose3d: QuantConvTranspose
}