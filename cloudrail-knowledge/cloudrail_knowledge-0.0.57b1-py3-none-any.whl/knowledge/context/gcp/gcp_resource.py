from abc import abstractmethod
from typing import Optional, List

from cloudrail.knowledge.context.gcp.constants.gcp_resource_type import GcpResourceType
from cloudrail.knowledge.context.mergeable import Mergeable


class GcpResource(Mergeable):

    def __init__(self, resource_type: GcpResourceType):
        super().__init__()
        self.tf_resource_type: GcpResourceType = resource_type
        self._id: str = None
        self._self_link: str = None

    @abstractmethod
    def get_keys(self) -> List[str]:
        pass

    def get_cloud_resource_url(self) -> Optional[str]:
        return self._self_link

    def get_friendly_name(self) -> str:
        if self.iac_state:
            return self.iac_state.address
        return self.get_name() or self.get_id()

    @property
    @abstractmethod
    def is_tagable(self) -> bool:
        pass

    def get_id(self) -> str:
        return self._id

    def set_id(self, _id: str):
        self._id = _id
