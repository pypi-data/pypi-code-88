from abc import ABCMeta, abstractmethod
from typing import Any, Dict, Mapping, Optional

from panza.internals.workspace import BaseJobWorkspaceHandle


class Backend(metaclass=ABCMeta):
    @abstractmethod
    async def build_environment(self, tag: str, job: BaseJobWorkspaceHandle):
        pass

    @abstractmethod
    async def run(
            self,
            context: Mapping[str, Any],
            environment_tag: str,
            job: BaseJobWorkspaceHandle,
            timeout: Optional[float]
    ) -> Dict[str, Any]:
        pass
