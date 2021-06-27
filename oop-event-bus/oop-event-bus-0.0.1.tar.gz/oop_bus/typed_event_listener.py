from abc import ABC, abstractmethod
from typing import Generic, TypeVar, get_args

from .event import Event
from .event_listener import EventListener

T = TypeVar("T", bound=Event)


class TypedEventListener(EventListener, Generic[T], ABC):
    @abstractmethod
    async def __call__(self, event: T):
        ...

    def get_event_name(self) -> str:
        type_args = get_args(self.__class__.__orig_bases__[0])
        return type_args[0].__name__
