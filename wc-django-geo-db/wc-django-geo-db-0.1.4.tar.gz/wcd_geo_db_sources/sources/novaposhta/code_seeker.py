from typing import Optional, TypedDict
from django.db import models
from wcd_geo_db.modules.code_seeker import CodeSeeker


__all__ = (
    'NovaPoshtaCodeValue',
    'NovaPoshtaCodeSeeker',

    'NOVAPOSHTA_SEEKER',
)


class NovaPoshtaCodeValue(TypedDict):
    type: str
    ref: str


class NovaPoshtaCodeSeeker(CodeSeeker):
    def Q(self, value: NovaPoshtaCodeValue, field_name: Optional[str] = None) -> models.Q:
        return models.Q(**{
            f'{field_name or self.field_name}__contains': {
                self.name: {
                    'type': value['type'],
                    'ref':  value['ref'],
                }
            }
            # f'{field_name or self.field_name}__{self.name}__type': value['type'],
            # f'{field_name or self.field_name}__{self.name}__ref': value['ref'],
        })


NOVAPOSHTA_SEEKER = NovaPoshtaCodeSeeker(name='NOVAPOSHTA')
