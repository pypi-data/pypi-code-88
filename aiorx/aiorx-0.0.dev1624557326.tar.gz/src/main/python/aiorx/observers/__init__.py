from typing import overload

from aiorx import Observer, E, OnNext, noop, throw, ensure_async


class ObserverAdapter(Observer[E]):

    @classmethod
    @overload
    def create_from(cls, observer: Observer[E]) -> Observer[E]:
        pass

    @classmethod
    @overload
    def create_from(cls, on_next: OnNext = noop, on_error=throw, on_complete=noop) -> Observer[E]:
        pass

    @classmethod
    def create_from(cls, *args, **kwargs):
        if len(args) > 0 and getattr(args[0], 'on_next', False):
            return args[0]
        return cls(*args, **kwargs)

    def __init__(self, on_next=noop, on_error=throw, on_complete=noop):
        self.on_next = ensure_async(on_next)
        self.on_error = ensure_async(on_error)
        self.on_complete = ensure_async(on_complete)
