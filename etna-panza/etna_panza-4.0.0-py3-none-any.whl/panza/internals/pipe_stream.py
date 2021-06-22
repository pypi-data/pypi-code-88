import asyncio
import time
from typing import AsyncIterator


class AsyncPipeStream:
    def __init__(self, stream: asyncio.StreamReader):
        self.stream = stream

    async def _iter_lines(self):
        async for line in self.stream:
            yield line.decode()

    async def _iter_lines_with_timeout(self, with_timeout: float):
        end_time = time.monotonic() + with_timeout
        while True:
            rem_time = end_time - time.monotonic()
            if rem_time <= 0:
                raise asyncio.TimeoutError
            line = await asyncio.wait_for(self.stream.readline(), rem_time)
            if not line:
                break
            yield line.decode()

    def iter_lines(self, with_timeout: float = None) -> AsyncIterator[str]:
        """
        Obtain a generator that reads the pipe's output line-by-line

        :param with_timeout:            the time (in seconds) to wait before bailing out

        :raise                          asyncio.TimeoutError
        """

        if with_timeout is None:
            return self._iter_lines()
        return self._iter_lines_with_timeout(with_timeout)
