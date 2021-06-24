import logging

from bitfield import BitField
from django.db.models import SmallIntegerField, CharField, DateField

from isc_common.auth.models.user import User
from isc_common.common import unknown
from isc_common.fields.code_field import CodeField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcyQuerySet, BaseRefHierarcyManager, BaseRef
from lfl_admin.competitions.models.disqualification_condition import Disqualification_condition
from lfl_admin.competitions.models.disqualification_zones import Disqualification_zones
from lfl_admin.competitions.models.divisions import Divisions
from lfl_admin.competitions.models.leagues import Leagues
from lfl_admin.competitions.models.protocol_types import Protocol_types
from lfl_admin.competitions.models.referee_category import Referee_category
from lfl_admin.competitions.models.seasons import Seasons
from lfl_admin.competitions.models.statistics_types import Statistics_types
from lfl_admin.competitions.models.tournament_types import Tournament_types
from lfl_admin.constructions.models.fields import Fields
from lfl_admin.region.models.regions import Regions

logger = logging.getLogger(__name__)


class TournamentsQuerySet(BaseRefHierarcyQuerySet):
    pass


class TournamentsManager(BaseRefHierarcyManager):

    @classmethod
    def props(cls):
        return BitField(flags=(
            ('active', 'active'),  # 1
            ('national', 'national'),  # 2
            ('show_league', 'show_league'),  # 4
            ('show_region', 'show_region'),  # 8
            ('up_selected', 'up_selected'),  # 16
            ('up2_selected', 'up2_selected'),  # 32
            ('down_selected', 'down_selected'),  # 64
            ('down2_selected', 'down2_selected'),  # 128
            ('calendar_created', 'calendar_created'),  # 256
            ('show_numbers', 'show_numbers'),  # 512
            ('show_player_number', 'show_player_number'),  # 1024
            ('show_stats', 'show_stats'),  # 2048
            ('show_empty_cells', 'show_empty_cells'),  # 4096
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
        return TournamentsQuerySet(self.model, using=self._db)


class Tournaments(BaseRef, Model_withOldId):
    code = CodeField()
    disqualification_condition = ForeignKeyProtect(Disqualification_condition)
    division = ForeignKeyProtect(Divisions)
    division_priority = SmallIntegerField()
    division_round = SmallIntegerField(null=True, blank=True)
    editor = ForeignKeyProtect(User, null=True, blank=True)
    field = ForeignKeyProtect(Fields)
    league = ForeignKeyProtect(Leagues)
    loss_points_rule = SmallIntegerField(null=True, blank=True)
    number_of_players = SmallIntegerField()
    number_of_rounds = SmallIntegerField()
    number_of_teams = SmallIntegerField()
    number_of_tours = SmallIntegerField()
    priority = SmallIntegerField()
    props = TournamentsManager.props()
    protocol_type = ForeignKeyProtect(Protocol_types)
    rating_rule = SmallIntegerField()
    referee_category = ForeignKeyProtect(Referee_category)
    referees_max = SmallIntegerField()
    region = ForeignKeyProtect(Regions)
    round = SmallIntegerField(null=True, blank=True)
    season = ForeignKeyProtect(Seasons)
    start_date = DateField(null=True, blank=True)
    technical_defeat = CharField(max_length=5, default='5:0')
    statistics_type = ForeignKeyProtect(Statistics_types)
    tournament_type = ForeignKeyProtect(Tournament_types)
    zone = ForeignKeyProtect(Disqualification_zones)

    objects = TournamentsManager()

    @classmethod
    def unknown(cls):
        res, _ = cls.objects.get_or_create(
            code=unknown,
            disqualification_condition=0,
            division=Divisions.unknown(),
            division_priority=0,
            field=Fields.unknown(),
            league=Leagues.unknown(),
            number_of_players=0,
            number_of_rounds=0,
            number_of_teams=0,
            number_of_tours=0,
            priority=0,
            protocol_type=Protocol_types.unknown(),
            rating_rule=0,
            referee_category=Referee_category.unknown(),
            referees_max=0,
            region=Regions.unknown(),
            season=Seasons.unknown(),
            statistics_type=Statistics_types.unknown(),
            tournament_type=Tournament_types.unknown(),
            zone=Disqualification_zones.unknown()
        )
        return res

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Турниры'
