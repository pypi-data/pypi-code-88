from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.schemas.openapi import AutoSchema

from identities.apps import APP_NAME as IDENTITIES_APP_NAME
from identities.permissions import IsGroupManagerRead
from identities.serializers import AnyObjectSerializer, PermissionSerializer
from identities.permissions import IsStaff


class GenericObjectSchema(AutoSchema):
    def get_responses(self, path, method):
        print(path, method)
        responses = super().get_responses(path, method)
        responses["200"]["content"]["application/json"]["schema"] = {
            "type": "array",
            "items": {
                "$ref": responses["200"]["content"]["application/json"]["schema"][
                    "$ref"
                ]
            },
        }
        return responses


class ObjectByPermissionSchema(AutoSchema):
    def get_filter_parameters(self, path, method):
        if method == "GET":
            return [
                {
                    "name": "perm_id",
                    "in": "query",
                    "required": True,
                    "description": (
                        "Permission ids for which available "
                        "objects should be returned"
                    ),
                    "schema": {"type": "array", "items": {"type": "integer"}},
                },
            ]
        return []


# pylint: disable=too-many-ancestors
class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    # pylint: disable=unsupported-binary-operation
    permission_classes = (IsStaff | IsGroupManagerRead,)

    def get_serializer_class(self):
        if self.action == "objects":
            return AnyObjectSerializer
        return PermissionSerializer

    def get_queryset(self):
        content_types = [
            x.id
            for x in ContentType.objects.filter(
                app_label__in=(IDENTITIES_APP_NAME, "auth")
            ).exclude(model__startswith="historical")
        ]
        return Permission.objects.filter(content_type__in=content_types)

    @action(detail=True, schema=GenericObjectSchema())
    def objects(self, request, pk=None):  # pylint: disable=unused-argument
        return Response(
            AnyObjectSerializer(
                self.get_object().content_type.get_all_objects_for_this_type(),
                many=True,
            ).data
        )


class ObjectByPermissionViewSet(viewsets.ViewSet):
    # pylint: disable=unsupported-binary-operation
    permission_classes = (IsStaff | IsGroupManagerRead,)
    schema = ObjectByPermissionSchema()

    def list(self, request):  # pylint: disable=no-self-use
        permissions = Permission.objects.filter(
            pk__in=request.query_params.getlist("perm_id")
        )
        return Response(
            {
                p.id: AnyObjectSerializer(
                    p.content_type.get_all_objects_for_this_type(),
                    many=True,
                ).data
                for p in permissions
            }
        )
