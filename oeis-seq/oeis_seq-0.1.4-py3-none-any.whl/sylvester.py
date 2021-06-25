# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register("A000058")
def sylvester() -> Iterable[int]:
    """Sylvester's sequence."""
    prev: int = 2  # sylvester(0)
    while True:
        yield prev
        prev = (prev * (prev - 1)) + 1
