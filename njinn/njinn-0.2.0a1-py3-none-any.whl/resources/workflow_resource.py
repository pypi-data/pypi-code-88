from ..models.base import BaseResource
from ..models.execution import Execution
from ..models.workflow import Workflow
from ..njinn_client import NjinnClient
from ..resources.execution_resource import ExecutionResource
from ..resources.mixins import (
    CreateResourceMixin,
    DeleteResouceMixin,
    GetResourceMixin,
    SaveResourceMixin,
)
from ..resources.utils import ResourceUtil


class WorkflowResource(
    GetResourceMixin,
    SaveResourceMixin,
    CreateResourceMixin,
    DeleteResouceMixin,
    BaseResource,
):
    def __init__(self, client: NjinnClient):
        super().__init__("api/v1/workflows", Workflow, client)

    def run(self, obj: Workflow, **kwargs) -> Execution:
        body = ResourceUtil.exclude_none(kwargs)
        response = self.client.post(f"{self.path}/run", body)
        return ExecutionResource(self.client).construct(response)

    def duplicate(self, obj: Workflow, **kwargs) -> Workflow:
        body = ResourceUtil.exclude_none(kwargs)
        response = self.client.post(f"{self.path}/duplicate", body)
        return self.construct(response)
