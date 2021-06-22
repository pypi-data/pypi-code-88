from typing import Iterable, Set, Type, TypeVar, Union, TYPE_CHECKING
from enum import Enum

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
