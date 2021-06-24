from django.utils.translation import pgettext_lazy
from django.db import models

from wcd_geo_db_sources.modules.process import ProcessStage

__all__ = 'SOURCE', 'ImportStage'

SOURCE = 'KOATUU'


class ImportStage(models.TextChoices):
    INITIAL = ProcessStage.INITIAL
    UPLOADING = '002000-uploading', pgettext_lazy('wcd_geo_db_sources:koatuu', 'Uploading')
    PARSING = '003000-parsing', pgettext_lazy('wcd_geo_db_sources:koatuu', 'Parsing')
    MERGE = '004000-merge', pgettext_lazy('wcd_geo_db_sources:koatuu', 'Merge')
    CLEANUP = '005000-cleanup', pgettext_lazy('wcd_geo_db_sources:koatuu', 'Cleanup')
