""" A collection of caching function and decorators that are used troughout the
module to save time and avoid duplicate web requests. """

import typing
from time import time
from dataclasses import dataclass, field

__all__ = ['cache_for', 'cache_forever']

SECONDS_IN_UNITS = {
    1: {'s', 'sec', 'secs', 'second', 'seconds', },
    60: {'m', 'min', 'mins', 'minute', 'minutes', },
    60 * 60: {'h', 'hr', 'hrs', 'hour', 'hours', },
}


def unit_to_seconds(unit: str) -> int:
    for to_seconds, unit_set in SECONDS_IN_UNITS.items():
        if unit in unit_set:
            return to_seconds

    raise ValueError(f'Invalid time unit {unit!r}')


@dataclass(frozen=True)
class CacheValue:
    """ A dataclass that represents a single caches value.
    Each cache contains """

    value: typing.Any
    cache_for: float
    _created: float = field(init=False)

    def __post_init__(self,) -> None:
        object.__setattr__(self, '_created', time())

    @property
    def expired(self,) -> bool:
        """ A boolean value: `True` if the saved cache value is expired,
        and `False` if the cache is still valid. """
        return time() - self._created > self.cache_for


def cache_for(amount: float, unit: str = 's'):
    """ A decorator that caches the return value of a function for a certion amount
    of time. When the cache 'expires', the function is called again and the timer
    resets. """

    wait_for = amount * unit_to_seconds(unit)

    def decorator(func):
        caches: typing.Dict[tuple, CacheValue] = dict()

        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            cache = caches.get(key)

            if cache is None or cache.expired:
                caches[key] = CacheValue(
                    value=func(*args, **kwargs),
                    cache_for=wait_for,
                )

            return caches[key].value

        return wrapper
    return decorator


cache_forever = cache_for(float('inf'))
