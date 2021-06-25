from ..base import *
from ..models import *
from ..njinn_client import NjinnClient
from .mixins import *


class NjinnGroupResource(
    GetResourceMixin,
    SaveResourceMixin,
    CreateResourceMixin,
    DeleteResouceMixin,
    BaseResource,
):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/groups", NjinnGroup, client)

Mapping.register(NjinnGroup, NjinnGroupResource)
