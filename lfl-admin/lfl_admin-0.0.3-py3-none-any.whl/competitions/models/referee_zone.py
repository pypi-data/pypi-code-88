import logging

from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import AuditModel, AuditManager, AuditQuerySet, Model_withOldId

from lfl_admin.competitions.models.leagues import Leagues
from lfl_admin.competitions.models.referees import Referees

logger = logging.getLogger(__name__)


class Referee_zoneQuerySet(AuditQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Referee_zoneManager(AuditManager):

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return Referee_zoneQuerySet(self.model, using=self._db)


class Referee_zone(AuditModel, Model_withOldId):
    league = ForeignKeyProtect(Leagues)
    referee = ForeignKeyProtect(Referees)

    objects = Referee_zoneManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Главные судьи в матчах'
        unique_together = (('referee', 'league'),)
