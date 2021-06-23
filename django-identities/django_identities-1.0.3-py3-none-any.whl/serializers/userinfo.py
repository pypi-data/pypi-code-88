import logging

from django.contrib.auth import get_user_model
from rest_framework import serializers

from ..permissions import has_group_manager_groups
from ..serializers.profile import ProfileSerializer


logger = logging.getLogger(__name__)
User = get_user_model()


class UserinfoSerializer(serializers.ModelSerializer):
    # Sets `required: true` in the OpenAPI schema
    id = serializers.IntegerField(required=True)
    profile = ProfileSerializer(read_only=True)
    ip_address = serializers.SerializerMethodField()
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        read_only_fields = ("ip_address", "permissions")
        fields = read_only_fields + (
            "username",
            "email",
            "first_name",
            "last_name",
            "profile",
            "id",
        )

    def get_ip_address(self, _: User):
        request = self.context["request"]
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            return x_forwarded_for.split(",")[0]
        return request.META.get("REMOTE_ADDR")

    def get_permissions(self, _: User):
        request = self.context["request"]
        return {
            "staff": request.user.is_staff,
            "group_manager": has_group_manager_groups(request.user),
        }
