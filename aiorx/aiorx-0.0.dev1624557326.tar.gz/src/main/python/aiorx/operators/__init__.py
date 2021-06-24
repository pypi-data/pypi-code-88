from typing import Generic

from aiorx import E, Observable, Observer
from aiorx.observables import ObservableDecorator
from aiorx.observers import ObserverAdapter


class Map(Generic[E]):

    def __init__(self, map_fn):
        self.map_fn = map_fn

    def __call__(self, observable: Observable[E]) -> Observable[E]:
        def factory(*args, **kwargs) -> Observer[E]:
            listener = ObserverAdapter.create_from(*args, **kwargs)

            async def on_next(event: E):
                await listener.on_next(self.map_fn(event))

            async def on_error(error):
                await listener.on_error(error)

            async def on_complete():
                await listener.on_complete()

            return ObserverAdapter(on_next, on_error, on_complete)

        return ObservableDecorator(observable, factory)


class Filter(Generic[E]):

    def __init__(self, condition):
        self.condition = condition

    def __call__(self, observable: Observable[E]) -> Observable[E]:
        def factory(*args, **kwargs) -> Observer[E]:
            listener = ObserverAdapter.create_from(*args, **kwargs)

            async def on_next(event: E):
                if self.condition(event):
                    await listener.on_next(event)

            async def on_error(error):
                await listener.on_error(error)

            async def on_complete():
                await listener.on_complete()

            return ObserverAdapter(on_next, on_error, on_complete)

        return ObservableDecorator(observable, factory)


class Tap(Generic[E]):

    def __init__(self, *args, **kwargs):
        self.observer = ObserverAdapter.create_from(*args, **kwargs)

    def __call__(self, observable: Observable[E]) -> Observable[E]:
        def factory(*args, **kwargs) -> Observer[E]:
            listener = ObserverAdapter.create_from(*args, **kwargs)

            async def on_next(event: E):
                await self.observer.on_next(event)
                await listener.on_next(event)

            async def on_error(error):
                await self.observer.on_error(error)
                await listener.on_error(error)

            async def on_complete():
                await self.observer.on_complete()
                await listener.on_complete()

            return ObserverAdapter(on_next, on_error, on_complete)

        return ObservableDecorator(observable, factory)


map = Map
filter = Filter
tap = Tap
