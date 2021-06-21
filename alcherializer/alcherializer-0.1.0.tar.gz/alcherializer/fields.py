from typing import Any, List, Tuple, Union
import sqlalchemy


class BaseField:

    def __init__(self, name: str = None, field: sqlalchemy.Column = None):
        self.name = name
        self.field = field

    def cast(self, value) -> Any:
        return value

    def run_validator(self, value: Any) -> Tuple[bool, List[str]]:
        errors = []
        for method_name in dir(self):
            if not method_name.startswith("check_if_"):
                continue

            executable = getattr(self, method_name)

            cast_value = self.cast(value)
            ok, error = executable(cast_value)
            if not ok:
                errors.append(error)

        return len(errors) <= 0, errors

    def check_if_required_and_filled(self, value) -> Tuple[bool, Union[str, None]]:
        if not self.field.nullable and (value is None or value == ""):
            return False, "Can't be blank"

        return True, None


class IntegerField(BaseField):

    def cast(self, value) -> int:
        if value is None:
            return 0

        return int(value)


class StringField(BaseField):

    def cast(self, value) -> str:
        if value is None:
            return ""

        return str(value)

    def check_if_length_is_under_limit(self, value: str) -> Tuple[bool, Union[str, None]]:
        if self.field.type.length and len(value) > self.field.type.length:
            return False, f"Limit of characters is {self.field.type.length}"

        return True, None
