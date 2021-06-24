from typing import Iterable

from aiorx import E, Observable, Observer
from aiorx.observers import ObserverAdapter
from aiorx.subscriptions import NullSubscription


class IterObservable(Observable[E]):

    def __init__(self, iterable: Iterable[E]):
        self.iterable = iterable

    async def process(self, observer: Observer[E]):
        iterator = iter(self.iterable)
        try:
            while True:
                await observer.on_next(next(iterator))
        except StopIteration:
            return

    async def subscribe(self, *args, **kwargs):
        observer = ObserverAdapter.create_from(*args, **kwargs)
        await self.process(observer)
        return NullSubscription()


def from_iterable(iterable: Iterable[E]) -> Observable[E]:
    return IterObservable(iterable)
