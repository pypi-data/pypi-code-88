# coding=utf-8
from itertools import count
from typing import Iterable, List

from oeis.registry import registry

from .utils import coprime


@registry.register("A000010")
def totient() -> Iterable[int]:
    """Euler totient function."""
    yield 1  # totient(0)
    for n in count(start=2):
        totients: List[bool] = [coprime(n, p) for p in range(1, n)]
        yield totients.count(True)
