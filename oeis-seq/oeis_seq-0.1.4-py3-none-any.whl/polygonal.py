# coding=utf-8
from typing import Iterable

from oeis.registry import registry


def polygonal(k: int) -> Iterable[int]:
    """
    Polygonal numbers.

    Args:
            k: # of sides.
    """
    yield 0
    prev: int = 1
    curr: int = 1
    while True:
        yield prev
        prev, curr = prev + curr + k, curr + k


@registry.register("A001477")
def natural() -> Iterable[int]:
    """Natural (nonnegative) numbers."""
    return polygonal(0)


@registry.register("A000217")
def triangular() -> Iterable[int]:
    """Triangular numbers."""
    return polygonal(1)


@registry.register("A000290")
def square() -> Iterable[int]:
    """Square numbers."""
    return polygonal(2)


@registry.register("A000326")
def pentagonal() -> Iterable[int]:
    """Pentagonal numbers."""
    return polygonal(3)


@registry.register("A000384")
def hexagonal() -> Iterable[int]:
    """Hexagonal numbers."""
    return polygonal(4)


@registry.register("A000566")
def heptagonal() -> Iterable[int]:
    """Heptagonal numbers (or 7-gonal numbers)."""
    return polygonal(5)


@registry.register("A000567")
def octagonal() -> Iterable[int]:
    """Octagonal numbers."""
    return polygonal(6)


@registry.register("A001106")
def nonagonal() -> Iterable[int]:
    """Nonagonal numbers (or 9-gonal numbers)."""
    return polygonal(7)


@registry.register("A001107")
def decagonal() -> Iterable[int]:
    """Decagonal numbers (or 10-gonal numbers)."""
    return polygonal(8)


@registry.register("A051682")
def hendecagonal() -> Iterable[int]:
    """Hendecagonal numbers (or 11-gonal numbers)."""
    return polygonal(9)


@registry.register("A051624")
def dodecagonal() -> Iterable[int]:
    """Dodecagonal numbers (or 12-gonal numbers)."""
    return polygonal(10)
