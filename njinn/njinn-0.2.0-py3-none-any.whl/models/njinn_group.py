from typing import List, TypeVar, Union

from ..models.base import BaseModel
from ..models.group_member import GroupMember
from ..models.mixins import DeleteModelMixin, ParentMixin, SaveModelMixin

T = TypeVar("T")


class NjinnGroup(ParentMixin, SaveModelMixin, DeleteModelMixin, BaseModel):
    def __init__(
        self,
        id=None,
        name=None,
        permissions=None,
        group_members=None,
        created_at=None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.id = id
        self.name = name
        self.permissions = permissions
        self.group_members = group_members
        self.created_at = created_at

        self._read_only = ["id", "created_at"]

    @property
    def _subresources(self):
        from ..resources.group_member_resource import GroupMemberResource

        return {GroupMember: GroupMemberResource}

    def members(
        self, identifier=None, **kwargs
    ) -> Union[GroupMember, List[GroupMember]]:
        return self._get(GroupMember, identifier, **kwargs)
