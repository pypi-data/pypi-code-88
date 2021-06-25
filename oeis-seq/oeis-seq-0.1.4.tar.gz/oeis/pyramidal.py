# coding=utf-8
from itertools import count
from typing import Iterable

from .registry import registry


def pyramidal(r: int) -> Iterable[int]:
    """
    Pyramidal numbers.

    Args:
            r: # of sides.
    """
    yield 0
    for n in count(start=1):
        yield (3 * pow(n, 2) + (pow(n, 3) * (r - 2)) - n * (r - 5)) // 6


@registry.register("A000292")
def triangular_pyramidal() -> Iterable[int]:
    """Triangular pyramidal numbers."""
    return pyramidal(3)


@registry.register("A000330")
def square_pyramidal() -> Iterable[int]:
    """Square pyramidal numbers."""
    return pyramidal(4)
