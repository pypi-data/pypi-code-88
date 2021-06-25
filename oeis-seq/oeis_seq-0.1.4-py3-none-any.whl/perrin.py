# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register("A001608")
def perrin() -> Iterable[int]:
    """Perrin sequence (or Ondrej Such sequence)."""
    yield 3  # perrin(0)
    yield 0  # perrin(1)
    yield 2  # perrin(2)
    p3: int = 3  # P(n-3)
    p2: int = 0  # P(n-2)
    p1: int = 2  # P(n-1)
    while True:
        curr: int = p2 + p3
        yield curr
        p1, p2, p3 = curr, p1, p2
