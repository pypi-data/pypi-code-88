# coding=utf-8
"""Create a thin wrapper around OEIS Registry."""
from typing import Callable, Dict, Generic, Iterable, TypeVar

T = TypeVar("T", bound=Callable[[], Iterable[int]])


class OEISRegistry(Generic[T]):
    """Thin wrapper around OEIS Registry."""

    def __init__(self) -> None:
        """Initialize an OEISRegistry."""
        self.sequences: Dict[str, T] = {}

    def __getitem__(self, identifier: str) -> T:
        """Return the sequence generator."""
        return self.sequences[identifier]

    def register(self, identifier: str) -> Callable[[T], T]:
        """
        Register sequence by identifier.

        Args:
            identifier: Sequence Identifier.
        """

        def wrapper(func: T) -> T:
            """
            Create a wrapper function.

            Args:
                func: Sequence generator
            """
            self.sequences[identifier] = func
            return func

        return wrapper


registry: OEISRegistry[Callable[[], Iterable[int]]] = OEISRegistry[
    Callable[[], Iterable[int]]
]()

__all__ = [
    "registry",
    "OEISRegistry",
]
