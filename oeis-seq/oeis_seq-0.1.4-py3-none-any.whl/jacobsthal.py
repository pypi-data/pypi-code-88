# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register("A001045")
def jacobsthal() -> Iterable[int]:
    """Jacobsthal sequence (or Jacobsthal numbers)."""
    yield 0  # special case
    yield 1  # special case
    prev: int = 0  # initially set to jacobsthal(0)
    curr: int = 1  # initially set to jacobsthal(1)
    while True:
        prev, curr = curr, curr + 2 * prev
        yield curr
