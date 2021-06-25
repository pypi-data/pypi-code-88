# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register("A000931")
def padovan() -> Iterable[int]:
    """Padovan sequence (or Padovan numbers)."""
    yield 1  # padovan(0)
    yield 1  # padovan(1)
    yield 1  # padovan(2)
    p3: int = 1  # P(n-3)
    p2: int = 1  # P(n-2)
    p1: int = 1  # P(n-1)
    while True:
        curr = p2 + p3
        yield curr
        p1, p2, p3 = curr, p1, p2
