from typing import List, Union

from ..scopes import ScopeRegistry
from ..aggregates import Aggregate, Aggregates
from .permissions import generate_permissions
from .groups import generate_group


__all__ = 'generate_all',


def generate_all(
    registries: List[ScopeRegistry],
    aggregates: List[Union[Aggregate, Aggregates]],
):
    for registry in registries:
        generate_permissions(registry)

    aggregates = (
        a
        for agg in aggregates
        for a in (
            (getattr(agg, name) for name in agg._item_names)
            if isinstance(agg, type) and issubclass(agg, Aggregates)
            else (agg,)
        )
    )

    for aggregate in aggregates:
        generate_group(aggregate)
