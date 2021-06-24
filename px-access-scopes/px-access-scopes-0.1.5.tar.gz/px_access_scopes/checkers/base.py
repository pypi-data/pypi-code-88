from typing import Set

from ..scopes import ScopeDomain
from .mixins import HasCallableMixin


__all__ = 'ScopesChecker',


class ScopesChecker(HasCallableMixin):
    def has(
        self,
        check_scopes: Set[ScopeDomain],
        *_,
        **kwargs
    ) -> bool:
        raise NotImplemented('Implement `has` method. It\'s mandatory.')
