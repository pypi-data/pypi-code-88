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
import numpy as np
from .quant_base import QuantBase
from ..qnq_ops import *


class QuantTorchFuncGeneral(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False
        self.weight_fl = -1

    def quantize_params(self):
        pass


torchfunc_switch = {
    TorchAdd: QuantTorchFuncGeneral,
    TorchSum: QuantTorchFuncGeneral,
    TorchMinus: QuantTorchFuncGeneral,
    TorchMatMul: QuantTorchFuncGeneral,
    TorchDotMul: QuantTorchFuncGeneral,
    TorchDiv: QuantTorchFuncGeneral,
    TorchSqrt: QuantTorchFuncGeneral,
    TorchSin: QuantTorchFuncGeneral,
    TorchCos: QuantTorchFuncGeneral,
    TorchSoftmax: QuantTorchFuncGeneral,
    TorchSigmoid: QuantTorchFuncGeneral,
    TorchExp: QuantTorchFuncGeneral,
    TorchTanh: QuantTorchFuncGeneral,
    TorchTemplate: QuantTorchFuncGeneral,
    TorchDummy: QuantTorchFuncGeneral,
    TorchBmm: QuantTorchFuncGeneral
}