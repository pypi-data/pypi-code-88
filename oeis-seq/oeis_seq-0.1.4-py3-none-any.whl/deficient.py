# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_deficient


@registry.register("A005100")
def deficient() -> Iterable[int]:
    """Deficient numbers."""
    for n in count(start=1):
        if is_deficient(n):
            yield n
