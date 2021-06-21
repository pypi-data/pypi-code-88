from typing import Any, Dict
import sqlalchemy
from alcherializer import fields
from alcherializer.exceptions import MalformedMetaClassException


class Serializer:

    def __init__(self, instance=None, data=None, **kwargs):
        if not hasattr(self, "Meta") or not hasattr(self.Meta, "model"):
            raise MalformedMetaClassException("Serializer bad definition")

        self.meta = getattr(self, "Meta")

        self.errors = {}
        self.fields = self._get_fields()
        self.instance = instance
        self.initial_data = {} if not data else data
        self.many = kwargs.get("many", False)
        self.partial = kwargs.get("partial", False)
        self.validated_data = {}

    @property
    def data(self) -> Dict[str, Any]:
        instances = self.instance if self.many else [self.instance]

        results = []
        for instance in instances:
            obj_dict = {}
            for key in self.fields.keys():
                obj_dict[key] = getattr(instance, key)

            results.append(obj_dict)

        return results if self.many else results[0]

    def clear(self) -> None:
        self.errors = {}
        self.validated_data = {}

    def is_valid(self) -> bool:
        for key, field in self.fields.items():
            if key in getattr(self.meta, "except_fields", ["id"]):
                continue

            value = self._get_value(key)
            valid, errors = field.get("validator").run_validator(value)
            if not valid:
                self.errors[key] = errors
                continue

            self.validated_data[key] = value

        return self._has_errors()

    def _get_value(self, key: str) -> Any:
        return self.initial_data.get(key)

    def _has_errors(self) -> bool:
        return len(self.errors.keys()) <= 0

    def _get_fields(self) -> Dict[str, Any]:
        columns = {}
        for key, value in self.meta.model.__dict__.items():
            if key.startswith("__"):
                continue

            columns[key] = {
                "type": value.type,
                "required": value.nullable is False,
                "validator": self._get_field_validator(key, value)
            }

        return columns

    def _get_field_validator(self, key: str, field):
        if hasattr(self, key):
            validator = getattr(self, key)
            validator.name = key
            validator.field = field

            return validator

        if isinstance(field.type, sqlalchemy.String):
            return fields.StringField(key, field)

        if isinstance(field.type, sqlalchemy.Integer):
            return fields.IntegerField(key, field)

        return fields.BaseField(key, field)
