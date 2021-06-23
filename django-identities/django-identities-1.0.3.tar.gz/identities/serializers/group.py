import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.transaction import atomic
from django_drf_utils.serializers.utils import get_request_username
from guardian.models import GroupObjectPermission
from rest_framework import serializers

from ..permissions import is_staff


logger = logging.getLogger(__name__)
User = get_user_model()

VALIDATION_ERROR_NON_STAFF_FIELDS = (
    "Only staff are allowed to change fields other than `users`"
)


class GroupObjectPermissionSerializer(
    serializers.Serializer
):  # pylint: disable=abstract-method
    permission = serializers.IntegerField()
    objects = serializers.ListField(child=serializers.IntegerField(min_value=1))

    def validate_permission(self, value):  # pylint: disable=no-self-use
        try:
            return Permission.objects.get(pk=value)
        except Permission.DoesNotExist as e:
            raise serializers.ValidationError(
                f"Permission {value} does not exist"
            ) from e

    def validate(self, attrs):  # pylint: disable=no-self-use
        data = super().validate(attrs)
        model = data["permission"].content_type.model_class()
        for obj in data["objects"]:
            try:
                model.objects.get(pk=obj)
            except model.DoesNotExist as e:
                raise serializers.ValidationError(
                    f"Object {obj} does not exist for model {model.__name__}"
                ) from e
        return data


class GroupObjectPermissionListSerializer(
    serializers.ListSerializer
):  # pylint: disable=abstract-method
    def to_representation(self, data):
        output = {}
        for perm in data.all():
            output.setdefault(perm.permission.id, []).append(perm.object_pk)
        return [
            GroupObjectPermissionSerializer({"permission": p, "objects": o}).data
            for p, o in output.items()
        ]


class GroupSerializer(serializers.ModelSerializer):
    permissions_object = GroupObjectPermissionListSerializer(
        child=GroupObjectPermissionSerializer(),
        required=False,
        source="groupobjectpermission_set",
    )
    users = serializers.PrimaryKeyRelatedField(
        many=True, source="user_set", queryset=User.objects.all()
    )

    class Meta:
        model = Group
        fields = ("id", "name", "users", "permissions", "permissions_object")

    def _log_action(self, action: str, queryset):
        if queryset:
            logger.info("%s %s %s", get_request_username(self), action, queryset)

    @staticmethod
    def _transform_object_permissions(permissions):
        return (
            (perm_grp["permission"].content_type, str(obj), perm_grp["permission"])
            for perm_grp in permissions
            for obj in perm_grp["objects"]
        )

    def _create_object_permissions(self, obj_perm, instance: Group):
        created = GroupObjectPermission.objects.bulk_create(
            GroupObjectPermission(
                group=instance, content_type=t, object_pk=o, permission=p
            )
            for t, o, p in obj_perm
        )
        self._log_action("created", created)

    @atomic
    def create(self, validated_data):
        obj_perm = self._transform_object_permissions(
            validated_data.pop("groupobjectpermission_set", ())
        )
        group = super().create(validated_data)
        self._create_object_permissions(obj_perm, group)
        return group

    def _validate_non_staff_changes(self, instance, validated_data, new_perm, old_perm):
        user = get_request_username(self)
        current_permissions = list(instance.permissions.all())
        has_different_name = validated_data.get("name", instance.name) != instance.name
        has_different_permissions = (
            validated_data.get("permissions", current_permissions)
            != current_permissions
        )
        has_different_group_object_permissions = set(old_perm.keys()) != new_perm
        if not is_staff(user) and (
            has_different_name
            or has_different_permissions
            or has_different_group_object_permissions
        ):
            raise serializers.ValidationError(VALIDATION_ERROR_NON_STAFF_FIELDS)

    @atomic
    def update(self, instance, validated_data):
        new_perm = set(
            self._transform_object_permissions(
                validated_data.pop("groupobjectpermission_set", ())
            )
        )
        old_perm = {
            (p.content_type, p.object_pk, p.permission): p.pk
            for p in GroupObjectPermission.objects.filter(group=instance)
        }

        self._validate_non_staff_changes(instance, validated_data, new_perm, old_perm)

        self._create_object_permissions(new_perm - set(old_perm.keys()), instance)
        to_be_removed = GroupObjectPermission.objects.filter(
            pk__in=[
                v for k, v in old_perm.items() if k in set(old_perm.keys()) - new_perm
            ]
        )
        self._log_action("deleted", list(to_be_removed))
        to_be_removed.delete()
        return super().update(instance, validated_data)
