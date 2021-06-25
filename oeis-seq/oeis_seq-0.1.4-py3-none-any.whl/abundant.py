# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_abundant


@registry.register("A005101")
def abundant() -> Iterable[int]:
    """Abundant numbers."""
    for n in count(start=1):
        if is_abundant(n):
            yield n
