from ..models.base import BaseResource
from ..models.njinn_group import NjinnGroup
from ..njinn_client import NjinnClient
from ..resources.mixins import (
    CreateResourceMixin,
    DeleteResouceMixin,
    GetResourceMixin,
    SaveResourceMixin,
)


class NjinnGroupResource(
    GetResourceMixin,
    SaveResourceMixin,
    CreateResourceMixin,
    DeleteResouceMixin,
    BaseResource,
):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/groups", NjinnGroup, client)
