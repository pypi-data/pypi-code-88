# @Time     : 2021/6/2
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from asyncio import AbstractEventLoop
from .base import AbstractTaskFactory, ArgsTypes, CoroOrFunction, KwargsTypes, _get_event_loop
from .adapters import CoroutineAdapters
from ..validator.is_validators import is_coroutine, is_async_function, is_function


class CoroTaskFactory(AbstractTaskFactory):

    def create_task(self):
        return self._create_by_coro(self.coro_or_func)


class CoroFunctionTaskFactory(AbstractTaskFactory):

    def create_task(self):
        """
        async function to task

        :return:
        """
        return self._create_by_coro(self._run_in_async_ctx())

    async def _run_in_async_ctx(self):
        """
        async function must be async context
        :return:
        """
        args, kwargs = self._args, self._kwargs
        return await self.coro_or_func(*args, **kwargs)


class FunctionTaskFactory(AbstractTaskFactory):

    def __init__(self,
                 loop: AbstractEventLoop,
                 *,
                 coro_or_func: CoroOrFunction,
                 args: ArgsTypes = None,
                 kwargs: KwargsTypes = None,
                 max_workers: int = None):
        super().__init__(coro_or_func, args, kwargs)
        self._eloop = loop
        self._max_workers = max_workers

    @property
    def eloop(self):
        return self._eloop

    def create_task(self):
        """
        function to task
        :return:
        """
        return self._create_by_coro(self._run_in_async_ctx())

    async def _run_in_async_ctx(self):
        fut = self._to_future(
            self.eloop,
            func=self.coro_or_func,
            args=self._args,
            kwargs=self._kwargs,
            max_workers=self._max_workers
        )
        return await fut

    def _to_future(self,
                   loop: AbstractEventLoop,
                   *,
                   func: CoroOrFunction,
                   args: tuple,
                   kwargs: dict,
                   max_workers: int = None):
        adapter = CoroutineAdapters(loop, func, max_workers=max_workers)
        return adapter.to_coroutine(*args, **kwargs)


class TaskFactory(AbstractTaskFactory):

    def __init__(self,
                 coro_or_func: CoroOrFunction,
                 args: ArgsTypes = None,
                 kwargs: KwargsTypes = None,
                 max_workers: int = None):
        super().__init__(coro_or_func, args, kwargs)
        self._max_workers = max_workers

    def create_task(self):
        coro_or_func = self.coro_or_func
        if is_coroutine(coro_or_func):
            return self._use_coro_factory(coro_or_func)
        elif is_async_function(coro_or_func):
            return self._use_async_factory(coro_or_func)
        elif is_function(coro_or_func):
            return self._use_func_factory(coro_or_func)
        else:
            raise ValueError(
                f"coro_or_func need a Coroutine, async function or function, but got {type(coro_or_func).__name__}"
            )

    def _use_coro_factory(self, coro_or_func: CoroOrFunction):
        args, kwargs = self._args, self._kwargs
        coro = CoroTaskFactory(coro_or_func, args, kwargs)
        return coro.create_task()

    def _use_async_factory(self, coro_or_func: CoroOrFunction):
        args, kwargs = self._args, self._kwargs
        async_func = CoroFunctionTaskFactory(coro_or_func, args, kwargs)
        return async_func.create_task()

    def _use_func_factory(self, coro_or_func: CoroOrFunction):
        event_loop = _get_event_loop()
        func = FunctionTaskFactory(
            event_loop,
            coro_or_func=coro_or_func,
            args=self._args, kwargs=self._kwargs,
            max_workers=self._max_workers
        )
        return func.create_task()
