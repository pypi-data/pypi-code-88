from collections import UserDict

from ..models.base import BaseModel


class Task(BaseModel, UserDict):
    def __init__(self, dict, **kwargs) -> None:
        super().__init__(**kwargs)
        self.data = {}
        if dict is not None:
            self.update(dict)

    @property
    def api_identifier(self):
        return self.get("name", None)
