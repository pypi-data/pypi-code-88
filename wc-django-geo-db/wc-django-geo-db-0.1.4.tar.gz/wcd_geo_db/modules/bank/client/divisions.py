from typing import Any, List, Optional, Sequence, Tuple, Type
from wcd_geo_db.modules.client import CodeSeekingClientMixin, DBClientMixin, NestedClient
from wcd_geo_db.const import DivisionLevel
from wcd_geo_db.modules.code_seeker.query import CodeSeekSeq

from ..query.geometry import Area
from ..dtos import DivisionDTO, DivisionTranslationDTO
from ..db import Division
from ..query import DivisionsQuerySet


__all__ = 'DivisionsClient',

CodeSeekDefinition = Tuple[str, Any]


class DivisionsClient(DBClientMixin, CodeSeekingClientMixin, NestedClient):
    model: Type[Division] = Division
    _qs: DivisionsQuerySet

    def get(self, ids: Sequence[int]) -> Sequence[DivisionDTO]:
        return self._qs.general_filter(ids=ids).as_dtos()

    def get_by_code(self, code: str, value: Any) -> Sequence[DivisionDTO]:
        return self.get(self.find(self._qs, codes=((code, value),)))

    def get_translations(
        self,
        ids: Sequence[int],
        language: str,
        fallback_languages: Sequence[str] = []
    ) -> Sequence[DivisionDTO]:
        entities = self.get(ids)

        return [
            DivisionTranslationDTO(
                id=e.id,
                language=language,
                entity_id=e.id,
                name=e.name
            )
            for e in entities
        ]

    def find(
        self,
        ids: Optional[Sequence[int]] = None,
        parent_ids: Optional[Sequence[int]] = None,
        levels: Optional[Sequence[DivisionLevel]] = None,
        codes: Optional[Sequence[Tuple[str, Any]]] = None,
        types: Optional[Sequence[str]] = None,
        location_areas: Optional[Sequence[Area]] = None,
        search_query: Optional[str] = None,
        **kw
    ) -> Sequence[int]:
        """Searches for an entities."""

        return (
            self._qs
            .general_filter(
                ids=ids,
                parent_ids=parent_ids,
                levels=levels,
                types=types,
                codes_filter=self._get_codes_filter(codes),
                location_areas=location_areas,
                search_query=search_query,
                **kw
            )
            .ids()
        )

    def find_descendants(
        self,
        ids: Sequence[int],
        levels: Optional[Sequence[DivisionLevel]] = None,
        codes: Optional[Sequence[Tuple[str, Any]]] = None,
        types: Optional[Sequence[str]] = None,
        location_areas: Optional[Sequence[Area]] = None,
        search_query: Optional[str] = None,
        **kw
    ) -> Sequence[int]:
        """Searches for a descendants of objects from `ids`."""

        return (
            self._qs
            .general_filter(ids=ids)
            .descendants(within=self._qs.general_filter(
                levels=levels,
                codes_filter=self._get_codes_filter(codes),
                types=types,
                location_areas=location_areas,
                search_query=search_query,
                **kw
            ))
            .ids()
        )

    def find_ancestors(
        self,
        ids: Sequence[int],
        levels: Optional[Sequence[DivisionLevel]] = None,
        codes: Optional[Sequence[Tuple[str, Any]]] = None,
        types: Optional[Sequence[str]] = None,
        location_areas: Optional[Sequence[Area]] = None,
        search_query: Optional[str] = None,
        **kw
    ) -> Sequence[int]:
        """Searches for an ancestors of objects from `ids`."""

        return (
            self._qs
            .general_filter(ids=ids)
            .ancestors(within=self._qs.general_filter(
                levels=levels,
                codes_filter=self._get_codes_filter(codes),
                types=types,
                location_areas=location_areas,
                search_query=search_query,
                **kw
            ))
            .ids()
        )
