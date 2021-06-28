from __future__ import annotations

__all__ = ["frozendict"]

import functools
import operator
from typing import (
    Any,
    Dict,
    Generic,
    Iterable,
    Mapping,
    Tuple,
    TypeVar,
    Union,
    overload,
)

from unbuiltins._types import SupportsKeysAndGetItem

KT = TypeVar("KT")
VT = TypeVar("VT")
KT_co = TypeVar("KT_co", covariant=True)
VT_co = TypeVar("VT_co", covariant=True)


class frozendict(Mapping[KT, VT], Generic[KT, VT]):
    """
    frozendict() -> new empty immutable dictionary
    frozendict(mapping) -> new immutable dictionary initialized from a mapping
        object's (key, value) pairs
    frozendict(iterable) -> new immutable dictionary initialized as if via:
        d = {}
        for k, v in iterable:
            d[k] = v
    frozendict(**kwargs) -> new immutable dictionary initialized with the
        name=value pairs in the keyword argument list.
        For example:  frozendict(one=1, two=2)
    """

    __dict: Dict[KT, VT]

    @overload
    def __init__(self: frozendict[None, None]):
        ...  # pragma: no cover

    @overload
    def __init__(self: frozendict[KT, VT], seq: Iterable[Tuple[KT, VT]]):
        ...  # pragma: no cover

    @overload
    def __init__(self: frozendict[KT, VT], seq: SupportsKeysAndGetItem[KT, VT]):
        ...  # pragma: no cover

    @overload
    def __init__(self: frozendict[str, VT], **kwargs: VT):
        ...  # pragma: no cover

    @overload
    def __init__(
        self: frozendict[str, VT],
        seq: Union[SupportsKeysAndGetItem[str, VT], Iterable[Tuple[str, VT]]],
        /,
        **kwargs: VT,
    ):
        ...  # pragma: no cover

    def __init__(self, *args, **kwargs):
        self.__dict = dict(*args, **kwargs)

    def __getitem__(self, key: KT) -> VT:
        return self.__dict[key]

    def __contains__(self, key: Union[KT, Any]) -> bool:
        return key in self.__dict

    def __iter__(self):
        return iter(self.__dict)

    def __or__(
        self: frozendict[KT_co, VT_co], other: Mapping[KT_co, VT_co]
    ) -> frozendict[KT_co, VT_co]:
        merged = self.__dict.copy()
        for k, v in other.items():
            merged[k] = v
        return frozendict(merged)

    def __eq__(self, other: Union[Mapping, Any]) -> bool:
        if not isinstance(other, Mapping):
            return False

        if len(self) != len(other):
            return False

        if set(self.keys()) != set(other.keys()):
            return False

        for k, v in other.items():
            if self[k] != v:
                return False

        return True

    def __len__(self) -> int:
        return self.__len

    def __repr__(self) -> str:
        return self.__repr

    def __hash__(self):
        return self.__hash

    def copy(self) -> frozendict[KT, VT]:
        return frozendict(self.__dict)

    @functools.cached_property
    def __len(self) -> int:
        return len(self.__dict)

    @functools.cached_property
    def __repr(self) -> str:
        return f"{type(self).__name__}({repr(self.__dict)})"

    @functools.cached_property
    def __hash(self) -> int:
        return functools.reduce(operator.xor, map(hash, self.items()), 0)
