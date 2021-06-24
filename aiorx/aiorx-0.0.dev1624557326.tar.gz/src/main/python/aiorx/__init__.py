import functools
import inspect
from typing import Generic, TypeVar, Callable, Awaitable, Union, Any
from typing import overload

E = TypeVar('E')

T = TypeVar('T')
R = TypeVar('R')

Consumer = Callable[[E], None]
AsyncConsumer = Callable[[E], Awaitable]
OnNext = Union[Consumer[E], AsyncConsumer[E]]
OnError = Union[Consumer[Any], AsyncConsumer[Any]]

UnaryFunction = Callable[[T], R]


def as_async(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper


def ensure_async(fn):
    if inspect.iscoroutinefunction(fn):
        return fn
    return as_async(fn)


async def throw(ex: Exception):
    raise ex


async def noop(event=None):
    pass


class Completable:

    async def on_complete(self):
        raise NotImplementedError()


class Publisher(Generic[E]):

    async def on_next(self, event: E):
        raise NotImplementedError()


class Observer(Generic[E], Publisher[E], Completable):
    async def on_next(self, event: E):
        pass

    async def on_error(self, error):
        pass

    async def on_complete(self):
        pass


class Subscription:

    async def unsubscribe(self):
        raise NotImplementedError()


class Subscribable(Generic[E]):
    @overload
    async def subscribe(self, observer: Observer[E]) -> Subscription:
        pass

    @overload
    async def subscribe(self, on_next: OnNext[E] = noop, on_error=throw, on_complete=noop) -> Subscription:
        pass

    async def subscribe(self, *args, **kwargs):
        raise NotImplementedError()


class Observable(Subscribable[E]):
    pass
