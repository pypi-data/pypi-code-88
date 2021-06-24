import logging

from bitfield import BitField
from django.db.models import SmallIntegerField, DateTimeField, CharField

from isc_common.auth.models.user import User
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import Model_withOldId, AuditManager, AuditQuerySet
from isc_common.models.base_ref import Hierarcy
from lfl_admin.competitions.models.clubs import Clubs
from lfl_admin.competitions.models.divisions import Divisions
from lfl_admin.competitions.models.formation import Formation
from lfl_admin.competitions.models.leagues import Leagues
from lfl_admin.competitions.models.referees import Referees
from lfl_admin.competitions.models.seasons import Seasons
from lfl_admin.competitions.models.tournaments import Tournaments
from lfl_admin.constructions.models.stadiums import Stadiums

logger = logging.getLogger(__name__)


class CalendarQuerySet(AuditQuerySet):
    pass


class CalendarManager(AuditManager):

    @classmethod
    def props(cls):
        return BitField(flags=(
            ('protocol', 'protocol'),  # 1
            ('in_archive', 'in_archive'),  # 1
            ('show_stats', 'show_stats'),  # 1
            ('show_empty_cells', 'show_empty_cells'),  # 1
            ('penalty', 'penalty'),  # 1
        ), default=0, db_index=True)

    @staticmethod
    def getRecord(record):
        res = {
            'id': record.id,
            'code': record.code,
            'name': record.name,
            'description': record.description,
            'parent': record.parent.id if record.parent else None,
            'editing': record.editing,
            'deliting': record.deliting,
        }
        return res

    def get_queryset(self):
        return CalendarQuerySet(self.model, using=self._db)


class Calendar(Hierarcy, Model_withOldId):
    away = ForeignKeyProtect(Clubs, related_name='Calendar_away')
    away_formation = ForeignKeyProtect(Formation, related_name='Calendar_away_formation')
    away_points = SmallIntegerField()
    away_score = SmallIntegerField()
    checked = SmallIntegerField(default=0)
    editor = ForeignKeyProtect(User, null=True, blank=True)
    home = ForeignKeyProtect(Clubs, related_name='Calendar_home')
    division = ForeignKeyProtect(Divisions)
    home_formation = ForeignKeyProtect(Formation, related_name='Calendar_home_formation')
    home_points = SmallIntegerField()
    home_score = SmallIntegerField()
    league = ForeignKeyProtect(Leagues)
    match_cast = CharField(max_length=50, null=True, blank=True)
    match_date_time = DateTimeField(null=True, blank=True)
    match_number = SmallIntegerField()
    props = CalendarManager.props()
    referee = ForeignKeyProtect(Referees)
    season = ForeignKeyProtect(Seasons)
    stadium = ForeignKeyProtect(Stadiums)
    technical_defeat = SmallIntegerField()
    tour = SmallIntegerField()
    tournament = ForeignKeyProtect(Tournaments)

    objects = CalendarManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            away=Clubs.unknown(),
            away_formation=Formation.unknown(),
            away_points=0,
            away_score=0,
            checked = 0,
            home=Clubs.unknown(),
            division=Divisions.unknown(),
            home_formation=Formation.unknown(),
            home_points=0,
            home_score=0,
            league=Leagues.unknown(),
            match_number=0,
            referee=Referees.unknown(),
            season=Seasons.unknown(),
            stadium=Stadiums.unknown(),
            technical_defeat=0,
            tour=0,
            tournament=Tournaments.unknown()
        )
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Календарь матчей турнира'
