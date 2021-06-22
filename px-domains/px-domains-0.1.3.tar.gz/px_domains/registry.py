from typing import Callable, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union
from enum import Enum
from collections import deque

from .domain import Domain


__all__ = (
    'auto',
    'raw',
    'DomainEnum',
    'DomainRegistry',
)

T = TypeVar('T')

DomainPartType = Union[Domain, str]
DomainType = DomainPartType
RegistryNestResult = Union[T, 'DomainRegistry']
EnumDefinition = Dict[str, str]

auto = Domain('auto')
MAX_DEPTH = 10**10
inf = float('inf')


class raw:
    __slots__ = '_raw',
    _raw: str

    def __init__(self, raw: str):
        self._raw = raw


EnumFields = List[Tuple[str, Union[str, Domain, raw, object]]]


class DomainEnum(Domain, Enum): pass


class DomainRegistry:
    """Registry for easier hierarchial domain structures definition.

    Examples:
        Creating registry root

        >>> root = DomainRegistry.create_root('ROOT')
        >>>
        >>> @root.nest('SOME')
        >>> class Tokens(Enum):
        >>>     AUTO1 = auto
        >>>     AUTO2 = auto
        >>>     AUTO3 = raw('AUTO3')
        >>>     FIXED = 'some'

        Can be nested in every possible way.

        >>> @Tokens.nest('NESTED')
        >>> class Nested(Enum):
        >>>     AUTO = auto

        `Tokens.AUTO1` will be: `'ROOT::SOME::AUTO1'`
    """
    _domain: Domain
    _hierarchy: Dict[Domain, Set[Domain]]
    _reversed_hierarchy: Dict[Domain, Domain]
    _sets: Dict[Domain, DomainEnum]
    _memory: Set[Domain]
    _root: 'DomainRegistry'

    _Domain: Type[Domain] = Domain
    _Enum: Type[DomainEnum] = DomainEnum
    _auto: Domain = auto

    def __init__(self, domain: Domain, root: 'DomainRegistry' = None):
        self._domain = domain
        self._root = root
        self._hierarchy = {}
        self._reversed_hierarchy = {}
        self._sets = {}
        self._memory = set()

    def has_domain(self, domain: DomainType) -> bool:
        """Checks whether domain was registered here."""

        return str(domain) in self._root._memory

    def lookup_hierarchy(self, domain: Domain) -> Optional['DomainRegistry']:
        """Resolving registry set instance from domain if there are such."""

        if domain not in self._root._sets:
            return None

        return self.create_instance(domain)

    def lookup_descendants(self, depth: int = MAX_DEPTH) -> Set[Domain]:
        """Finds all descending domains"""

        children = deque((self._domain,))
        sets = self._root._sets
        hierarchy = self._root._hierarchy
        result = set()
        depths = {}
        r = self._root._reversed_hierarchy

        while len(children) > 0:
            current = children.popleft()

            if current in result:
                raise RecursionError(
                    'Tree is corrupted. It has loops somehow.'
                )

            result.add(current)

            d = depths[current] = depths.get(r.get(current), 0) + 1

            if d <= depth:

                if current in hierarchy:
                    children.extend(hierarchy[current])

                if current in sets:
                    result |= {e.value for e in sets[current]}

        return result

    def _lookup_ancestors(self, domain: Domain, depth: int = MAX_DEPTH) -> List[Domain]:
        """Finds all ancestor domains."""

        current = domain
        result = [current]
        hierarchy = self._root._reversed_hierarchy

        while current is not None and depth > 0:
            depth -= 1
            previous = current
            current = hierarchy.get(current, None)

            if current is None:
                current = self._Domain.parse(previous).get_basement()

            if current is not None:
                result.append(current)

        return list(reversed(result))

    def lookup_ancestors(self, depth: int = MAX_DEPTH) -> List[Domain]:
        """Finds all ancestor domains."""

        return self._lookup_ancestors(self._domain, depth=depth)

    def _register_set(self, domain: Domain, enum: DomainEnum):
        r = self._root
        r._sets[domain] = enum
        r._reversed_hierarchy[domain] = self._domain
        h = r._hierarchy[self._domain] = r._hierarchy.get(self._domain) or set()
        h.add(domain)
        self._memory.add(domain)
        self._memory |= {value.value for value in enum._member_map_.values()}

    def _get_set(self):
        return self._root._sets[self._domain]

    def _resolve_field_value(self, domain: Domain, key: str, value):
        return (
            self._Domain(value._raw)
            if isinstance(value, raw)
            else
            domain | key
            if value is self._auto
            else
            domain | value
        )

    def _resolve_field_dict(self, domain: Domain, fields: EnumFields) -> EnumDefinition:
        values = {
            key: self._resolve_field_value(domain, key, value)
            for key, value in fields
        }

        return values

    def _resolve_enum(self, domain: Domain, definition: Enum) -> EnumDefinition:
        return self._resolve_field_dict(domain, [
            (key, value.value)
            for key, value in definition._member_map_.items()
        ])

    def _resolve_object(self, domain: Domain, definition: object) -> EnumDefinition:
        return self._resolve_field_dict(domain, [
            (key, value)
            for key, value in definition.__dict__.items()
            if not key.startswith('_')
        ])

    def _resolve_definition(self, domain: Domain, definition: object) -> EnumDefinition:
        if issubclass(definition, Enum):
            return self._resolve_enum(domain, definition)

        if issubclass(definition, object):
            return self._resolve_object(domain, definition)

        return {}

    def nest(self, name: DomainPartType) -> Callable[[T], RegistryNestResult[T]]:
        """Decorator for new set registration."""

        def decorator(definition: T) -> RegistryNestResult[T]:
            domain = self._domain | name

            assert not self.has_domain(domain), (
                f'There is already a such a domain: {domain}.',
                'There couldn\'t be a registry named the same as already registered.'
            )

            enum = self._Enum(domain, self._resolve_definition(domain, definition))
            self._register_set(domain, enum)

            return self.create_instance(domain)

        return decorator

    def create_instance(self, domain: Domain):
        """Creates instance out of any domain."""

        return self._root.__class__(domain=domain, root=self._root)

    def __getattr__(self, name: str):
        try:
            return getattr(self._get_set(), name)
        except KeyError as e:
            raise AttributeError(e)

    @classmethod
    def create_root(cls, domain: DomainPartType) -> 'DomainRegistry':
        """Creates new root with the domain as a base."""

        instance = cls(
            domain if isinstance(domain, cls._Domain)
            else cls._Domain.parse(domain)
        )
        instance._root = instance

        return instance

    def __repr__(self):
        return f'<{self.__class__.__name__} registry: {str(self._domain)}>'

    def __str__(self):
        return str(self._domain)
