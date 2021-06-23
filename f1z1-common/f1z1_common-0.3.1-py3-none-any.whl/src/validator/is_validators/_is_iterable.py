# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from collections.abc import Iterable


def is_iterable(value):
    return isinstance(value, Iterable)
