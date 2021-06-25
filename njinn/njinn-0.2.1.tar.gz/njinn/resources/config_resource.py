from ..base import *
from ..models import *
from ..njinn_client import NjinnClient
from .mixins import *


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


Mapping.register(Config, ConfigResource)
