# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_superperfect


@registry.register("A019279")
def superperfect() -> Iterable[int]:
    """Perfect numbers."""
    for n in count(start=1):
        if is_superperfect(n):
            yield n
