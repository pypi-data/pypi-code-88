from typing import Any, Dict, Sequence, Tuple
from django.db import models
from wcd_geo_db.modules.code_seeker import CodeSeekerRegistry


__all__ = 'CodeMapper',


class CodeMapper:
    items: Sequence[models.Model]
    registry: CodeSeekerRegistry
    mapping: Dict[str, Sequence[Tuple[Any, models.Model]]]

    def __init__(self, registry: CodeSeekerRegistry, items):
        self.items = items
        self.registry = registry
        self.mapping = {}

        self.prepare_mapping()

    def prepare_mapping(self):
        mapping = self.mapping

        for item in self.items:
            for code, value in item.codes.items():
                mapping[code] = mapping.get(code) or []
                mapping[code].append((value, item))

    def get_by_codes(self, codes: Sequence):
        r = self.registry

        return (
            item
            for code, value in codes
            for stored_value, item in (self.mapping.get(code) or [])
            if (
                # code in self.registry and
                self.registry[code].eq(value, stored_value)
            )
        )

    def get_one(self, codes: Sequence) -> models.Model:
        return next(self.get_by_codes(codes), None)
