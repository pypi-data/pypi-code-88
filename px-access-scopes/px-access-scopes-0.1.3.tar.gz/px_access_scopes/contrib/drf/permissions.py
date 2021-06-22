from typing import Dict, Optional, Sequence
from functools import cached_property, reduce
from django.http import Http404
from rest_framework.permissions import BasePermission, SAFE_METHODS
from px_access_scopes.contrib.django import ScopeDomain


__all__ = 'ScopePermission', 'ScopeObjectPermission'


class ScopePermission(BasePermission):
    _METHODS: Sequence[str] = {
        'GET', 'OPTIONS', 'HEAD',
        'POST', 'PUT', 'PATCH', 'DELETE',
    }
    _AUTO_METHODS: Dict[str, Sequence[str]] = {
        'GET': ('OPTIONS', 'HEAD',),
        'POST': ('OPTIONS', 'HEAD',),
        'PUT': ('OPTIONS', 'HEAD',),
        'PATCH': ('OPTIONS', 'HEAD',),
        'DELETE': ('OPTIONS', 'HEAD',),
    }
    permissions_map: Dict[str, Sequence[str]] = {}

    def get_required_permissions(self, method):
        """
        Return the list of permission codes that the user is required to have.
        """

        return self.permissions_map.get(method, [])

    def has_permission(self, request, view):
        if not request.user:
            return False

        return request.user.has_perms(
            self.get_required_permissions(request.method)
        )

    @cached_property
    @classmethod
    def from_permissions(
        cls,
        *permissions: Sequence[ScopeDomain],
        methods: Optional[Sequence[str]] = None
    ) -> 'ScopePermission':
        if methods is None:
            methods = cls._METHODS
        auto_methods = cls._AUTO_METHODS

        assert any(False for x in methods if x not in cls._METHODS), (
            f'Unhandelable method provided: {methods} \r\n'
            f'Must be one of: {cls._METHODS}.'
        )

        def permissions_map_reducer(map, method):
            map[method] = permissions

            for m in auto_methods.get(method, []):
                if m not in map:
                    map[m] = permissions

            return map

        permissions_map = reduce(permissions_map_reducer, methods, {})

        return type(cls.__name__, (cls, ), {
            'permissions_map': permissions_map
        })

    @cached_property
    @classmethod
    def from_scopes(
        cls,
        *scopes: Sequence[ScopeDomain],
        methods: Optional[Sequence[str]] = None
    ) -> 'ScopePermission':
        return cls.from_permissions(
            *(scope.permission for scope in scopes), methods=methods
        )


class ScopeObjectPermission(ScopePermission):
    def get_required_object_permissions(self, method):
        """
        Return the list of permission codes that the user is required to have.
        """

        return self.permissions_map.get(method, [])

    def has_object_permission(self, request, view, obj):
        user = request.user

        perms = self.get_required_object_permissions(request.method)

        if not user.has_perms(perms, obj):
            # If the user does not have permissions we need to determine if
            # they have read permissions to see 403, or not, and simply see
            # a 404 response.

            if request.method in SAFE_METHODS:
                # Read permissions already checked and failed, no need
                # to make another lookup.
                raise Http404

            read_perms = self.get_required_object_permissions('GET')
            if not user.has_perms(read_perms, obj):
                raise Http404

            # Has read permissions.
            return False

        return True
