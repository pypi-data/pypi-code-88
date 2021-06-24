import asyncio

from aiorx import Observable, E, Observer, Subscription
from aiorx.observers import ObserverAdapter
from aiorx.subscriptions import SubscriptionAdapter


class Subject(Observable[E], Observer[E]):

    def __init__(self):
        self.listeners = []

    async def on_next(self, event: E):
        await asyncio.gather(*[listener.on_next(event) for listener in self.listeners])

    async def on_error(self, error):
        await asyncio.gather(*[listener.on_error(error) for listener in self.listeners])

    async def on_complete(self):
        await asyncio.gather(*[listener.on_complete() for listener in self.listeners])
        # @todo should fail for new subscribers?
        self.listeners = None

    async def subscribe(self, *args, **kwargs) -> Subscription:
        listener = ObserverAdapter.create_from(*args, **kwargs)
        self.listeners.append(listener)
        return SubscriptionAdapter(lambda: self.listeners.remove(listener))
