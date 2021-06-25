# coding=utf-8
from typing import Iterable

from oeis.registry import registry


@registry.register("A224749")
def vauban() -> Iterable[int]:
    """Vauban's sequence."""
    yield 0
    yield 1
    n5: int = 0  # vauban(0)
    n4: int = 0  # vauban(0)
    n3: int = 0  # vauban(0)
    n2: int = 0  # vauban(0)
    n1: int = 1  # vauban(1)
    while True:
        curr: int = 3 * n1 + 6 * n2 + 6 * n3 + 6 * n4 + 6 * n5
        yield curr
        n1, n2, n3, n4, n5 = curr, n1, n2, n3, n4
