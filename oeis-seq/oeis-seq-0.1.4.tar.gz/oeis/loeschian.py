# coding=utf-8
from itertools import count
from math import sqrt
from typing import Iterable

from oeis.registry import registry


@registry.register("A003136")
def loeschian() -> Iterable[int]:
    """Loeschian numbers."""

    def is_loeschian(n: int) -> bool:
        if n % 3 == 2:
            return False
        M: int = 2 * round(sqrt(n / 3))
        for x in range(0, M + 1):
            for y in range(0, x + 1):
                if n == (x ** 2) + (x * y) + (y ** 2):
                    return True
        return False

    yield 0
    yield 1
    yield 3
    for i in count(start=4):
        if is_loeschian(i):
            yield i
