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


class QNQInput(nn.Module):
    def __init__(self):
        super(QNQInput, self).__init__()

    def forward(self, x):
        return x