from typing import List, Union

from .scopes import ScopeRegistry
from .aggregates import Aggregate, Aggregates


__all__ = 'registries', 'aggregates'

registries: List[ScopeRegistry] = []
aggregates: List[Union[Aggregate, Aggregates]] = []
