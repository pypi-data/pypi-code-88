from typing import List

from ..base import *


class GetResourceMixin(BaseResource):
    def get(self, identifier=None, **kwargs):
        if identifier is None:
            response = self.client.get(self.path, params=kwargs)
            if response.get("results"):
                return [self.construct(entity) for entity in response.get("results")]
            return [self.construct(response[key]) for key in response]
        else:
            self.identifier = identifier
            response = self.client.get(f"{self.path}")
            return self.construct(response)


class SaveResourceMixin(BaseResource):
    def save(self, obj: BaseModel, fields: List = None):
        if fields:
            body = ResourceUtil.extract_body(obj, fields)
            response = self.client.patch(f"{self.path}", body)
        else:
            body = ResourceUtil.extract_body(obj)
            response = self.client.put(f"{self.path}", body)

        return self.construct(response)


class CreateResourceMixin(BaseResource):
    def create(self, obj: BaseModel):
        body = ResourceUtil.extract_body(obj)
        body = ResourceUtil.exclude_none(body)

        response = self.client.post(f"{self.path}", body)
        return self.construct(response)


class DeleteResouceMixin(BaseResource):
    def delete(self, obj: BaseModel):
        return self.client.delete(f"{self.path}")
