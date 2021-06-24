from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, Type
from functools import cached_property, reduce
from wcd_geo_db.modules.client import CodeSeekingClientMixin, DBClientMixin, NestedClient
from wcd_geo_db.const import DivisionLevel
from wcd_geo_db.modules.code_seeker.query import CodeSeekSeq

from ...bank.dtos import DivisionDTO
# from ..query.geometry import Area
from ..dtos import AddressDefinitionDTO, FormattedAddressDTO
# from ..db import Division
# from ..query import DivisionsQuerySet


__all__ = 'FormatterClient',


class FormatterClient(NestedClient):
    _bank_lookup: Callable

    def __init__(self, *_, bank_lookup: Callable = None, **kw):
        assert bank_lookup is not None, 'Bank lookuper is mandatory.'

        super().__init__(**kw)

        self._bank_lookup = bank_lookup

    @cached_property
    def bank(self):
        return self._bank_lookup(self)

    def _make_formatted_address(
        self,
        definition: AddressDefinitionDTO,
        divisions_map: Dict[int, DivisionDTO] = {}
    ) -> Optional[FormattedAddressDTO]:
        path = definition.get('divisions_path')

        if not path:
            return None

        divisions = [
            divisions_map[id]
            for id in path
            if id in divisions_map
        ]

        return FormattedAddressDTO(
            id=str(path[-1]),
            divisions=divisions,
            formatted_address=', '.join(d.name for d in reversed(divisions))
        )

    def _normalize_address_definitions(
        definitions: Sequence[AddressDefinitionDTO],
    ) -> Tuple[Sequence[AddressDefinitionDTO], dict]:
        return definitions

    def format_addresses(
        self,
        definitions: Sequence[AddressDefinitionDTO],
        language: str,
        fallback_languages: Sequence[str] = []
    ) -> Sequence[Optional[FormattedAddressDTO]]:
        """Formats addresses definitions.

        Result will be in the same order as passed in definitions.
        If address can't be formatted pastes None on it's place.
        """
        definitions: Sequence[AddressDefinitionDTO] = list(definitions)
        division_ids = set()
        divisions = []

        for definition in definitions:
            path = (definition.get('divisions_path') or ())

            for i, division in enumerate(path):
                if  division is None:
                    continue

                if isinstance(division, int):
                    division_ids.add(division)
                elif isinstance(division, DivisionDTO):
                    divisions.append(division)
                    # FIXME: Made an adequate normalization that wouldn't
                    # mutate initial structure.
                    path[i] = division.id
                else:
                    raise TypeError(
                        f'Wrong division in path: {type(division)}, {repr(division)}.'
                    )

        if len(division_ids) > 0:
            divisions += list(self.bank.divisions.get(ids=division_ids))

        divisions_map = {d.id: d for d in divisions}

        return [
            self._make_formatted_address(
                definition,
                divisions_map=divisions_map
            )
            for definition in definitions
        ]
