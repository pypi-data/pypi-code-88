import typing
import dacite
from dacite.dataclasses import Field, _FIELDS, _FIELD, _FIELD_INITVAR

T = typing.TypeVar("T", bound=typing.Any)


def from_dict(data_class, data):

    def get_fields(data_class: typing.Type[T]) -> typing.List[Field]:
        fields = getattr(data_class, _FIELDS)
        return [f for f in fields.values() if f._field_type is _FIELD or f._field_type is _FIELD_INITVAR]

    fields = get_fields(data_class=data_class)
    data_copy = {}
    for key, value in data.items():
        for field in fields:
            if key.lower() == field.name.lower():
                data_copy[field.name] = value

    return dacite.from_dict(data_class=data_class, data=data_copy)
