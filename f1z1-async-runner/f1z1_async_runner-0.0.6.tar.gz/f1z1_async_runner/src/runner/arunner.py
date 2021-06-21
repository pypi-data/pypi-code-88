# @Time     : 2021/6/1
# @Project  : f1z1-g
# @IDE      : PyCharm
# @Author   : Angel
# @Email    : 376355670@qq.com
from asyncio import run

from f1z1_common import Executor

from .base import AbstractRunner


class AsyncRunner(AbstractRunner):

    def __init__(self,
                 coro_or_func,
                 args=None,
                 kwargs=None,
                 max_workers: int = None):
        super().__init__(coro_or_func, args, kwargs)
        self._max_workers = max_workers

    def run(self):
        return run(self.main())

    async def main(self):
        executor = Executor(
            coro_or_func=self.coro_or_func,
            args=self._args,
            kwargs=self._kwargs,
            max_workers=self._max_workers
        )
        return await executor.execute()
