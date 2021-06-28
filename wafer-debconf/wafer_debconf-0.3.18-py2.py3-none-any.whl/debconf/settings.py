from wafer.settings import *

TEMPLATES[0]['OPTIONS']['context_processors'] += (
    'debconf.context_processors.expose_time_zone',
    'debconf.context_processors.expose_debconf_online',
)

BAKERY_VIEWS += (
    'debconf.views.RobotsView',
    'debconf.views.IndexView',
    'debconf.views.DebConfScheduleView',
    'debconf.views.StatisticsView',
    'debconf.views.ContentStatisticsView',
    'register.views.statistics.StatisticsView',
    'volunteers.views.VolunteerStatisticsView',
)

DEBCONF_ONLINE = False
