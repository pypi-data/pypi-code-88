from django.db import models
from django.utils.translation import pgettext_lazy

from pxd_tree.hierarchy import Tree, tree_indexes
from wcd_geo_db.const import DivisionLevel

from ..query import DivisionsQuerySet
from .mixins import (
    CodesDefinableMixin, NamedMixin, SynonymizedMixin,
    create_types_field, codes_indexes
)
from .geometry import WithGeometryMixin


__all__ = 'Division',


class Division(Tree, NamedMixin, SynonymizedMixin, WithGeometryMixin, CodesDefinableMixin):
    Levels = DivisionLevel
    objects: models.Manager[DivisionsQuerySet] = DivisionsQuerySet.as_manager()

    class Meta:
        verbose_name = pgettext_lazy('wcd_geo_db', 'Division')
        verbose_name_plural = pgettext_lazy('wcd_geo_db', 'Divisions')
        indexes = tree_indexes() + codes_indexes()

    id = models.BigAutoField(
        primary_key=True, verbose_name=pgettext_lazy('wcd_geo_db', 'ID')
    )
    level = models.SmallIntegerField(
        verbose_name=pgettext_lazy('wcd_geo_db', 'Division level'),
        choices=Levels.choices, null=False, blank=False
    )
    types = create_types_field(pgettext_lazy('wcd_geo_db', 'Division types'))
