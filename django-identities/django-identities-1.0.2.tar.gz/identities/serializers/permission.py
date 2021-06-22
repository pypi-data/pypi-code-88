from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


# It can serialize an instance of any django.db.models.Model
class AnyObjectSerializer(serializers.Serializer):  # pylint: disable=abstract-method
    id = serializers.IntegerField(read_only=True, min_value=1)
    name = serializers.SerializerMethodField()

    def get_name(self, obj):  # pylint: disable=no-self-use
        return str(obj)


# It can serialize an instance of any django.db.models.Model
class AnyObjectByPermissionSerializer(
    serializers.Serializer
):  # pylint: disable=abstract-method
    perm_id = serializers.IntegerField(read_only=True, min_value=1)
    obj_id = serializers.IntegerField(read_only=True, min_value=1)
    name = serializers.CharField(read_only=True)
