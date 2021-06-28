__all__ = ["Missing", "Missable"]

import enum
from typing import Literal, TypeVar, Union, final

T = TypeVar("T")


@final
class MissingType(enum.Enum):
    # workaround to make type annotation recognize Missing as a singleton
    #  see https://github.com/python/typing/issues/236
    __slots__ = ()

    MISSING = 0

    def __bool__(self):
        return False

    def __str__(self):
        return "Missing"

    __repr__ = __str__


# Missing: Final[MissingType] = MissingType()
Missing: Literal[MissingType.MISSING] = MissingType.MISSING

Missable = Union[T, Literal[MissingType.MISSING]]
Missable.__doc__ = """
Missable type, analogous to typing.Optional.

Missable[X] is equivalent to Union[X, Type[Missing]].
"""
