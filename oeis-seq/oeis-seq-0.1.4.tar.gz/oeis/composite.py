# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_prime


@registry.register("A002808")
def composite() -> Iterable[int]:
    """Composite numbers."""
    for n in count(start=4):
        if not is_prime(n):
            yield n
