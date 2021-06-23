from ..models.base import BaseResource
from ..models.execution import Execution
from ..njinn_client import NjinnClient
from ..resources.mixins import GetResourceMixin, SaveResourceMixin


class ExecutionResource(GetResourceMixin, SaveResourceMixin, BaseResource):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/executions", Execution, client)
