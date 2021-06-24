from aiorx import Observable, E, Subscription
from aiorx.observers import ObserverAdapter
from aiorx.subscriptions import SubscriptionAdapter


class ObservableAdapter(Observable[E]):

    def __init__(self, subscribe, unsubscribe=None):
        self._subscribe = subscribe
        self._unsubscribe = unsubscribe

    async def subscribe(self, *args, **kwargs) -> Subscription:
        observer = ObserverAdapter.create_from(*args, **kwargs)
        unsubscribe = self._subscribe(observer)
        return SubscriptionAdapter(self._unsubscribe or unsubscribe)


class ObservableDecorator(Observable):

    def __init__(self, parent: Observable, observer_factory):
        self.parent = parent
        self.observer_factory = observer_factory

    async def subscribe(self, *args, **kwargs) -> Subscription:
        observer = self.observer_factory(*args, **kwargs)
        return await self.parent.subscribe(observer)