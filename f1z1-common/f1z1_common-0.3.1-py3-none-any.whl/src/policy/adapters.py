# @Time     : 2021/6/2
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from asyncio import AbstractEventLoop, get_event_loop
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from typing import Callable

from .base import ICoroutineAdapters


class CoroutineAdapters(ICoroutineAdapters):
    """
    function to coroutine
    """

    def __init__(self,
                 loop: AbstractEventLoop,
                 func: Callable,
                 *, max_workers: int = None):
        self._eloop = loop
        self._func = func
        self._executor = ThreadPoolExecutor(max_workers=max_workers)

    @property
    def func(self):
        return self._func

    @property
    def executor(self):
        return self._executor

    def to_coroutine(self, *args, **kwargs):
        function = self._get_function(**kwargs)
        return self._create_future(function, *args)

    def _create_future(self, sync, *args):
        event_loop = self._get_event_loop()
        fut = event_loop.run_in_executor(self.executor, sync, *args)
        return fut

    def _get_function(self, **kwargs):
        return partial(self.func, **kwargs)

    def _get_event_loop(self):
        if self._eloop is None:
            return get_event_loop()
        return self._eloop
