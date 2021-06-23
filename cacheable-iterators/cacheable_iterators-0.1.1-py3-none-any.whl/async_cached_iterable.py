"""
Helper classes for caching both asynchronous iterators (`AsyncIterator[T]`).
Could be used outside of this module if you dare.
"""

from typing import *


T = TypeVar('T')
class AsyncCachedIterable(AsyncIterable[T], Generic[T]):
    """
    A cache-implementing wrapper for an asynchronous iterator.
    Note that this is class is `AsyncIterable[T]` rather than `AsyncIterator[T]`.
    It should not be iterated by his own.
    """
    
    cache: List[T]
    iter: AsyncIterator[T]
    completed: bool
    
    def __init__(self, it: AsyncIterator[T]):
        self.iter = it.__aiter__()
        self.cache = list()
        self.completed = False
    
    def __aiter__(self) -> AsyncIterator[T]:
        return AsyncCachedIterator(self)
    
    async def __anext__(self) -> T:
        try:
            item = await self.iter.__anext__()
        except StopAsyncIteration:
            self.completed = True
            raise
        else:
            self.cache.append(item)
            return item
    
    def __del__(self):
        del self.cache

class AsyncCachedIterator(AsyncIterator[T], Generic[T]):
    """
    A cache-using wrapper for an iterator.
    This class is only constructed by `CachedIterable` and cannot be used without it.
    """
    
    parent: AsyncCachedIterable[T]
    position: int
    
    def __init__(self, parent: AsyncCachedIterable):
        self.parent = parent
        self.position = 0
    
    async def __anext__(self) -> T:
        if (self.position < len(self.parent.cache)):
            item = self.parent.cache[self.position]
        elif (self.parent.completed):
            raise StopAsyncIteration
        else:
            item = await self.parent.__anext__()
        
        self.position += 1
        return item


__all__ = \
[
    'AsyncCachedIterable',
    'AsyncCachedIterator',
]
