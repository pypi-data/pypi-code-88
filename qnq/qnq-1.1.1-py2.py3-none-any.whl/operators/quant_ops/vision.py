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
from torch.nn.modules.sparse import Embedding
from .quant_base import QuantBase


class QuantUpsample(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False

    def quantize_params(self):
        pass


class QuantEmbedding(QuantBase):
    def __init__(self, name, module, bit_width, writer):
        super().__init__(name, module, bit_width, writer)
        self.activation_positive = False


vision_switch = {nn.Upsample: QuantUpsample, nn.Embedding: QuantEmbedding}
