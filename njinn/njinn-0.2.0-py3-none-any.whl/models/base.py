from copy import deepcopy
from typing import TypeVar

from ..resources.base import BaseResource

T = TypeVar("T")


class BaseModel:
    _internal = ["_api_resource", "_read_only"]

    def __init__(self, api_resource: BaseResource = None, **kwargs) -> None:
        self._api_resource = api_resource
        self._read_only = []

    @property
    def api_identifier(self):
        return getattr(self, "id", None)

    @property
    def api_resource(self) -> BaseResource:
        if self._api_resource is None:
            if self.api_identifier is None:
                raise Exception(
                    f"{self} does not have '_api_resource'. Object needs to be created by NjinnApi or parent resource first."
                )
            raise Exception(f"{self} does not have '_api_resource'")

        def renew_api_resource():
            if self._api_resource.identifier != self.api_identifier:
                self._api_resource = deepcopy(self._api_resource)
                self._api_resource.identifier = self.api_identifier
            return self._api_resource

        return renew_api_resource()

    @property
    def _subresources(self):
        return {}

    def refresh(self: T) -> T:
        return self._refresh(self.api_resource.get(self.api_identifier))

    def _refresh(self: T, instance: T) -> T:
        for attr in self.__dict__:
            if hasattr(instance, attr):
                self.__setattr__(attr, deepcopy(getattr(instance, attr)))

        return self
