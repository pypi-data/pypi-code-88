from typing import List
from django.contrib.auth.models import Permission

from ..scopes import ScopeRegistry
from ..models import Scope


__all__ = 'generate_permissions',


def generate_permissions(registry: ScopeRegistry) -> List[Permission]:
    keys = set(registry.lookup_descendants())
    content_type = Scope.get_content_type()
    existing = (
        Permission.objects
        .filter(codename__in=keys)
        .values_list('codename', flat=True)
    )
    choices = registry.get_choices(keys.difference(existing))

    return Permission.objects.bulk_create([
        Permission(codename=value, name=label, content_type=content_type)
        for value, label in choices
    ])
