from typing import Any, List, Optional, Sequence, TypeVar

from wcd_geo_db.const import DivisionLevel
from wcd_geo_db.modules.code_seeker.query import CodeSeekerQuerySet
from pxd_tree.hierarchy import TreeQuerySet

from ..dtos import DivisionDTO, GeometryDTO
from .base import QuerySet
from .geometry import WithGeometryQuerySet
from .search import SearchQuerySet


__all__ = 'DivisionsQuerySet',

QT = TypeVar('QT', bound='DivisionsQuerySet')
VALUES_NAMES = (
    'id', 'name', 'level', 'types', 'codes', 'parent_id', 'path',
    'geometry__location', 'geometry__polygon',
)


def as_dto(values: dict) -> DivisionDTO:
    return DivisionDTO(
        id=values['id'],
        name=values['name'],
        level=DivisionLevel(values['level']),
        types=values['types'],
        codes=values['codes'],
        parent_id=values['parent_id'],
        path=list(values['path']),
        geometry=GeometryDTO(
            location=values['geometry__location'],
            polygon=values['geometry__polygon'],
        )
    )


class DivisionsQuerySet(
    WithGeometryQuerySet,
    CodeSeekerQuerySet,
    TreeQuerySet,
    SearchQuerySet,
    QuerySet
):
    def as_dtos(self) -> List[DivisionDTO]:
        return [as_dto(values) for values in self.values(*VALUES_NAMES)]

    def general_filter(
        self: QT,
        parent_ids: Optional[Sequence[int]] = None,
        levels: Optional[Sequence[DivisionLevel]] = None,
        types: Optional[Sequence[str]] = None,
        **kw
    ) -> QT:
        q = (
            super().general_filter(**kw)
            .optional_in('parent_id', parent_ids)
            .optional_in('level', levels)
            .optional_overlap('types', types)
        )

        return q
