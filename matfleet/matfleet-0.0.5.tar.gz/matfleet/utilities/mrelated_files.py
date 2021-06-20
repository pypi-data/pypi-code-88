#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/01/14 17:45:54'

import os
from pathlib import PurePath


def get_module_path(module):
    return os.path.dirname(module.__file__)


def judge_dir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return
        else:
            os.remove(path)
            os.mkdir(path)
    else:
        os.mkdir(path)


def get_now_allfiles(path: str, suffix: list=None):

    assert os.path.exists(path)
    final_pt = []
    for subfn in os.listdir(path):
        if PurePath(subfn).suffix.lower() in suffix:
            final_pt.append(os.path.join(path, subfn))
        else:
            pass

    return final_pt


def abs_file(filename):
    return os.path.abspath(os.path.join(os.getcwd(), filename))


def root_file(filename):
    return os.path.join(os.path.expanduser('~'), filename)
