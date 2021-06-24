from asyncio import Event

from aiorx import Subscription, ensure_async


class NullSubscription:

    async def unsubscribe(self):
        pass


NULL_SUBSCRIPTION = NullSubscription()


class EventSubscription(Subscription):

    def __init__(self, event: Event):
        self.event = event

    async def unsubscribe(self):
        self.event.set()


class SubscriptionAdapter(Subscription):

    def __init__(self, unsubscribe):
        self._unsubscribe = ensure_async(unsubscribe)

    async def unsubscribe(self):
        await self._unsubscribe()
