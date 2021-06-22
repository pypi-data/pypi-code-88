from functools import lru_cache
from typing import Iterator, List, Union

from .aggregates import Aggregate, Aggregates


__all__ = (
    'get_permission_app_label',
    'get_permission_string',
    'flatten_aggregates',
)


@lru_cache
def get_permission_app_label():
    from .models import Scope

    return Scope._meta.app_label


def get_permission_string(key: str):
    return get_permission_app_label() + '.' + key


def flatten_aggregates(
    aggregates: List[Union['Aggregate', 'Aggregates']]
) -> Iterator['Aggregate']:
    return (
        a
        for agg in aggregates
        for a in (
            (getattr(agg, name) for name in agg._item_names)
            if isinstance(agg, type) and issubclass(agg, Aggregates)
            else (agg,)
        )
    )
