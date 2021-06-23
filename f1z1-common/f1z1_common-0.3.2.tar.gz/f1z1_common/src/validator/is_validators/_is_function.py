# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from asyncio import iscoroutine, iscoroutinefunction
from collections.abc import Callable


def is_coroutine(value):
    return iscoroutine(value)


def is_function(value):
    return isinstance(value, Callable)


def is_async_function(value):
    return all([
        is_function(value),
        iscoroutinefunction(value)
    ])
