import logging
from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import QuerySet
from guardian.shortcuts import get_objects_for_user
from rest_framework import permissions
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.permissions import BasePermission, IsAuthenticated

logger = logging.getLogger(__name__)


update_methods = ("PUT", "PATCH")


User = get_user_model()

perm_group_manager = "auth.change_group"


def get_group_manager_groups(user: User) -> QuerySet[Group]:
    return get_objects_for_user(user, perm_group_manager)


def has_group_manager_groups(user: User) -> bool:
    return get_group_manager_groups(user).exists()


def has_group_manager_permission(user: User, group: Optional[Group] = None) -> bool:
    return user.has_perm(perm_group_manager, group)


class IsGroupManagerRead(permissions.BasePermission):
    """Group Manager can modify a Group"""

    def has_permission(self, request, view):
        user = request.user
        return (
            user
            and user.is_authenticated
            and has_group_manager_groups(user)
            and request.method in ("GET", "HEAD")
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and has_group_manager_permission(
            request.user, obj
        )


class IsGroupManagerWrite(permissions.BasePermission):
    """Group Manager can edit a Group"""

    def has_permission(self, request, view):
        user = request.user
        return (
            user
            and user.is_authenticated
            and has_group_manager_groups(user)
            and request.method in ("PUT", "PATCH")
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view) and has_group_manager_permission(
            request.user, obj
        )


def is_staff(user: User) -> bool:
    return user.is_staff or user.is_superuser


def is_tech_account(user: User) -> bool:
    return hasattr(user, "profile") and user.profile.is_tech_account


class AuditPermission(permissions.BasePermission):
    """Staff and tech accounts can read"""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user
            and request.user.is_authenticated
            and (request.user.is_staff or is_tech_account(request.user))
        )


class IsStaff(permissions.BasePermission):
    """Staff (or PA - Portal Admin) can read/write everything."""

    def has_permission(self, request, view):
        user = request.user
        return user and user.is_authenticated and user.is_staff

    def has_object_permission(self, request, view, _):
        """Can access and perform any action on any object"""
        return self.has_permission(request, view)


class ReadOnly(IsAuthenticated):
    """Authorized users with read-only access."""

    def has_permission(self, request, view):
        return (
            super().has_permission(request, view)
            and request.method in permissions.SAFE_METHODS
        )

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class IsStaffOrReadOnly(permissions.BasePermission):
    """Authenticated users can view, staff can edit."""

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (request.method in permissions.SAFE_METHODS or request.user.is_staff)
        )


class IsAuthenticatedAndUniqueCheck(permissions.BasePermission):
    """Allows authenticated users to perform a unique check"""

    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and request.method == "POST"
        )


class IsStaffOrTechAccount(permissions.BasePermission):
    """Staff or Techaccount used by landing zones"""

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (is_tech_account(request.user) or is_staff(request.user))
        )


class UserUniquePermission(permissions.BasePermission):
    methods = ("POST",)

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.method in self.methods
            and is_staff(request.user)
        )


class UserDataPermission(permissions.BasePermission):
    update_user_method = "PATCH"
    create_local_user_method = "POST"

    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if request.method == self.create_local_user_method:
                return is_staff(request.user)
            return True
        return False

    # pylint: disable=too-many-return-statements
    def has_object_permission(self, request, view, obj):  # NOT called on POST!
        if request.method in permissions.SAFE_METHODS:
            # non-modifying operation
            return True

        # modifying operation
        requestor = request.user

        if request.method == self.update_user_method:
            # attempt to modify user
            if not is_staff(requestor):
                logger.error(
                    "Non-staff user (ID: %s) attempted to modify user (ID: %s) with data: %s",
                    requestor.id,
                    obj.id,
                    request.data,
                )
                return False

            return True

        # not allowed modifying method
        logger.error(
            "User (ID: %s) attempted to modify user (ID: %s)"
            "using not allowed method %s with data: %s",
            requestor.id,
            obj.id,
            request.method,
            request.data,
        )
        return False


class ObjectPermission(BasePermission):
    """Check if user has correct object-level permission for the action

    This class is roughly based on rest_framework.permissions.DjangoObjectPermissions
    """

    perms_map = {
        "GET": ["{app_label}.view_{model_name}"],
        "OPTIONS": [],
        "HEAD": ["{app_label}.view_{model_name}"],
        "PUT": ["{app_label}.change_{model_name}"],
        "PATCH": ["{app_label}.change_{model_name}"],
        "DELETE": ["{app_label}.delete_{model_name}"],
    }

    def get_required_object_permissions(self, method, model_cls):
        kwargs = {
            "app_label": model_cls._meta.app_label,
            "model_name": model_cls._meta.model_name,
        }

        if method not in self.perms_map:
            raise MethodNotAllowed(method)

        return tuple(perm.format(**kwargs) for perm in self.perms_map[method])

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method not in self.perms_map:
            raise MethodNotAllowed(request.method)
        return True

    def has_object_permission(self, request, view, obj):
        perms = self.get_required_object_permissions(request.method, obj.__class__)
        return request.user.has_perms(perms, obj)
