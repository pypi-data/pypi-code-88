# coding=utf-8
from itertools import count
from math import comb
from typing import Iterable

from oeis.registry import registry


@registry.register("A000108")
def catalan() -> Iterable[int]:
    """Catalan numbers."""
    yield 1  # catalan(0)
    for n in count(start=1):
        yield comb(2 * n, n) - comb(2 * n, n - 1)
