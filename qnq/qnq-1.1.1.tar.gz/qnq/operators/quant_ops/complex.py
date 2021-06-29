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

from ..qnq_ops import *
from .quant_base import *


class QuantInput(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.weight_fl = -1
        self.activation_positive = False

    def quantize_params(self):
        pass


class QuantYOLO(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.weight_fl = -1

    def quantize_params(self):
        pass


complex_switch = {QNQYOLO: QuantYOLO, QNQInput: QuantInput}
