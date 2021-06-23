from ..models.base import BaseResource
from ..models.group_member import GroupMember
from ..resources.mixins import (
    CreateResourceMixin,
    DeleteResouceMixin,
    GetResourceMixin,
    SaveResourceMixin,
)


class GroupMemberResource(
    GetResourceMixin,
    SaveResourceMixin,
    CreateResourceMixin,
    DeleteResouceMixin,
    BaseResource,
):
    def __init__(self, parent: BaseResource):
        super().__init__("members", GroupMember, parent.client)
        self.parent = parent

