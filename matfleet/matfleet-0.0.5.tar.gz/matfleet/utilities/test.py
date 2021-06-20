#   coding:utf-8
#   This file is part of Alkemiems.
#
#   Alkemiems is free software: you can redistribute it and/or modify
#   it under the terms of the MIT License.

__author__ = 'Guanjie Wang'
__version__ = 1.0
__maintainer__ = 'Guanjie Wang'
__email__ = "gjwang@buaa.edu.cn"
__date__ = '2021/04/16 09:30:01'

from matfleet.utilities.mtype import recursive_basic_type

a = '{"1": "sfdsdfsd", "2": 52352}'
print(a, type(a))
a = recursive_basic_type(a)
print(a, type(a))
