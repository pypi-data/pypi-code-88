from typing import Optional, Sequence, Set, Type

from ..scopes import ScopeRegistry, ScopeDomain
from ..utils import normalize_scope, ScopeType
from ..exceptions import CheckExit
from .base import ScopesChecker
from .checkers import run_checkers, ScopesCheckerType


__all__ = 'ScopesCheckRunner',


class ScopesCheckRunner(ScopesChecker):
    """Root runner for multiple checkers.

    Instance might be used as a simple checker inside another runner
    but with small exceptions:

    - It transforms passed scopes into an appropriate `.Domain` instances.
    - It handles `CheckExit` and returns `False` in that case.
    - It adds `registry` to a provided kwargs, by replasing any passed through.
    """

    Domain: Type[ScopeDomain] = ScopeDomain
    registry: Optional[ScopeRegistry]
    checkers: Sequence[ScopesCheckerType]

    def __init__(
        self,
        checkers: Sequence[ScopesCheckerType],
        registry: Optional[ScopeRegistry] = None
    ):
        assert len(checkers) != 0, 'There must be at least one checker.'

        self.checkers = checkers
        self.registry = registry

    def _normalize_scope(self, scope: ScopeType):
        return normalize_scope(scope, self.Domain)

    def _run_checkers(
        self,
        check_scopes: Sequence[ScopeType],
        kwargs: dict = {}
    ) -> bool:
        if self.registry is not None:
            kwargs['registry'] = self.registry

        return run_checkers(check_scopes, self.checkers, kwargs)

    def has(self, check_scopes: Sequence[ScopeType], *_, **kwargs) -> bool:
        check_scopes = {
            self._normalize_scope(scope) for scope in check_scopes
        }

        try:
            return self._run_checkers(check_scopes, kwargs)
        except CheckExit:
            return False
