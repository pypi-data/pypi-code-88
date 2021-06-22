from django.contrib.auth import get_user_model
from guardian.shortcuts import get_objects_for_user
from rest_framework.filters import BaseFilterBackend

User = get_user_model()


class UserActiveFilter(BaseFilterBackend):
    """Filter users depending on the user being active (`is_active` is `True`)."""

    param = "include_inactive"

    def filter_queryset(self, request, queryset, view):
        if request.method != "GET" or request.query_params.get(self.param):
            # pylint: disable=no-member
            return queryset.all()
        # exclude inactive users by default
        return queryset.exclude(is_active=False)

    def get_schema_operation_parameters(self, view):
        return (
            {
                "name": self.param,
                "required": False,
                "in": "query",
                "description": "Includes users which are not active (`is_active` is `False`)",
                "schema": {"type": "boolean"},
            },
        )


class ObjectPermissionsFilter(BaseFilterBackend):
    """Filter objects which user has object-level view permission"""

    accept_global_permissions = False
    superuser_show_all = True

    def filter_queryset(self, request, queryset, view):
        app_label = queryset.model._meta.app_label
        model_name = queryset.model._meta.model_name
        obj = get_objects_for_user(
            request.user,
            f"{app_label}.view_{model_name}",
            queryset,
            accept_global_perms=self.accept_global_permissions,
            with_superuser=self.superuser_show_all,
        )
        return obj
