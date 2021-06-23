# @Time     : 2021/6/2
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from asyncio import AbstractEventLoop
from .base import AbstractExecutor, CoroOrFunction, ArgsTypes, KwargsTypes, ReturnType, _get_event_loop
from .adapters import CoroutineAdapters
from ..validator.is_validators import is_coroutine, is_async_function, is_function


class CoroExecutor(AbstractExecutor):

    async def execute(self) -> ReturnType:
        return await self.coro_or_func


class CoroFunctionExecutor(AbstractExecutor):

    async def execute(self) -> ReturnType:
        args, kwargs = self._args, self._kwargs
        return await self.coro_or_func(*args, **kwargs)


class FunctionExecutor(AbstractExecutor):

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

    async def execute(self) -> ReturnType:
        # sync function to coroutine
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
                   func,
                   args: tuple,
                   kwargs: dict,
                   max_workers: int = None):
        adapter = CoroutineAdapters(loop, func, max_workers=max_workers)
        return adapter.to_coroutine(*args, **kwargs)


class Executor(AbstractExecutor):

    def __init__(self,
                 coro_or_func: CoroOrFunction,
                 args: ArgsTypes = None,
                 kwargs: KwargsTypes = None,
                 max_workers: int = None):
        super().__init__(coro_or_func, args, kwargs)
        self._coro_or_func = coro_or_func
        self._max_workers = max_workers

    @property
    def coro_or_func(self) -> CoroOrFunction:
        return self._coro_or_func

    @property
    def max_workers(self):
        return self._max_workers

    async def execute(self) -> ReturnType:
        coro_or_func = self.coro_or_func
        if is_coroutine(coro_or_func):
            return await self._use_coro_exec(coro_or_func)
        elif is_async_function(coro_or_func):
            return await self._use_coro_func_exec(coro_or_func)
        elif is_function(coro_or_func):
            return await self._use_func_exec(coro_or_func)
        else:
            raise ValueError(
                f"executed need Coroutine, Task, async function, or function, but got {type(coro_or_func).__name__}"
            )

    async def _use_coro_exec(self, coro_or_func: CoroOrFunction):
        executor = CoroExecutor(
            coro_or_func=coro_or_func,
            args=self._args,
            kwargs=self._kwargs
        )
        return await executor.execute()

    async def _use_coro_func_exec(self, coro_or_func: CoroOrFunction):
        executor = CoroFunctionExecutor(
            coro_or_func=coro_or_func,
            args=self._args,
            kwargs=self._kwargs
        )
        return await executor.execute()

    async def _use_func_exec(self, coro_or_func: CoroOrFunction):
        event_loop = _get_event_loop()
        executor = FunctionExecutor(
            event_loop,
            coro_or_func=coro_or_func,
            args=self._args,
            kwargs=self._kwargs,
            max_workers=self.max_workers
        )
        return await executor.execute()
