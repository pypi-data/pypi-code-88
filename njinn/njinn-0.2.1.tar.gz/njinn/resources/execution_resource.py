from ..base import *
from ..models import *
from ..njinn_client import NjinnClient
from .mixins import *


class ExecutionResource(GetResourceMixin, SaveResourceMixin, BaseResource):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/executions", Execution, client)


Mapping.register(Execution, ExecutionResource)
