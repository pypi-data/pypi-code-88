# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from abc import ABCMeta, abstractmethod

from f1z1_common import ArgsTypes, CoroOrFunction, KwargsTypes, ReturnType


class AbstractRunner(metaclass=ABCMeta):

    def __init__(self, coro_or_func: CoroOrFunction, args: ArgsTypes = None, kwargs: KwargsTypes = None):
        self._coro_or_func = coro_or_func
        self._args = () if not args else kwargs
        self._kwargs = {} if not kwargs else kwargs

    @property
    def coro_or_func(self):
        return self._coro_or_func

    @abstractmethod
    def run(self) -> ReturnType:
        raise NotImplementedError("NotImplemented .run() -> ReturnType")
