from typing import Callable, Any
from .lib import find_attributes


def getter(Class: type) -> type:
    def generate_getter(name: str) -> Callable[Class, Any]:
        def get_value(self) -> Any:
            return getattr(self, name)
        return get_value

    for attribute in find_attributes(Class):
        getter_name = "get_" + attribute.replace(f"_{Class.__name__}__", "")
        setattr(Class, getter_name, generate_getter(attribute))

    return Class
