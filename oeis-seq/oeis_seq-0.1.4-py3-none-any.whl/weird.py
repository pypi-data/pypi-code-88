# coding=utf-8
from itertools import count
from typing import Iterable

from oeis.registry import registry
from oeis.utils import is_abundant, is_semiperfect


@registry.register("A006037")
def weird() -> Iterable[int]:
    """Weird numbers."""
    for n in count(start=1):
        if is_abundant(n) and not is_semiperfect(n):
            yield n
