from abc import ABC, abstractmethod

from .event import Event


class EventListener(ABC):
    @abstractmethod
    async def __call__(self, event: Event):
        ...

    @abstractmethod
    def get_event_name(self) -> str:
        ...
