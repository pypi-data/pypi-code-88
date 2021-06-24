from typing import Callable, Optional, Sequence, Set, Union
from functools import reduce

from ..scopes import ScopeRegistry, ScopeDomain
from ..aggregates import Aggregate
from ..utils import to_set, ScopeType
from .base import ScopesChecker


__all__ = (
    'run_checkers',
    'scopes_checker',
    'aggregates_checker',
    'registry_hierarchy_lookup',
    'domain_path_hierarchy_lookup',
    'HierarchyChecker',
)

ScopesCheckerType = Union['ScopesChecker', Callable[..., bool]]


def run_checkers(
    check_scopes: Set[ScopeDomain],
    checkers: Sequence['ScopesCheckerType'],
    kwargs: dict = {}
) -> bool:
    """Checkers runner function."""

    for checker in checkers:
        if checker(check_scopes, **kwargs):
            return True

    return False


def scopes_checker(
    check_scopes: Set[ScopeDomain],
    scopes: Sequence[ScopeType] = (),
    **kwargs
) -> bool:
    """Simple scopes to scopes checker."""

    return False if not scopes else len(to_set(scopes) & check_scopes) > 0


def aggregates_checker(
    check_scopes: Set[ScopeDomain],
    aggregates: Sequence[Aggregate] = (),
    **kwargs
) -> bool:
    """Checker for scopes in access aggregates."""

    return False if not aggregates else any(
        scopes_checker(check_scopes, scopes=aggregate)
        for aggregate in aggregates
    )


def registry_hierarchy_lookup(
    scope: ScopeDomain,
    registry: Optional[ScopeRegistry] = None,
    **kwargs,
) -> Set[ScopeDomain]:
    """Resolves scope hierarchy from the registry."""

    if registry is None:
        return {scope}

    found = registry.lookup_hierarchy(scope)

    if found is None:
        found = registry.lookup_hierarchy(scope.get_basement())

    return {scope} | (set(found.lookup_ancestors()) if found is not None else set())


def domain_path_hierarchy_lookup(
    scope: ScopeDomain, **kwargs
) -> Set[ScopeDomain]:
    """Resolves scope hierarchy defined in domain."""

    return set(scope.get_path())


class HierarchyChecker(ScopesChecker):
    """Hierarchical scopes checker.

    It finds all scope hierarchy and runs internal checkers for all
    scopes it found.
    """
    hierarchy_lookup: Callable
    checkers: Sequence[ScopesCheckerType]

    def __init__(
        self,
        checkers: Sequence[ScopesCheckerType],
        hierarchy_lookup: Callable = registry_hierarchy_lookup
    ):
        self.checkers = checkers
        self.hierarchy_lookup = hierarchy_lookup

    def has(
        self,
        check_scopes: Set[ScopeDomain],
        **kwargs
    ) -> bool:
        resolved_scopes = reduce(
            lambda acc, x: acc | self.hierarchy_lookup(x, **kwargs),
            check_scopes,
            set()
        )

        return run_checkers(resolved_scopes, self.checkers, kwargs)
