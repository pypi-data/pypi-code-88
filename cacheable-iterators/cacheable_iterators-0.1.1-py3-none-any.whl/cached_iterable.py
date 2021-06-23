"""
Helper classes for caching both simple (`Iterator[T]`) and coroutine/awaitable (`Awaitable[Iterator[T]]`) iterators.
Could be used outside of this module if you dare.
"""

from typing import *


T = TypeVar('T')
class CachedIterable(Iterable[T], Generic[T]):
    """
    A cache-implementing wrapper for an iterator.
    Note that this is class is `Iterable[T]` rather than `Iterator[T]`.
    It should not be iterated by his own.
    """
    
    cache: List[T]
    iter: Iterator[T]
    completed: bool
    
    def __init__(self, it: Iterator[T]):
        self.iter = iter(it)
        self.cache = list()
        self.completed = False
    
    def __iter__(self) -> Iterator[T]:
        return CachedIterator(self)
    
    def __next__(self) -> T:
        try:
            item = next(self.iter)
        except StopIteration:
            self.completed = True
            raise
        else:
            self.cache.append(item)
            return item
    
    def __del__(self):
        del self.cache

class CachedIterator(Iterator[T], Generic[T]):
    """
    A cache-using wrapper for an iterator.
    This class is only constructed by `CachedIterable` and cannot be used without it.
    """
    
    parent: CachedIterable[T]
    position: int
    
    def __init__(self, parent: CachedIterable):
        self.parent = parent
        self.position = 0
    
    def __next__(self) -> T:
        if (self.position < len(self.parent.cache)):
            item = self.parent.cache[self.position]
        elif (self.parent.completed):
            raise StopIteration
        else:
            item = next(self.parent)
        
        self.position += 1
        return item


__all__ = \
[
    'CachedIterable',
    'CachedIterator',
]
