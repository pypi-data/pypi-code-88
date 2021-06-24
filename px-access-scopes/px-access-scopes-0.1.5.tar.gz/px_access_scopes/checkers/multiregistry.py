from typing import Callable, Sequence, Set, Tuple
from functools import lru_cache

from ..scopes import ScopeRegistry, ScopeDomain
from .checkers import registry_hierarchy_lookup


__all__ = 'MultiregistryHierarchyLookup',


class MultiregistryHierarchyLookup:
    registries: Sequence[ScopeRegistry]
    descendands: Sequence[Tuple[ScopeRegistry, Set[ScopeDomain]]]
    lookup: Callable

    def __init__(
        self,
        registries: Sequence[ScopeRegistry] = [],
        hierarchy_lookup: Callable = registry_hierarchy_lookup,
    ):
        self.registries = registries
        self.descendands = []
        self.lookup = hierarchy_lookup

    def update_descendants(self):
        self.descendands = [
            (registry, registry.lookup_descendants())
            for registry in self.registries
        ]

    @lru_cache
    def get_registry(self, scope: ScopeDomain, first: bool = True):
        for registry, scopes in self.descendands:
            if scope in scopes:
                return registry

        if first:
            self.update_descendants()
            self.get_registry(scope, first=False)

    def __call__(self, scope: ScopeDomain, **kwargs) -> Set[ScopeDomain]:
        registry = self.get_registry(scope)

        return self.lookup(scope=scope, registry=registry, **kwargs)
