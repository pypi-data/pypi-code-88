from typing import Any

from .base import BaseModel


class MockModel(BaseModel):
    class Meta:
        abstract = True

    async def save(self, *args: Any, **kwargs: Any):
        pass

    async def delete(self, *args: Any, **kwargs: Any):
        pass
