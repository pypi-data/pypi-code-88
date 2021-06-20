#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:43:56'


def encode(s):
    return ''.join([bin(ord(c)) for c in s])


def decode(s, etype='bin'):
    if etype == 'bin':
        sep = '0b'
    else:
        sep = ''
    return ''.join([chr(int(sep + i, 2)) for i in s.split(sep) if len(i) > 0])
