# @Time     : 2021/6/2
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from abc import ABCMeta, abstractmethod
from asyncio import Task, create_task, get_event_loop
from typing import Callable, Coroutine, Dict, TypeVar, Tuple, Union

from ..validator.is_validators import is_coroutine

ArgsTypes = Union[Tuple, None]
KwargsTypes = Union[Dict, None]
CoroOrFunction = Union[Callable, Coroutine]
ReturnType = TypeVar("ReturnType")


class ICoroutineAdapters(object):
    """
    coroutine adapters
    """

    def to_coroutine(self, *args, **kwargs) -> Coroutine:
        raise NotImplementedError("NotImplemented .to_coroutine(*args, **kwargs) -> Coroutine")


class AbstractExecutor(metaclass=ABCMeta):

    def __init__(self,
                 coro_or_func: CoroOrFunction,
                 args: ArgsTypes = None,
                 kwargs: KwargsTypes = None):
        self._coro_or_func = coro_or_func
        self._args = () if not args else args
        self._kwargs = {} if not kwargs else kwargs

    @property
    def coro_or_func(self) -> CoroOrFunction:
        return self._coro_or_func

    @abstractmethod
    async def execute(self) -> ReturnType:
        raise NotImplementedError("NotImplemented .execute(*args, **kwargs) -> ReturnType")


class AbstractTaskFactory(metaclass=ABCMeta):

    def __init__(self, coro_or_func: CoroOrFunction, args: ArgsTypes = None, kwargs: KwargsTypes = None):
        self._coro_or_func = coro_or_func
        self._args = () if not args else args
        self._kwargs = {} if not kwargs else kwargs

    @property
    def coro_or_func(self) -> CoroOrFunction:
        return self._coro_or_func

    @abstractmethod
    def create_task(self) -> Task:
        raise NotImplementedError("NotImplemented .create_task() -> Task")

    def _create_by_coro(self, coro):
        if not is_coroutine(coro):
            raise ValueError(
                f"coro need Coroutine, but got {type(coro).__name__}"
            )
        return create_task(coro)


class IAsyncTask(object):
    """
    task interface
    """

    @property
    def coro_or_func(self) -> CoroOrFunction:
        raise NotImplementedError("NotImplemented .coro_or_func -> CoroOrFunction")

    def create_task(self, *args, **kwargs) -> Task:
        raise NotImplementedError("NotImplemented .create_task(*args, **kwargs) -> Task")


def _get_event_loop():
    return get_event_loop()
