from enum import Enum, auto
from functools import wraps, lru_cache
from typing import *

from async_lru import alru_cache

from .async_cached_iterable import *
from .cached_iterable import *
from .helpers import *

class IteratorType(Enum):
    """
    Defines an iterator type to be wrapped with this module.
    """
    
    Simple = auto()
    """ All iterators those match signature `Iterator[T]` """
    
    AwaitableIter = auto()
    """ All iterators those match signature `Awaitable[Iterator[T]]` """
    
    AsyncIter = auto()
    """ All iterators those match signature `AsyncIterator[T]` """

Args = TypeVar('Args')
T = TypeVar('T')
F = TypeVar('F', bound=Callable)

#region Iterator Wrappers
def wrap_iter(func: Callable[[Args], Iterator[T]]) -> Callable[[Args], CachedIterable[T]]:
    # print(f"Decorator: wrap_iter({func})")
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> CachedIterable[T]:
        result = func(*args, **kwargs)
        return CachedIterable(result)
    
    return wrapper

def wrap_awaitable_iter(func: Callable[[Args], Awaitable[Iterator[T]]]) -> Callable[[Args], Awaitable[CachedIterable[T]]]:
    # print(f"Decorator: wrap_iter_awaitable({func})")
    
    @wraps(func)
    async def wrapper(*args, **kwargs) -> CachedIterable[T]:
        result = await func(*args, **kwargs)
        return CachedIterable(result)
    
    return wrapper

def wrap_async_iter(func: Callable[[Args], AsyncIterator[T]]) -> Callable[[Args], AsyncCachedIterable[T]]:
    # print(f"Decorator: wrap_async_iter({func})")
    
    @wraps(func)
    def wrapper(*args, **kwargs) -> AsyncCachedIterable[T]:
        result = func(*args, **kwargs)
        return AsyncCachedIterable(result)
    
    return wrapper

_WRAPPERS = \
{
    IteratorType.Simple: wrap_iter,
    IteratorType.AwaitableIter: wrap_awaitable_iter,
    IteratorType.AsyncIter: wrap_async_iter,
}
#endregion

#region Reversed Wrappers
def unwrap_iter(wrapped_func: Callable[[Args], Iterable[T]]) -> Callable[[Args], Iterator[T]]:
    # print(f"Decorator: unwrap_iter({wrapped_func})")
    
    @wraps(wrapped_func)
    def wrapper(*args, **kwargs) -> Iterator[T]:
        result = wrapped_func(*args, **kwargs)
        # print(f"Wrapper: unwrapping func {wrapped_func}")
        return iter(result)
    
    return wrapper

def unwrap_awaitable_iter(wrapped_func: Callable[[Args], Awaitable[Iterable[T]]]) -> Callable[[Args], Awaitable[Iterator[T]]]:
    # print(f"Decorator: unwrap_iter_awaitable({wrapped_func})")
    
    @wraps(wrapped_func)
    async def wrapper(*args, **kwargs) -> Iterator[T]:
        result = await wrapped_func(*args, **kwargs)
        return iter(result)
    
    return wrapper

def unwrap_async_iter(wrapped_func: Callable[[Args], AsyncIterable[T]]) -> Callable[[Args], AsyncIterator[T]]:
    # print(f"Decorator: unwrap_async_iter({wrapped_func})")
    
    @wraps(wrapped_func)
    def wrapper(*args, **kwargs) -> AsyncIterator[T]:
        result = wrapped_func(*args, **kwargs)
        # print(f"Wrapper: unwrapping func {wrapped_func}")
        return result.__aiter__()
    
    return wrapper

_UNWRAPPERS = \
{
    IteratorType.Simple: unwrap_iter,
    IteratorType.AwaitableIter: unwrap_awaitable_iter,
    IteratorType.AsyncIter: unwrap_async_iter,
}
#endregion

@smart_decorator
def iter_cache(cache_engine: Callable[[F], F] = simple_cache, iterator_type: IteratorType = IteratorType.Simple):
    """
    Constructs a decorator for the give iterator type (of function return)
    using the given cache engine (simple infinite cache by default).
    
    Args:
        cache_engine: A constructed decorator which implements caching. Default: `simple_cache`
        iterator_type: `IteratorType`. A type of iterator to be wrapped. Default: `IteratorType.Simple`
    
    Returns:
        Returns the decorated function which combines iterator wrapping, caching, and unwrapping.
    """
    
    # print(f"Decorator (external): iter_cache(cache_engine: {cache_engine}, iterator_type: {iterator_type})")
    
    def decorator(func: Callable[[Args], T]) -> Callable[[Args], T]:
        # print(f"Decorator (internal): iter_cache(cache_engine: {cache_engine}, iterator_type: {iterator_type})({func})")
        unwrap_engine =_UNWRAPPERS[iterator_type]
        wrap_engine = _WRAPPERS[iterator_type]
        
        decorations = [ wrap_engine, cache_engine, unwrap_engine ]
        for d in decorations:
            func = d(func)
        
        return func
    
    return decorator

@smart_decorator
def lru_iter_cache(*args, **kwargs):
    """
    A shorter alias for `iter_cache` with `functools.lru_cache` implementation for caching **simple** iterators.
    All arguments (both positional and keyword) are passed directly to `functools.lru_cache`.
    
    Returns:
        Returns the decorated function which combines iterator wrapping, caching, and unwrapping.
    """
    
    return iter_cache(cache_engine=lru_cache(*args, **kwargs))

@smart_decorator
def alru_iter_cache(*args, **kwargs):
    """
    A shorter alias for `iter_cache` with `async_lru.alru_cache` implementation for caching **awaitable** (coroutine) iterators.
    All arguments (both positional and keyword) are passed directly to `async_lru.alru_cache`.
    
    Returns:
        Returns the decorated function which combines iterator wrapping, caching, and unwrapping.
    """
    
    return iter_cache(cache_engine=alru_cache(*args, **kwargs), iterator_type=IteratorType.AwaitableIter)

@smart_decorator
def lru_async_iter_cache(*args, **kwargs):
    """
    A shorter alias for `iter_cache` with `functools.lru_cache` implementation for caching **asynchronous** iterators.
    All arguments (both positional and keyword) are passed directly to `functools.lru_cache`.
    
    Returns:
        Returns the decorated function which combines iterator wrapping, caching, and unwrapping.
    """
    
    return iter_cache(cache_engine=lru_cache(*args, **kwargs), iterator_type=IteratorType.AsyncIter)


__all__ = \
[
    'iter_cache',
    'lru_iter_cache',
    'alru_iter_cache',
    'lru_async_iter_cache',
    
    'IteratorType',
]
