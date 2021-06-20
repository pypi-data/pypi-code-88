import torch
import torch.nn.functional as F
import torchvision.models as m
from torch import nn
from einops import rearrange, reduce, asnumpy, parse_shape
from einops.layers.torch import Rearrange, Reduce


"""
This module contains all the new layers 
"""


def noop(x):
    """
    No operation

    """
    return x


def init_cnn(m):  #%t
    """
    Initialize a cnn with kaiming_normal_ or constant
    """
    if getattr(m, "bias", None) is not None:
        nn.init.constant_(m.bias, 0)
    if isinstance(m, (nn.Conv2d, nn.Linear)):
        nn.init.kaiming_normal_(m.weight)
    for l in m.children():
        init_cnn(l)


def init_default(m: nn.Module, func=nn.init.kaiming_normal_) -> nn.Module:  #%t
    "Initialize `m` weights with `func` and set `bias` to 0."
    if func:
        if hasattr(m, "weight"):
            func(m.weight)
        if hasattr(m, "bias") and hasattr(m.bias, "data"):
            m.bias.data.fill_(0.0)
    return m

def avgpoolflatten():  #%t
    """
    avgpool + Flatten for sequential
    """
    return nn.Sequential(Reduce("b c h w -> b c", "mean"))  # combine avg pool + view

class flatten(nn.Module):  #%t
    """
    Flatten
    """

    def forward(self, x):
        return x.view(x.size(0), -1)


class GeneralRelu(nn.Module):  #%t
    """
    General with leak or clipping if required
    """

    def __init__(self, leak=None, sub=None, maxv=None):
        super().__init__()
        self.leak, self.sub, self.maxv = leak, sub, maxv

    def forward(self, x):
        x = F.leaky_relu(x, self.leak) if self.leak is not None else F.relu(x)
        if self.sub is not None:
            x.sub_(self.sub)
        if self.maxv is not None:
            x.clamp_max_(self.maxv)
        return x


class AdaptiveConcatPool2d(nn.Module):  #%t
    """
    AdaptiveAvgPool2d + AdaptiveMaxPool2d

    """

    def __init__(self, sz=1):
        super().__init__()
        self.output_size = sz
        self.ap = nn.AdaptiveAvgPool2d(sz)
        self.mp = nn.AdaptiveMaxPool2d(sz)

    def forward(self, x):
        return torch.cat([self.mp(x), self.ap(x)], 1)

