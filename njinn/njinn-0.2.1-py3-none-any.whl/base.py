from copy import deepcopy
from typing import List, Type, TypeVar, Union

T = TypeVar("T")

from .njinn_client import NjinnClient


class BaseResource:
    def __init__(self, path: str, model_class: Type, client: NjinnClient) -> None:
        self._path = path
        self.model_class = model_class
        self.client = client
        self.identifier = None

    @property
    def path(self) -> str:
        def with_identifier():
            return f"/{self.identifier}" if self.identifier else ""

        parent = getattr(self, "parent", None)
        if parent:
            return f"{parent.path}/{self._path}{with_identifier()}"
        return f"{self._path}{with_identifier()}"

    def construct(self, response):
        return self.model_class(api_resource=self, **response)


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
                    f"{self} does not have '_api_resource'. Object needs to be created by NjinnAPI or parent resource first."
                )
            raise Exception(f"{self} does not have '_api_resource'")

        def renew_api_resource():
            if self._api_resource.identifier != self.api_identifier:
                self._api_resource = deepcopy(self._api_resource)
                self._api_resource.identifier = self.api_identifier
            return self._api_resource

        return renew_api_resource()

    @property
    def _submodels(self):
        return []

    def refresh(self: T) -> T:
        return self._refresh(self.api_resource.get(self.api_identifier))

    def _refresh(self: T, instance: T) -> T:
        for attr in self.__dict__:
            if hasattr(instance, attr):
                self.__setattr__(attr, deepcopy(getattr(instance, attr)))

        return self


class Mapping:
    _resource_map = {}

    @staticmethod
    def register(model_class: Type, resource_class):
        Mapping._resource_map[model_class] = resource_class

    @staticmethod
    def lookup_resource(model_class: Type) -> Type:
        if model_class in Mapping._resource_map.keys():
            return Mapping._resource_map[model_class]

        raise NotImplementedError(f"{model_class} has no backing resource")


class ResourceUtil:
    def __init__(
        self,
        resource_class: Type[BaseResource],
        context: Union[NjinnClient, BaseResource],
    ):
        self.resource_class = resource_class
        self.context = context

    def get(self, identifier=None, **kwargs) -> Union[BaseModel, List[BaseModel]]:

        resource = self.resource_class(self.context)
        return resource.get(identifier, **kwargs)

    def create(self, obj: BaseModel) -> BaseModel:
        resource = self.resource_class(self.context)
        return resource.create(obj)

    @classmethod
    def exclude_none(cls, body: dict):
        return {key: body[key] for key in body if body[key] is not None}

    @classmethod
    def extract_body(cls, obj: BaseModel, fields: List = None):
        copy = obj.__dict__.copy()
        if fields:
            return {key: copy[key] for key in fields}
        else:
            return {
                key: copy[key] for key in copy.keys() - (obj._read_only + obj._internal)
            }
