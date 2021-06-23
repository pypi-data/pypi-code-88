from enum import Enum
from px_domains import Domain, DomainRegistry, raw


__all__ = (
    'auto',
    'raw',
    'ScopeDomain',
    'ScopeEnum',
    'ScopeRegistry',
)


class ScopeDomain(Domain):
    pass


class ScopeEnum(ScopeDomain, Enum):
    pass


auto = ScopeDomain('auto')


class ScopeRegistry(DomainRegistry):
    """Simple domain registry for an access scopes.

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
    _Enum = ScopeEnum
    _auto = auto
