from ..base import *
from .mixins import *


class GroupMember(SaveModelMixin, DeleteModelMixin, BaseModel):
    def __init__(self, user=None, group=None, **kwargs):
        super().__init__(**kwargs)
        self.user = user
        self.group = group

        self._read_only = []

    @property
    def api_identifier(self):
        return self.user
