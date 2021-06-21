from typing import Tuple, Callable, Type, Union, TypeVar
import inspect
from dataclasses import is_dataclass, fields


class Secret(str):
    """A class to mark arguments as sensitive"""

    def __repr__(self):
        return "***"

    def __format__(self, format_spec):
        return str.__format__("***", format_spec)


def enforce_secret_by_signature(
    f: Callable, args: tuple, kwargs: dict
) -> Tuple[tuple, dict]:
    sig = inspect.signature(f)
    sanitized_kwargs = {
        key: enforce_secret(val, sig.parameters[key].annotation)
        for key, val in kwargs.items()
    }
    sanitized_args = tuple(
        enforce_secret(val, prm.annotation)
        for val, prm in zip(args, sig.parameters.values())
    )
    return sanitized_args, sanitized_kwargs


T = TypeVar("T")


def enforce_secret(val: T, t: Type) -> Union[T, Secret]:
    if t is Secret or (  # check for Optional / Union:
        getattr(t, "__origin__", None) is Union
        and Secret in t.__args__
        and isinstance(val, str)
    ):
        return Secret(val)
    if is_dataclass(val) and issubclass(type(val), t):
        t = type(val)
    if is_dataclass(t):
        for f in fields(t):
            original_val = getattr(val, f.name)
            sanitized_val = enforce_secret(original_val, f.type)
            if original_val is not sanitized_val:
                setattr(val, f.name, sanitized_val)
    return val
