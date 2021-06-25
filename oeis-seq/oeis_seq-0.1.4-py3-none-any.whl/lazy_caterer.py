# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register("A000124")
def lazy_caterer() -> Iterable[int]:
    """Central polygonal numbers (the Lazy Caterer's sequence)."""
    yield 1  # special case
    yield 2  # special case
    for i in count(start=2):
        yield ((i * i) + i + 2) // 2
