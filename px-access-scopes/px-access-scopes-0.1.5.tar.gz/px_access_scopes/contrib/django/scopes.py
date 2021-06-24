from functools import cached_property
from typing import Callable, Dict, List, Optional, Tuple, Type, Union
from collections import OrderedDict
from django.db import models
from django.utils.translation import pgettext_lazy
from px_domains import raw
from px_domains.registry import DomainPartType, T, RegistryNestResult
from px_access_scopes import ScopeDomain as BaseDomain, ScopeRegistry as BaseRegistry


__all__ = (
    'ScopeDomain',
    'ScopeEnum',
    'ScopeRegistry',
    'auto',
    'raw',
)

EnumDefinition = Dict[str, Union[Tuple[str, str], str]]
TVal = Tuple[str, str, str]
EnumField = Union[TVal, Tuple[str, str]]
EnumFields = List[EnumField]


def get_tuple(values: EnumField) -> TVal:
    if len(values) == 3:
        return values

    return (values + (None, None, None))[:3]


def get_labeled(value, label = None):
    if label is None:
        return value

    return value, label


class ScopeDomain(BaseDomain):
    _delimiter: str = ':'

    @cached_property
    def permission(self):
        from .utils import get_permission_string

        return get_permission_string(self)


class ScopeLabelDomain(BaseDomain):
    _delimiter: str = pgettext_lazy('pxd_access_scopes', ' : ')


class ScopeEnum(ScopeDomain, models.Choices):
    pass


# FIXME:
# Due to an strange work of django's enums auto will be a str
# instead of object.
auto: ScopeDomain = 'auto-' + str(object())


class ScopeRegistry(BaseRegistry):
    """Django-specific domain registry for an access scopes.

    Examples:
        Creating registry root

        >>> root = ScopeRegistry.create_root('ROOT')
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

    _Domain = ScopeDomain
    _LabelDomain = ScopeLabelDomain
    _Enum = ScopeEnum
    _auto = auto
    _labels: OrderedDict


    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self._labels = OrderedDict()

    def _register_set(self, domain: ScopeDomain, enum: ScopeEnum):
        super()._register_set(domain, enum)

        for member in enum:
            self._root._labels[member] = member.label

    def _resolve_field_dict(self, domain: ScopeDomain, fields: EnumFields) -> EnumDefinition:
        values = {
            key: get_labeled(
                self._resolve_field_value(domain, key, value),
                label
            )
            for key, value, label in (get_tuple(t) for t in fields)
        }

        return values

    def _resolve_choices(self, domain: ScopeDomain, definition: Type[models.Choices]) -> EnumDefinition:
        return self._resolve_field_dict(domain, [
            (key, value.value, definition._value2label_map_.get(value.value))
            for key, value in definition._member_map_.items()
        ])

    def _resolve_definition(self, domain: ScopeDomain, definition: object) -> EnumDefinition:
        if issubclass(definition, models.Choices):
            return self._resolve_choices(domain, definition)

        return super()._resolve_definition(domain, definition)

    def _get_choices_label(self, domain: str):
        labels = self._root._labels
        ancestors = self._lookup_ancestors(domain)

        return self._LabelDomain.from_definition([str(labels.get(x)) for x in ancestors])

    def get_choices(self, domains: List[ScopeDomain]):
        empty = [(None, self.__empty__)] if hasattr(self, '__empty__') else []

        return empty + [
            (domain, self._get_choices_label(domain)) for domain in domains
        ]

    def nest(
        self,
        name: DomainPartType,
        label: Optional[str] = None
    ) -> Callable[[T], RegistryNestResult[T]]:
        """Decorator for new set registration."""
        internal = super().nest(name)

        def decorator(*args) -> RegistryNestResult[T]:
            instance = internal(*args)
            instance._root._labels[instance._domain] = label if label is not None else instance._domain._definition[-1]

            return instance

        return decorator

    @classmethod
    def create_root(
        cls,
        domain: DomainPartType,
        label: Optional[str] = None
    ) -> 'ScopeRegistry':
        """Creates new root with the domain as a base."""

        instance = super(ScopeRegistry, cls).create_root(domain)
        instance._root._labels[instance._domain] = label if label is not None else instance._domain

        return instance
