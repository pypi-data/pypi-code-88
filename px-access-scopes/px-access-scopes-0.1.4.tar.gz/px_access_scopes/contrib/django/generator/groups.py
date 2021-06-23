from typing import List
from django.contrib.auth.models import Permission, Group
from px_access_scopes.aggregates import Aggregate

from ..aggregates import Aggregate
from ..models import Scope


__all__ = 'generate_group',


def generate_group(aggregate: Aggregate) -> Group:
    group, _ = Group.objects.get_or_create(
        pk=aggregate.group_id, defaults={'name': aggregate.verbose_name}
    )
    group.permissions.set(Permission.objects.filter(
        codename__in=aggregate, content_type=Scope.get_content_type()
    ))

    return group
