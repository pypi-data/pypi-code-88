from typing import Iterable, Iterator, Set, Type, TypeVar, Union, TYPE_CHECKING
from enum import Enum

from .aggregates import Aggregate, Aggregates

if TYPE_CHECKING:
    from .scopes import ScopeDomain


T = TypeVar('T')
D = TypeVar('D', bound='ScopeDomain')
ScopeType = Union['ScopeDomain', Enum, str]


def to_set(value: Iterable[T]) -> Set[T]:
    return value if isinstance(value, set) else set(value)


def normalize_scope(scope: ScopeType, cls: Type[D] = 'ScopeDomain') -> D:
    if isinstance(scope, Enum):
        scope = scope.value

    if not isinstance(scope, cls):
        scope = cls.parse(scope)

    return scope


def flatten_aggregates(
    aggregates: Iterable[Union['Aggregate', 'Aggregates']]
) -> Iterator['Aggregate']:
    return (
        a
        for agg in aggregates
        for a in (
            (getattr(agg, name) for name in agg._item_names)
            if isinstance(agg, type) and issubclass(agg, Aggregates)
            else (agg,)
        )
    )
