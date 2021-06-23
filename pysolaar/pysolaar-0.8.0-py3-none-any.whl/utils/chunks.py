from itertools import chain, islice
from typing import Generator, Iterable


def chunks(iterable: Iterable, size: int = 10) -> Generator:
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))