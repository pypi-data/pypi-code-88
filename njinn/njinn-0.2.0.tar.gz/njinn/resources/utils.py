from typing import List, Type, Union

from ..models.base import BaseModel, BaseResource
from ..njinn_client import NjinnClient


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
