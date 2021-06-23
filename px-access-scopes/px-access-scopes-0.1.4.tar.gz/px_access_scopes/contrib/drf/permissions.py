from typing import Dict, Optional, Sequence
from functools import lru_cache, reduce
from django.http import Http404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from px_access_scopes import (
    ScopesChecker, HierarchyChecker, ScopesCheckRunner,
    MultiregistryHierarchyLookup
)
from px_access_scopes.contrib.django import ScopeDomain, user_checker
from px_access_scopes.contrib.django.globals import registries


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
    checker: ScopesChecker = ScopesCheckRunner((
        HierarchyChecker(
            (user_checker,),
            hierarchy_lookup=MultiregistryHierarchyLookup(
                registries=registries
            )
        ),
    ))

    def get_required_permissions(self, method):
        """
        Return the list of permission codes that the user is required to have.
        """

        return self.permissions_map.get(method, [])

    def has_permission(self, request, view):
        if not request.user:
            return False

        return self.checker(
            self.get_required_permissions(request.method),
            user=request.user, request=request, view=view, method=request.method,
        )

    @classmethod
    @lru_cache(maxsize=600)
    def from_permissions(
        cls,
        *permissions: Sequence[ScopeDomain],
        methods: Optional[Sequence[str]] = None
    ) -> 'ScopePermission':
        if methods is None:
            methods = cls._METHODS
        auto_methods = cls._AUTO_METHODS

        assert all(False for x in methods if x not in cls._METHODS), (
            f'Unhandelable methods provided: {methods} \r\n'
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

    @classmethod
    @lru_cache(maxsize=600)
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
        kw = {
            'request': request,
            'view': view,
            'method': request.method,
            'user': request.user,
            'obj': obj
        }

        perms = self.get_required_object_permissions(request.method)

        if not self.checker(perms, **kw):
            # If the user does not have permissions we need to determine if
            # they have read permissions to see 403, or not, and simply see
            # a 404 response.

            if request.method in SAFE_METHODS:
                # Read permissions already checked and failed, no need
                # to make another lookup.
                raise Http404

            read_perms = self.get_required_object_permissions('GET')
            if not self.checker(read_perms, **kw):
                raise Http404

            # Has read permissions.
            return False

        return True
