from typing import Callable, Any
from .lib import find_attributes


def setter(Class: type) -> type:
    def generate_setter(name: str) -> Callable[Class, Any]:
        def set_value(self, value: Any) -> Any:
            setattr(self, name, value)
        return set_value

    for attribute in find_attributes(Class):
        setter_name = "set_" + attribute.replace(f"_{Class.__name__}__", "")
        setattr(Class, setter_name, generate_setter(attribute))

    return Class
