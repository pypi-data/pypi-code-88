import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import transaction
from django_drf_utils.serializers.utils import get_request_username
from rest_framework import serializers
from rest_framework.exceptions import MethodNotAllowed

from ..serializers.profile import ProfileSerializer


logger = logging.getLogger(__name__)
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)
    groups = serializers.SlugRelatedField(
        slug_field="name",
        read_only=False,
        many=True,
        required=False,
        queryset=Group.objects.all(),
    )

    class Meta:
        model = User
        read_only_fields = (
            "id",
            "username",
            "last_login",
        )
        fields = read_only_fields + (
            "profile",
            "email",
            "first_name",
            "last_name",
            "groups",
            "is_active",
        )

    @transaction.atomic
    def update(self, instance, validated_data):
        if "groups" in validated_data:
            instance.groups.set(validated_data["groups"])
        if (
            "is_active" in validated_data
            and validated_data["is_active"] != instance.is_active
        ):
            request_user = get_request_username(self)
            logger.info(
                "User (ID: %s) changed `is_active` of user (ID: %s) from %s to %s",
                request_user.id,
                instance.id,
                instance.is_active,
                validated_data["is_active"],
            )
            instance.is_active = validated_data["is_active"]

            if not instance.is_active:
                # remove all associations to user
                # remove all permissions
                instance.groups.clear()
                instance.user_permissions.clear()

        instance.save()
        return instance

    def create(self, validated_data):
        if "profile" in validated_data:
            del validated_data["profile"]
        validated_data["username"] = validated_data["email"]
        return super().create(validated_data)


class UserShortSerializer(serializers.ModelSerializer):
    """A read-only user serializer."""

    affiliation = serializers.CharField(source="profile.affiliation", read_only=True)
    affiliation_id = serializers.CharField(
        source="profile.affiliation_id", read_only=True
    )

    class Meta:
        model = User
        read_only_fields = (
            "username",
            "email",
            "last_name",
            "first_name",
            "affiliation",
            "affiliation_id",
        )
        fields = read_only_fields

    # Make sure that this serializer is NOT used for POST or PUT requests

    def create(self, validated_data):
        raise MethodNotAllowed(method="POST")

    def update(self, instance, validated_data):
        raise MethodNotAllowed(method="PUT")
