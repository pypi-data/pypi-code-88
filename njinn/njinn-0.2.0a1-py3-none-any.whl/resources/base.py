from typing import Type

from ..njinn_client import NjinnClient


class BaseResource:
    def __init__(self, path: str, instance_class: Type, client: NjinnClient) -> None:
        self._path = path
        self.instance_class = instance_class
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
        return self.instance_class(api_resource=self, **response)
