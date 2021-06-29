# This script contain util will help you, good luck!
# Author:
#     Albert Dongz
# History:
#     2020.4.17 First Release
# Dependencies:
#     PyTorch
# Attention:
#     1. Nothing

import os
import torch
import logging
import logging.config
import datetime
import torch.nn as nn
import yaml
from yaml.loader import SafeLoader


# https://www.cnblogs.com/qianyuliang/p/7234217.html
# https://stackoverflow.com/questions/17108973/python-logging-display-only-information-from-debug-level
# todo
# https://docs.python.org/zh-cn/3/library/logging.config.html#access-to-external-objects
def setup_logging(save_path="./checkpoints",
                  config_path=None,
                  env_key="LOG_CFG"):
    # get current time and create log dir
    now = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
    log_path = os.path.normpath(save_path + '/' + now)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # external config path
    if config_path is None:
        # get this file real abstract path
        module_path = os.path.dirname(os.path.realpath(__file__))
        # get default yaml file path
        config_path = os.path.join(module_path, "logging.yaml")
    path = config_path
    value = os.getenv(env_key, None)
    if value:
        path = value

    # load configuration
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.load(f, Loader=SafeLoader)
            # add log_path prefix
            # todo, make here more beauty
            config['handlers']['info_file_handler'][
                'filename'] = os.path.normpath(
                    log_path + '/' +
                    config['handlers']['info_file_handler']['filename'])
            config['handlers']['debug_file_handler'][
                'filename'] = os.path.normpath(
                    log_path + '/' +
                    config['handlers']['debug_file_handler']['filename'])
            config['handlers']['error_file_handler'][
                'filename'] = os.path.normpath(
                    log_path + '/' +
                    config['handlers']['error_file_handler']['filename'])
            logging.config.dictConfig(config)

    else:
        lognow(save_path)

    return log_path


# deprecated
def lognow(save_path="./checkpoints/"):
    """This function set up logging.

    Keyword Arguments:
        save_path {str} -- log save path (default: {"./checkpoints/"})

    Returns:
        str -- log absolute path, contain time and param path.
    """
    # get current time and create log dir
    now = datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S')
    log_path = os.path.normpath(save_path + '/' + now)
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    # setting up logging
    logger = logging.getLogger("qnq")
    logger.setLevel(level=logging.DEBUG)
    handler = logging.FileHandler(log_path + "/qnq.log")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s",
                                  "%H:%M:%S")
    handler.setFormatter(formatter)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(console)
    return logger, log_path


def float2fixed(data, bw, fl):
    """turn torch.Tensor to fixed Tensor.

    Args:
        data (torch.Tensor): torch.Tensor
        bw (int): bit width of quantization.
        fl (int): fraction length.

    Returns:
        torch.Tensor: fixed Tensor
    """
    unit = 2.0**(-fl)
    fixed_data = torch.clamp(torch.round(data / unit) * unit,
                             min=-2**(bw - 1 - fl) + unit,
                             max=+2**(bw - 1 - fl) - unit)
    return fixed_data


def bn2scale(module):
    """

    Args:
        module (nn.BatchNorm): Module need to be process
    """
    # 从未处理的module中获取bn层的四个参数
    weight = module.weight
    bias = module.bias
    try:
        mean = module.running_mean
    except:
        mean = 0
    try:
        var = module.running_var
    except:
        var = 1
    # 计算标准差，即sqrt(var) => std
    std = torch.sqrt(var)
    # 计算值
    new_weight = weight / std
    new_bias = bias - weight * mean / std
    new_mean = torch.zeros(mean.shape)
    new_var = torch.ones(var.shape)
    # 保存参数
    module.weight = nn.Parameter(new_weight)
    module.bias = nn.Parameter(new_bias)
    module.running_mean = new_mean
    module.running_var = new_var


def transfer_bn2scale(net):
    """Auto transfer BatchNorm to Scale

    Arguments:
        net {torch.nn.Module} -- net need be processed
        state {OrderDict} -- checkpoint of net

    Returns:
        net, state -- processed net and state
    """
    for name, module in net.named_modules():
        if isinstance(module, nn.BatchNorm2d):
            bn2scale(module)
    # todo
    net.cuda()


class DummyModule(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x


# Ref: https://zhuanlan.zhihu.com/p/49329030
# fuse Conv-BN & Deconv-BN
def fuse_module(m):
    def fuse(conv, bn):
        w = conv.weight
        mean = bn.running_mean
        var_sqrt = torch.sqrt(bn.running_var + bn.eps)

        beta = bn.weight
        gamma = bn.bias

        if conv.bias is not None:
            b = conv.bias
        else:
            b = mean.new_zeros(mean.shape)

        if isinstance(conv, nn.Conv2d):
            fused_conv = nn.Conv2d(conv.in_channels,
                                   conv.out_channels,
                                   conv.kernel_size,
                                   conv.stride,
                                   conv.padding,
                                   conv.dilation,
                                   conv.groups,
                                   bias=True,
                                   padding_mode=conv.padding_mode)
            w = w * (beta / var_sqrt).reshape([conv.out_channels, 1, 1, 1])
            b = (b - mean) / var_sqrt * beta + gamma
        else:
            fused_conv = nn.ConvTranspose2d(conv.in_channels,
                                            conv.out_channels,
                                            conv.kernel_size,
                                            conv.stride,
                                            conv.padding,
                                            conv.output_padding,
                                            conv.groups,
                                            bias=True,
                                            padding_mode=conv.padding_mode)
            w = w * (beta / var_sqrt).reshape([conv.out_channels, 1, 1])
            b = (b - mean) / var_sqrt * beta + gamma
        fused_conv.weight = nn.Parameter(w)
        fused_conv.bias = nn.Parameter(b)
        return fused_conv

    children = list(m.named_children())
    c = None
    cn = None

    for name, child in children:
        if isinstance(child, nn.BatchNorm2d):
            bc = fuse(c, child)
            m._modules[cn] = bc
            m._modules[name] = DummyModule()
            c = None
        elif isinstance(child, (nn.Conv2d, nn.ConvTranspose2d)):
            c = child
            cn = name
        else:
            fuse_module(child)


def fuse_convbn(model, conv_layer, bn_layer):
    conv = conv_layer.module
    bn = bn_layer.module

    # BN = bn_alpha * ( (x - bn_mean) / bn_std ) + bn_beta
    bn_mean = bn.running_mean
    bn_std = torch.sqrt(bn.running_var + bn.eps)
    bn_alpha = bn.weight
    bn_beta = bn.bias
    # Conv = conv_weight * x + conv_bias
    conv_weight = conv.weight
    conv_bias = conv.bias if conv.bias is not None else bn_mean.new_zeros(
        bn_mean.shape)

    # fused parameters
    fused_weight = conv_weight * (bn_alpha / bn_std).reshape(
        [conv.out_channels, 1, 1, 1])
    fused_bias = (conv_bias - bn_mean) / bn_std * bn_alpha + bn_beta

    # fuse
    fused_conv = nn.Conv2d(conv.in_channels,
                           conv.out_channels,
                           conv.kernel_size,
                           conv.stride,
                           conv.padding,
                           bias=True)
    fused_conv.weight = nn.Parameter(fused_weight)
    fused_conv.bias = nn.Parameter(fused_bias)

    model[conv_layer.name] = fused_conv
    model[bn_layer.name] = DummyModule()


def fuse_convbnrelu(model, conv_layer, bn_layer, relu_layer):
    # todo add relu
    conv = conv_layer.module
    bn = bn_layer.module

    # BN = bn_alpha * ( (x - bn_mean) / bn_std ) + bn_beta
    bn_mean = bn.running_mean
    bn_std = torch.sqrt(bn.running_var + bn.eps)
    bn_alpha = bn.weight
    bn_beta = bn.bias
    # Conv = conv_weight * x + conv_bias
    conv_weight = conv.weight
    conv_bias = conv.bias if conv.bias is not None else bn_mean.new_zeros(
        bn_mean.shape)

    # fused parameters
    fused_weight = conv_weight * (bn_alpha / bn_std).reshape(
        [conv.out_channels, 1, 1, 1])
    fused_bias = (conv_bias - bn_mean) / bn_std * bn_alpha + bn_beta

    # fuse
    fused_conv = nn.Conv2d(conv.in_channels,
                           conv.out_channels,
                           conv.kernel_size,
                           conv.stride,
                           conv.padding,
                           bias=True)
    fused_conv.weight = nn.Parameter(fused_weight)
    fused_conv.bias = nn.Parameter(fused_bias)

    model[conv_layer.name] = fused_conv
    model[bn_layer.name] = DummyModule()