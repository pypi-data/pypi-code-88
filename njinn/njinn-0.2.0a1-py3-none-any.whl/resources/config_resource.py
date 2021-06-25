from ..models.base import BaseResource
from ..models.config import Config
from ..njinn_client import NjinnClient
from ..resources.mixins import (
    CreateResourceMixin,
    DeleteResouceMixin,
    GetResourceMixin,
    SaveResourceMixin,
)
from ..resources.utils import ResourceUtil


class ConfigResource(
    GetResourceMixin,
    SaveResourceMixin,
    CreateResourceMixin,
    DeleteResouceMixin,
    BaseResource,
):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/configs", Config, client)

    def duplicate(self, obj: Config, **kwargs) -> Config:
        body = ResourceUtil.exclude_none(kwargs)
        response = self.client.post(f"{self.path}/duplicate", body)
        return self.construct(response)
