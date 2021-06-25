# coding=utf-8
from typing import Iterable, List

from oeis.registry import registry


@registry.register("A005132")
def recaman() -> Iterable[int]:
    """Recamán's sequence."""
    yield 0  # recaman(0)
    seq: List[int] = [0]
    i: int = 1
    while True:
        n: int = seq[i - 1] - i
        if n > 0 and (n not in seq):
            pass
        else:
            n = seq[i - 1] + i
        seq.append(n)
        yield n
        i += 1
