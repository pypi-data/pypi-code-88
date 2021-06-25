from typing import List, TypeVar, Union

from ..base import *
from ..models import *
from .mixins import *

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
    def _submodels(self):
        return [GroupMember]

    def members(
        self, identifier=None, **kwargs
    ) -> Union[GroupMember, List[GroupMember]]:
        return self._get(GroupMember, identifier, **kwargs)
