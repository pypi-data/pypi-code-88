import os
import random

import hiddenlayer as hl
import matplotlib.pyplot as plt
import numpy as np
import PIL
import torch
import torchvision
from prettytable import PrettyTable
from torch import nn

"""
This module contains all the new add ons for torch
"""

torch.Tensor.ndim = property(lambda x: len(x.shape))

def get_hist(h):
    """
    grab histogram
    """
    return torch.stack(h.stats[2]).t().float().log1p()


def get_min(h):
    """
    Grab min values from histogram
    """
    h1 = torch.stack(h.stats[2]).t().float()
    return h1[19:22].sum(0) / h1.sum(0)


def find_modules(m, cond):  #%t
    """
    Return modules with a condition
    """
    if cond(m):
        return [m]
    return sum([find_modules(o, cond) for o in m.children()], [])


def is_lin_layer(l):  #%t
    """
    Check if linear
    """
    lin_layers = (nn.Conv1d, nn.Conv2d, nn.Conv3d, nn.Linear, nn.ReLU)
    return isinstance(l, lin_layers)


def clear_memory():  #%t
    """
    Clear GPU cache
    """
    torch.cuda.empty_cache()


def seed_everything(seed=42):  #%t
    """
    Seed everything with a number
    """
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


class FreezeUnfreeze:
    """
    Main freeze or unfreeze class

    """

    def __init__(self, model, switch, to=None):
        self.model = model
        self.switch = switch  # 0 for freeze, 1 for unfreeze
        self.ps = [None for x in self.model.parameters()]
        self.count = 0
        self.to = to

    def runner(self):
        if self.to == None:
            self.to = len(self.ps)
        if self.to < 0:
            self.to = len(self.ps) - abs(self.to)
        for param in self.model.parameters():
            if self.count < self.to:
                param.requires_grad = False if self.switch == 0 else True
                self.count += 1


def freeze_to(model, to=None):  #%t
    """
    Freeze upto a layer

    """
    FreezeUnfreeze(model, 0, to).runner()


def unfreeze_to(model, to=None):  #%t
    """
    Unfreeze to a layer

    """
    FreezeUnfreeze(model, 1, to).runner()


def count_parameters(model, show_table=False):  #%t
    """
    Count number of parameters and show table

    """
    table = PrettyTable(["Modules", "Parameters"])
    total_params = 0
    for name, parameter in model.named_parameters():
        if not parameter.requires_grad:
            continue
        param = parameter.numel()
        table.add_row([name, param])
        total_params += param

    print(f"Total Trainable Params: {total_params}")
    if show_table == True:
        print(table)
    return total_params


def param_state(x):
    """
    Return state of a single param

    """
    return x.requires_grad


def total_layer_state(model):  #%t
    """
    Get number of frozen, unfrozen and total layers

    """
    ps = [param_state(x) for x in model.parameters()]
    frozen = ps.count(False)
    return f"Frozen: {frozen}, Not: {len(ps)-frozen}, Total: {len(ps)}"


def open_image(fpath, size, convert_to="", to_tensor=False, perm=()):  #%t
    """
    Open image

    """
    tem = PIL.Image.open(fpath).resize(size)
    if len(convert_to) > 1:
        tem = tem.convert(convert_to)
    if to_tensor == True:
        tem = pil_to_tensor(tem)
    if len(perm) > 2:
        tem = tem.permute(*perm)

    return tem


def pil_from_tensor(x):  #%t
    """
    Convert to tensor from pil

    """
    return torchvision.transforms.functional.to_pil_image(x)


def pil_to_tensor(x):  #%t
    """
    Convert to pil from tensor

    """
    return torchvision.transforms.functional.to_tensor(x)


def visualize_model(model, inp_size=[1, 3, 64, 64], device="cuda:0"):  #%t
    """
    Use hiddenlayer to visualize a model
    """
    model = model.to(device)
    model.eval()
    graph = hl.build_graph(model, torch.zeros(inp_size).to(device))
    return graph
