from typing import List, Union

from px_access_scopes.utils import flatten_aggregates

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

    aggregates = flatten_aggregates(aggregates)

    for aggregate in aggregates:
        generate_group(aggregate)
