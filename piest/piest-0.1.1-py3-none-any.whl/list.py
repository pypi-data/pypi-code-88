from __future__ import annotations

from itertools import chain
from typing import List, Optional, Tuple, TypeVar

T = TypeVar('T')


def head_rest(li: List[T]) -> Tuple[Optional[T], List[T]]:
    return (li[0], li[1:]) if len(li) != 0 else (None, [])


def flat1_chain(li: List[List[T]]) -> List[T]:
    return list(chain.from_iterable(li))


def splits(li: List[str]) -> List[List[str]]:
    return list(map(str.split, li))


def flat_splits(li: List[str]) -> List[str]:
    return flat1_chain(splits(li))


def divide(li: List[T], val: T) -> Tuple[List[T], List[T]]:
    return (li[:(i := li.index(val))], li[i+1:]) if val in li else (li, [])
