from abc import ABC, abstractmethod
from typing import Any, Callable

from cloudevents.http import CloudEvent


class Processor(ABC):

    @abstractmethod
    def mapper(self) -> Callable[[CloudEvent], Any]:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
