from typing import List, Union

from .models.config import Config
from .models.execution import Execution
from .models.mixins import ParentMixin
from .models.njinn_group import NjinnGroup
from .models.workflow import Workflow
from .njinn_client import NjinnClient
from .resources.config_resource import ConfigResource
from .resources.execution_resource import ExecutionResource
from .resources.njinn_group_resource import NjinnGroupResource
from .resources.workflow_resource import WorkflowResource


class NjinnApi(ParentMixin):
    _subresources = {
        Workflow: WorkflowResource,
        Config: ConfigResource,
        Execution: ExecutionResource,
        NjinnGroup: NjinnGroupResource,
    }

    def __init__(self, host: str, username: str, password: str) -> None:
        self.client = NjinnClient(host, username, password)

    def workflows(self, identifier=None, **kwargs) -> Union[Workflow, List[Workflow]]:
        return self._get(Workflow, identifier, **kwargs)

    def configs(self, identifier=None, **kwargs) -> Union[Config, List[Config]]:
        return self._get(Config, identifier, **kwargs)

    def executions(
        self, identifier=None, **kwargs
    ) -> Union[Execution, List[Execution]]:
        return self._get(Execution, identifier, **kwargs)

    def groups(self, identifier=None, **kwargs) -> Union[NjinnGroup, List[NjinnGroup]]:
        return self._get(NjinnGroup, identifier, **kwargs)
