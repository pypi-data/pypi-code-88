import logging

import pkg_resources
from django.apps import AppConfig

import gdaps
from gdaps.api import PluginConfig
from gdaps.apps import GdapsConfig
from gdaps.frontend.api import current_engine

logger = logging.getLogger(__name__)


class FrontendPluginMeta:
    version = gdaps.__version__
    visible = False
    author = GdapsConfig.PluginMeta.author
    email = GdapsConfig.PluginMeta.author_email
    category = GdapsConfig.PluginMeta.category


class FrontendConfig(PluginConfig):
    name = "gdaps.frontend"
    label = "gdaps_frontend"
    verbose_name = "GDAPS frontend"

    PluginMeta = FrontendPluginMeta

    def ready(self):
        entry_points = []
        for entry_point in pkg_resources.iter_entry_points(
            group="gdaps.frontend.engines", name=None
        ):  # type: pkg_resources.EntryPoint
            entry_point.load()
            entry_points.append(entry_point.name)

            # if there is an engine selected in settings, check if everything it needs is available
            if current_engine():
                current_engine().check_runtime_prereq()

        if entry_points:
            logger.info(f" ✓ Loaded gdaps frontend engines... {entry_points}")
        else:
            logger.info(f"   No gdaps frontend engines available.")
