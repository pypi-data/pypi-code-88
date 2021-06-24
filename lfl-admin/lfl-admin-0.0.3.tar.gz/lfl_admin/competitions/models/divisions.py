import logging

from bitfield import BitField
from django.db.models import SmallIntegerField, CharField, TextField

from isc_common.auth.models.user import User
from isc_common.common import unknown
from isc_common.fields.code_field import CodeStrictField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcyManager, BaseRefHierarcyQuerySet, BaseRef
from lfl_admin.competitions.models.disqualification_condition import Disqualification_condition
from lfl_admin.competitions.models.disqualification_zones import Disqualification_zones
from lfl_admin.region.models.regions import Regions

logger = logging.getLogger(__name__)


class DivisionsQuerySet(BaseRefHierarcyQuerySet):
    pass


class DivisionsManager(BaseRefHierarcyManager):
    @classmethod
    def props(cls):
        return BitField(flags=(
            ('active', 'active'),  # 1
            ('completed', 'completed'),  # 1
            ('show_news', 'show_news'),  # 1
        ), default=1, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return DivisionsQuerySet(self.model, using=self._db)


class Divisions(BaseRef, Model_withOldId):
    code = CodeStrictField()
    disqualification_condition = ForeignKeyProtect(Disqualification_condition)
    editor = ForeignKeyProtect(User, related_name='Divisions_creator', null=True, blank=True)
    number_of_rounds = SmallIntegerField()
    props = DivisionsManager.props()
    region = ForeignKeyProtect(Regions)
    scheme = CharField(null=True, blank=True, max_length=255)
    top_text = TextField(null=True, blank=True)
    zone = ForeignKeyProtect(Disqualification_zones)

    objects = DivisionsManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            code=unknown,
            disqualification_condition=0,
            number_of_rounds=0,
            region=Regions.unknown(),
            zone=Disqualification_zones.unknown()
        )
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Супертурниры'
