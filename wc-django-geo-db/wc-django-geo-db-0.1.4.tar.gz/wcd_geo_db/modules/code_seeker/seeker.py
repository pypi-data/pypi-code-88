from typing import Any, Optional
from django.db import models


__all__ = (
    'DEFAULT_CODES_FIELD', 'CodeSeeker',
)


DEFAULT_CODES_FIELD = 'codes'


def s_default(self, name: str, value = None):
    return getattr(self, name, None) if value is None else value


class CodeSeeker:
    name: str
    field_name: str = DEFAULT_CODES_FIELD

    def __init__(
        self, *_, name: Optional[str] = None, field_name: Optional[str] = None
    ):
        self.name = s_default(self, 'name', name)
        self.field_name = s_default(self, 'field_name', field_name)

    def Q(self, value: Any, field_name: Optional[str] = None) -> models.Q:
        return models.Q(**{
            f'{field_name or self.field_name}__contains': {self.name: value}
        })

    def eq(self, a: Any, b: Any) -> bool:
        return a == b

    def ge(self, a: Any, b: Any) -> bool:
        return a > b

    def __hash__(self) -> int:
        return self.name.__hash__()


