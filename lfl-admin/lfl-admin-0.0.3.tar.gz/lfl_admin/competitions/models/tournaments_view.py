import logging

from django.conf import settings
from django.db.models import SmallIntegerField, CharField, DateField, BooleanField

from isc_common import delAttr, setAttr
from isc_common.auth.models.user import User
from isc_common.fields.code_field import CodeField
from isc_common.fields.name_field import NameField
from isc_common.fields.related import ForeignKeyProtect
from isc_common.http.DSRequest import DSRequest
from isc_common.models.audit import Model_withOldId
from isc_common.models.base_ref import BaseRefHierarcyQuerySet, BaseRefHierarcyManager, BaseRef
from isc_common.number import DelProps
from lfl_admin.competitions.models.disqualification_condition import Disqualification_condition
from lfl_admin.competitions.models.disqualification_zones import Disqualification_zones
from lfl_admin.competitions.models.divisions import Divisions
from lfl_admin.competitions.models.leagues import Leagues
from lfl_admin.competitions.models.protocol_types import Protocol_types
from lfl_admin.competitions.models.referee_category import Referee_category
from lfl_admin.competitions.models.seasons import Seasons
from lfl_admin.competitions.models.statistics_types import Statistics_types
from lfl_admin.competitions.models.tournament_types import Tournament_types
from lfl_admin.competitions.models.tournaments import TournamentsManager
from lfl_admin.constructions.models.fields import Fields
from lfl_admin.region.models.regions import Regions

logger = logging.getLogger(__name__)


class Tournaments_viewQuerySet(BaseRefHierarcyQuerySet):
    def prepare_request(self, request):
        from lfl_admin.statistic.models.raiting_of_players_tournamet import Raiting_of_players_tournamet

        data = request.get_data()

        ids = data.get('ids')
        if ids is not None:
            tournament_id = list(set(map(lambda x: x.get('tournament'), Raiting_of_players_tournamet.objects.filter(raiting_id__in=ids).values('tournament'))))
            if len(tournament_id) == 0:
                tournament_id = [-1]

            delAttr(request.json.get('data'), 'ids')
            setAttr(request.json.get('data'), 'id', tournament_id)
        return request

    def get_info(self, request, *args):
        request = DSRequest(request=request)
        request = self.prepare_request(request)

        criteria = self.get_criteria(json=request.json)
        cnt = super().filter(*args, criteria).count()
        cnt_all = super().filter().count()
        return dict(qty_rows=cnt, all_rows=cnt_all)

    def get_range_rows1(self, request, function=None, distinct_field_names=None, remove_fields=None):
        request = DSRequest(request=request)
        request = self.prepare_request(request)

        self.alive_only = request.alive_only
        self.enabledAll = request.enabledAll
        res = self.get_range_rows(
            start=request.startRow,
            end=request.endRow,
            function=function,
            distinct_field_names=distinct_field_names,
            json=request.json,
            criteria=request.get_criteria(),
            user=request.user
        )
        return res


class Tournaments_viewManager(BaseRefHierarcyManager):

    @staticmethod
    def getRecord(record):
        res = {
            'active': record.active,
            'code': record.code,
            'condition__name': record.disqualification_condition.name,
            'condition_id': record.disqualification_condition.id,
            'deliting': record.deliting,
            'description': record.description,
            'division__name': record.division.name,
            'division_id': record.division.id,
            'division_priority': record.division_priority,
            'division_round': record.division_round,
            'editing': record.editing,
            'field__name': record.field.name,
            'field_id': record.field.id,
            'id': record.id,
            'league__name': record.league.name,
            'league_id': record.league.id,
            'logo_real_name': record.logo_real_name,
            'logo_src': f'http://{settings.IMAGE_CONTENT_HOST}:{settings.IMAGE_CONTENT_PORT}/{record.logo_image_src}&ws_host={settings.WS_HOST}&ws_port={settings.WS_PORT}&ws_channel={settings.WS_CHANNEL}',
            'loss_points_rule': record.loss_points_rule,
            'name': record.name,
            'number_of_players': record.number_of_players,
            'number_of_rounds': record.number_of_rounds,
            'number_of_teams': record.number_of_teams,
            'number_of_tours': record.number_of_tours,
            'priority': record.priority,
            'props': record.props,
            'protocol_type_id': record.protocol_type.id,
            'protocol_type_name': record.protocol_type.name,
            'rating_rule': record.rating_rule,
            'referee_category__name': record.referee_category.name,
            'referee_category_id': record.referee_category.id,
            'referees_max': record.referees_max,
            'region__name': record.region.name,
            'region_id': record.region.id,
            'round': record.round,
            'season__name': record.season.name,
            'season_id': record.season.id,
            'start_date': record.start_date,
            'statistics_type__name': record.statistics_type.name,
            'statistics_type_id': record.statistics_type.id,
            'technical_defeat': record.technical_defeat,
            'tournament_type__name': record.tournament_type.name,
            'tournament_type_id': record.tournament_type.id,
            'zone__name': record.zone.name,
            'zone_id': record.zone.id,
        }
        return DelProps(res)

    def get_queryset(self):
        return Tournaments_viewQuerySet(self.model, using=self._db)


class Tournaments_view(BaseRef, Model_withOldId):
    active = BooleanField()
    code = CodeField()
    disqualification_condition = ForeignKeyProtect(Disqualification_condition)
    division = ForeignKeyProtect(Divisions)
    division_priority = SmallIntegerField()
    division_round = SmallIntegerField(null=True, blank=True)
    editor = ForeignKeyProtect(User, null=True, blank=True)
    field = ForeignKeyProtect(Fields)
    league = ForeignKeyProtect(Leagues)
    logo_image_src = NameField()
    logo_real_name = NameField()
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
    statistics_type = ForeignKeyProtect(Statistics_types)
    technical_defeat = CharField(max_length=5, default='5:0')
    tournament_type = ForeignKeyProtect(Tournament_types)
    zone = ForeignKeyProtect(Disqualification_zones)

    objects = Tournaments_viewManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Турниры'
        db_table = 'competitions_tournaments_view'
        managed = False
