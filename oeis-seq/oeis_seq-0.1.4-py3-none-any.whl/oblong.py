# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry


@registry.register("A002378")
def oblong() -> Iterable[int]:
    """Oblong (or promic, pronic, or heteromecic) numbers."""
    for n in count(start=0):
        yield n * (n + 1)
