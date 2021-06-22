from django.contrib.auth.models import Group
from django_drf_utils.views.utils import unique_check
from rest_framework import viewsets

from ..serializers import GroupSerializer
from ..permissions import (
    IsGroupManagerRead,
    IsGroupManagerWrite,
    IsStaff,
    get_group_manager_groups,
)


@unique_check((IsStaff,))
class GroupViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    # pylint: disable=unsupported-binary-operation
    permission_classes = (IsStaff | IsGroupManagerRead | IsGroupManagerWrite,)

    def get_queryset(self):
        requestor = self.request.user
        if requestor.is_staff:
            return Group.objects.all()
        return get_group_manager_groups(requestor)
