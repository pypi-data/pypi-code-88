from __future__ import annotations

__all__ = ["either", "filternone", "first"]

from typing import Iterable, Optional, TypeVar

from unbuiltins.constants import Missable, Missing

T = TypeVar("T")


def either(*args: Optional[T]) -> T:
    """
    Return the first arg that is not None and not Missing.
    """
    if len(args) < 2:
        raise TypeError(
            f"either expected at least 2 arguments, got {len(args)}"
        )

    for arg in args:
        if arg is not None and arg is not Missing:
            return arg

    raise TypeError("all arguments are None or Missing")


def filternone(iterable: Iterable[Optional[T]], /) -> Iterable[T]:
    """
    filternone(iterable)

    Return those items of iterable that are not None.
    """
    return (i for i in iterable if i is not None)


def first(iterable: Iterable[T], /, default: Missable[T] = Missing) -> T:
    """
    first(iterable[, default])

    Return the first item from the iterable. If default is given and the
    iteratable has no next item, it is returned instead of raising TypeError
    """
    v = next(iter(iterable), default)
    if v is Missing:
        raise TypeError("first() of empty iterable")
    else:
        return v
