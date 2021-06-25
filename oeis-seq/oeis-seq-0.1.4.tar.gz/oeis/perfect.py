# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_perfect


@registry.register("A000396")
def perfect() -> Iterable[int]:
    """Perfect numbers."""
    for n in count(start=1):
        if is_perfect(n):
            yield n
