#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2020/11/09 14:36:44'

import argparse


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


def str2list(v):
    if str(v).startswith('[') and str(v).endswith(']'):
        return eval(v)
    elif ',' in v:
        return v.split(',')
    elif ';' in v:
        return v.split(';')
    else:
        raise argparse.ArgumentTypeError('Unsupported value encountered.')


def str2dict(v):
    if str(v).startswith('{') and str(v).endswith('}'):
        return eval(v)
