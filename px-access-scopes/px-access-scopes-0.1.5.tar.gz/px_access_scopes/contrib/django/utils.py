from functools import lru_cache


__all__ = (
    'get_permission_app_label',
    'get_permission_string',
)


@lru_cache
def get_permission_app_label() -> str:
    from .models import Scope

    return Scope._meta.app_label


def get_permission_string(key: str) -> str:
    return get_permission_app_label() + '.' + key
