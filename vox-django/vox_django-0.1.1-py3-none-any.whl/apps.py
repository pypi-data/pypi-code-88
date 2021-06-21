from django.apps import AppConfig
from django.conf import settings
from health_check.plugins import plugin_dir

from vox_django.healthcheck.backends import DatabaseHealthCheck

HEALTH_CHECK_PLUGINS = settings.HEALTH_CHECK_PLUGINS

AVAILABLE_PLUGINS = {
    'database': DatabaseHealthCheck,
}


class VoxDjangoConfig(AppConfig):
    name = 'vox_django'

    def ready(self):
        [plugin_dir.register(AVAILABLE_PLUGINS[plugin]) for plugin in HEALTH_CHECK_PLUGINS]
