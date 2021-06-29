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


class TorchAdd(nn.Module):
    def __init__(self):
        super(TorchAdd, self).__init__()

    def forward(self, x, y):
        return x + y


class TorchSum(nn.Module):
    def __init__(self):
        super(TorchSum, self).__init__()

    def forward(self, *args, **kwargs):
        return torch.sum(*args, **kwargs)


class TorchMinus(nn.Module):
    def __init__(self):
        super(TorchMinus, self).__init__()

    def forward(self, x, y):
        return x - y


class TorchMatMul(nn.Module):
    def __init__(self):
        super(TorchMatMul, self).__init__()

    def forward(self, x, y):
        return torch.matmul(x, y)


class TorchDotMul(nn.Module):
    def __init__(self):
        super(TorchDotMul, self).__init__()

    def forward(self, x, y):
        return x * y


class TorchDiv(nn.Module):
    def __init__(self):
        super(TorchDiv, self).__init__()

    def forward(self, x, y):
        return x / y


class TorchSqrt(nn.Module):
    def __init__(self):
        super(TorchSqrt, self).__init__()

    def forward(self, x):
        return torch.sqrt(x)


class TorchSin(nn.Module):
    def __init__(self):
        super(TorchSin, self).__init__()

    def forward(self, x):
        return torch.sin(x)


class TorchCos(nn.Module):
    def __init__(self):
        super(TorchCos, self).__init__()

    def forward(self, x):
        return torch.cos(x)


class TorchSoftmax(nn.Module):
    def __init__(self):
        super(TorchSoftmax, self).__init__()

    def forward(self, *args, **kwargs):
        return torch.softmax(*args, **kwargs)


class TorchSigmoid(nn.Module):
    def __init__(self):
        super(TorchSigmoid, self).__init__()

    def forward(self, x):
        return torch.sigmoid(x)


class TorchExp(nn.Module):
    def __init__(self):
        super(TorchExp, self).__init__()

    def forward(self, x):
        return torch.exp(x)


class TorchTanh(nn.Module):
    def __init__(self):
        super(TorchTanh, self).__init__()

    def forward(self, x):
        return torch.tanh(x)


class TorchTemplate(nn.Module):
    def __init__(self, func):
        super(TorchTemplate, self).__init__()
        self.func = func

    def forward(self, *args):
        return self.func(*args)


class TorchDummy(nn.Module):
    """TorchDummy collect activation from different input and quantize these use unified fl choice.

    Args:
        x (any): You can use any algorithm but a single function,
        eg: 'a + b' or 'a * b' or just a single variable 'a',
        but not 'a * (b + c)', that's because (b + c) in later need be quantized too.
    """
    def __init__(self):
        super(TorchDummy, self).__init__()

    def forward(self, x):
        return x


class TorchCat(nn.Module):
    def __init__(self, *layers):
        super(TorchCat, self).__init__()
        self.layers = layers

    def forward(self, *args):
        return torch.cat(*args)


class ConcatSign(nn.Module):
    def __init__(self, modules=[]):
        super(ConcatSign, self).__init__()
        self.modules = modules

    def forward(self):
        pass

class TorchBmm(nn.Module):
    def __init__(self):
        super(TorchBmm, self).__init__()

    def forward(self, x):
        return torch.bmm(x)


# global var
TorchFuncTuple = (TorchAdd, TorchSum, TorchMinus, TorchMatMul, TorchDotMul,
                  TorchDiv, TorchSqrt, TorchSin, TorchCos, TorchSoftmax,
                  TorchSigmoid, TorchExp, TorchTanh, TorchTemplate, TorchDummy, TorchBmm)
