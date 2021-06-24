from typing import Optional, Sequence, Set, TYPE_CHECKING

from .scopes import ScopeDomain

if TYPE_CHECKING:
    from django.contrib.auth.models import PermissionsMixin


__all__ = 'user_checker',


def user_checker(
    check_scopes: Set[ScopeDomain],
    user: Sequence['PermissionsMixin'] = None,
    obj: Optional[object] = None,
    **kwargs
) -> bool:
    """User scopes checker."""

    return user.has_perms(check_scopes, obj=obj)
