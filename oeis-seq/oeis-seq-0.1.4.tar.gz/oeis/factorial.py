# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register("A000142")
def factorial() -> Iterable[int]:
    """Factorial numbers."""
    curr: int = 1
    for n in count(start=1):
        yield curr
        curr *= n
