from typing import List, Type, TypeVar

from ..models.base import BaseModel
from ..resources.utils import ResourceUtil

T = TypeVar("T")


class ParentMixin:
    @property
    def _context(self):
        if issubclass(type(self), BaseModel):
            return self.api_resource
        return self.client

    def create(self, obj: T) -> T:
        self._guard_subresource(type(obj))
        return obj._refresh(self._init_subresource(type(obj)).create(obj))

    def _get(self, instance_class: Type, identifier=None, **kwargs) -> T:
        return self._init_subresource(instance_class).get(identifier, **kwargs)

    def _init_subresource(self, instance_class: Type):
        return ResourceUtil(self._subresources[instance_class], self._context)

    def _guard_subresource(self, instance_class: Type):
        types_with_create = [
            type
            for type in self._subresources
            if hasattr(self._subresources[type], "create")
        ]

        if instance_class not in types_with_create:
            message = f"{instance_class.__name__} cannot be created from {self.__class__.__name__}."
            message += f" Valid options: {', '.join([type.__name__ for type in types_with_create])}"
            raise NotImplementedError(message)


class SaveModelMixin(BaseModel):
    def save(self: T, fields: List = None) -> T:
        return self._refresh(self.api_resource.save(self, fields))


class DeleteModelMixin(BaseModel):
    def delete(self):
        return self.api_resource.delete(self)
