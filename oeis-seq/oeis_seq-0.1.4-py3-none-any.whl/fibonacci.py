# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register(identifier="A000045")
def fibonacci() -> Iterable[int]:
    """Fibonacci numbers."""
    yield 0  # special case
    yield 1  # special case
    prev: int = 0  # fib(0)
    curr: int = 1  # fib(1)
    while True:
        prev, curr = curr, prev + curr
        yield curr
