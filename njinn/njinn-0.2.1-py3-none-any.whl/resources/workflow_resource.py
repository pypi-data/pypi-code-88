from ..base import *
from ..models import *
from ..njinn_client import NjinnClient
from .mixins import *


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
        return Mapping.lookup_resource(Execution)(self.client).construct(response)

    def duplicate(self, obj: Workflow, **kwargs) -> Workflow:
        body = ResourceUtil.exclude_none(kwargs)
        response = self.client.post(f"{self.path}/duplicate", body)
        return self.construct(response)


Mapping.register(Workflow, WorkflowResource)
