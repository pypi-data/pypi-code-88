import functools
import warnings

from typing import Callable


def deprecated_alias(alias_name: str) -> Callable:
    """Decorate a function to raise a deprecation warning before being called.

    This is meant to be used as follows :

    .. code-block: python

       alias = deprecated_function("alias")(decorated_function)

    The warning will indicate that ``alias_name`` is an alias and that
    ``decorated_function`` is the new name that should be used.

    :param alias_name: name of the alias for the decorated function.
    """
    def deco(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            warnings.warn(
                f"{alias_name} is a deprecated alias for {f.__name__}"
                f"and will be removed; use {f.__name__} instead.",
                DeprecationWarning,
            )
            return f(*args, **kwargs)

        return wrapper

    return deco
