# @Time     : 2021/5/27
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from abc import ABCMeta, abstractmethod
from typing import Callable, List


class AbstractCallbackManager(metaclass=ABCMeta):

    def __init__(self):
        self._callbacks: List[Callable] = []

    @property
    def callbacks(self):
        return self._callbacks

    @property
    def length(self):
        return len(self.callbacks)

    def empty(self):
        return not self.length

    def add(self, function: Callable) -> int:
        self.check(function)
        if not self._is_exits(function):
            self.callbacks.append(function)
        return self.length

    def remove(self, function: Callable) -> int:
        if self.empty():
            return self.length
        idx = self._find(function)
        if idx > -1:
            self.callbacks.pop(idx)
        return self.length

    def to_list(self):
        if self.empty():
            return []
        return [cb for cb in self]

    def __add__(self, other):
        if self.is_callback_manager(other):
            self.callbacks.extend(other.callbacks)
        return self

    def __iter__(self):
        if not self.empty():
            for _, cb in enumerate(self.callbacks):
                yield cb

    @abstractmethod
    def check(self, value) -> bool:
        raise NotImplementedError("NotImplemented .check(value) -> bool")

    def is_callback_manager(self, value):
        return isinstance(value, AbstractCallbackManager)

    def _find(self, function):
        if not self._is_exits(function):
            return -1
        return self.callbacks.index(function)

    def _is_exits(self, function):
        if self.empty():
            return False
        return function in self.callbacks
