from typing import List, Union

from .models import *
from .models.mixins import ParentMixin
from .njinn_client import NjinnClient
from .resources import *


class NjinnAPI(ParentMixin):
    _submodels = [
        Workflow,
        Config,
        Execution,
        NjinnGroup,
    ]

    def __init__(
        self, host: str, username: str = None, password: str = None, token: str = None
    ) -> None:
        self.client = NjinnClient(
            host, username=username, password=password, token=token
        )

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
