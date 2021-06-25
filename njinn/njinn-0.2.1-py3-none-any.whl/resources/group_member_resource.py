from ..base import *
from ..models import *
from .mixins import *


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

Mapping.register(GroupMember, GroupMemberResource)
