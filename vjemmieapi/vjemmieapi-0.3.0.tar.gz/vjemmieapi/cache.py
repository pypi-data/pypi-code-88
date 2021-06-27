import os

from typing import Coroutine, Any, Callable, Union
from mypy_extensions import VarArg, KwArg

from aiocache import Cache
from aiocache.serializers import PickleSerializer


def init_memcache() -> Cache:
    return Cache(
        Cache.MEMCACHED,
        endpoint="memcached",
        port=11211,
        namespace="main",
        serializer=PickleSerializer(),
    )


async def mock_func(*args, **kwargs) -> None:
    return None


class MockCache:
    def __getattr__(
        self, name: str
    ) -> Callable[[VarArg(Any), KwArg(Any)], Coroutine[Any, Any, None]]:
        return mock_func


CACHE_ENABLED = os.environ.get("CACHE_ENABLED", False)
cache: Union[Cache, MockCache] = init_memcache() if CACHE_ENABLED else MockCache()
