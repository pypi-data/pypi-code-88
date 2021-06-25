from typing import List, Type, TypeVar

from ..base import *

T = TypeVar("T")


class ParentMixin:
    @property
    def _context(self):
        if issubclass(type(self), BaseModel):
            return self.api_resource
        return self.client

    def create(self, obj: T) -> T:
        self._guard_creation(type(obj))
        return obj._refresh(self._init_subresource(type(obj)).create(obj))

    def _get(self, model_class: Type, identifier=None, **kwargs) -> T:
        return self._init_subresource(model_class).get(identifier, **kwargs)

    def _init_subresource(self, model_class: Type):
        return ResourceUtil(Mapping.lookup_resource(model_class), self._context)

    def _guard_creation(self, model_class: Type):
        types_with_create = [
            type
            for type in self._submodels
            if hasattr(Mapping.lookup_resource(type), "create")
        ]

        if model_class not in types_with_create:
            message = f"{model_class.__name__} cannot be created from {self.__class__.__name__}."
            message += f" Valid options: {', '.join([type.__name__ for type in types_with_create])}"
            raise NotImplementedError(message)


class SaveModelMixin(BaseModel):
    def save(self: T, fields: List = None) -> T:
        return self._refresh(self.api_resource.save(self, fields))


class DeleteModelMixin(BaseModel):
    def delete(self):
        return self.api_resource.delete(self)
