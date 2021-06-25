from typing import TypeVar

from ..models.base import BaseModel
from ..models.mixins import DeleteModelMixin, SaveModelMixin

T = TypeVar("T")


class Config(SaveModelMixin, DeleteModelMixin, BaseModel):
    def __init__(
        self,
        url=None,
        id=None,
        project=None,
        name=None,
        title=None,
        values=None,
        config_scheme=None,
        labels=None,
        description=None,
        version=None,
        updated_by=None,
        updated_at=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.url = url
        self.id = id
        self.project = project
        self.name = name
        self.title = title
        self.values = values
        self.config_scheme = config_scheme
        self.labels = labels
        self.description = description
        self.version = version
        self.updated_by = updated_by
        self.updated_at = updated_at

        self._read_only = [
            "url",
            "id",
            "version",
            "update_by",
            "update_at",
        ]

    def duplicate(self: T, name=None, title=None) -> T:
        return self.api_resource.duplicate(self, name=name, title=title)
