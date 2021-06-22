from typing import Any

from tortoise import fields

from .. import json


class JSONField(fields.JSONField):
    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        super().__init__(encoder=json.fast_dumps, decoder=json.loads, **kwargs)
