# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from enum import Enum


def is_enum(value):
    return isinstance(value, Enum)


def is_enum_subclass(klass):
    return issubclass(klass, Enum)
