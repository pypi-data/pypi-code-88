from typing import Optional, Tuple, Union
from px_access_scopes import Aggregate as BaseAggregate, Aggregates

from .scopes import ScopeDomain, ScopeEnum


__all__ = 'Aggregate', 'Aggregates',

# Group identifier must be in a range of {2000 - 4000}
# to avoid id collisions with an existing database ids.
# It will be better to initially create aggregates with larger ids
# and the newer they are - the lower they become.
# It's because of id autoincrement database mechanics.
GROUP_IDS_RANGE = (2000, 5000)
AggregateValue = Union[ScopeDomain, ScopeEnum]


class Aggregate(BaseAggregate):
    """Set with additional config parameters."""

    _group_ids_range: Tuple[int, int] = GROUP_IDS_RANGE
    group_id: int
    name: str
    verbose_name: str

    def __init__(
        self,
        group_id: int,
        name: Optional[str] = None,
        verbose_name: Optional[str] = None,
        *args
    ) -> None:
        lowest, highest = self._group_ids_range
        assert lowest <= group_id <= highest, (
            f'Group identifier must be in a range of {lowest}-{highest} '
            'to avoid id collisions with an existing database ids.'
        )

        super().__init__(name=name or group_id, *args)
        self.group_id = group_id
        self.verbose_name = verbose_name or self.name
