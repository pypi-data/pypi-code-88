#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2020/12/06 10:06:47'

import pydoc


def write_help_func_to_file(cc, outputfn, mode='w'):
    with open(outputfn, mode) as f:
        pydoc.doc(cc, output=f)
