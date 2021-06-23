from django.contrib.auth import get_user_model
from django_drf_utils.views.utils import unique_check
from rest_framework import mixins, permissions, viewsets, generics, serializers
from rest_framework.filters import SearchFilter
from rest_framework.schemas.openapi import AutoSchema

from ..filters import UserActiveFilter
from ..permissions import (
    has_group_manager_groups,
    is_tech_account,
    UserDataPermission,
    UserUniquePermission,
)
from ..serializers import (
    UserSerializer,
    UserinfoSerializer,
)

User = get_user_model()


class UserinfoSchema(AutoSchema):
    def map_field(self, field):
        mapped_field = super().map_field(field)
        if isinstance(field, serializers.SerializerMethodField):
            field_name_to_component = {
                "permissions": {
                    "type": "object",
                    "readOnly": True,
                    "properties": {
                        "staff": {"readOnly": True, "type": "boolean"},
                        "group_manager": {"readOnly": True, "type": "boolean"},
                    },
                },
                "manages": {
                    "readOnly": True,
                    "type": "object",
                    "properties": {
                        "data_providers": {
                            "readOnly": True,
                            "type": "array",
                            "items": {"$ref": "#/components/schemas/DataProvider"},
                        }
                    },
                },
            }
            return field_name_to_component.get(field.field_name, mapped_field)
        return mapped_field


# pylint: disable=too-many-ancestors
@unique_check((UserUniquePermission,))
class UserViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """Show details of registered users."""

    serializer_class = UserSerializer
    permission_classes = (UserDataPermission,)
    filter_backends = (SearchFilter, UserActiveFilter)
    search_fields = ("username", "email")

    def get_queryset(self):
        if (
            self.request.user.is_staff
            or is_tech_account(self.request.user)
            or has_group_manager_groups(self.request.user)
        ):
            return User.objects.all()
        # Restrict unnecessary access to other people data
        return User.objects.filter(username=self.request.user.username)

    def create(self, request, *args, **kwargs):
        # False positive, exists on mixins.CreateModelMixin
        # pylint: disable=no-member
        response = super().create(request, *args, **kwargs)
        created_user = User.objects.get(id=response.data["id"])
        created_user.set_unusable_password()
        created_user.save()
        return response


class UserinfoView(generics.RetrieveAPIView):
    serializer_class = UserinfoSerializer
    permission_classes = (permissions.IsAuthenticated,)
    schema = UserinfoSchema()

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)

    def get_object(self):
        return self.get_queryset()[0]
