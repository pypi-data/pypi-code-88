from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex
from django.utils.translation import pgettext_lazy


__all__ = (
    'create_types_field', 'create_division_field', 'codes_indexes',
    'CodesDefinableMixin', 'GroupingMixin', 'NamedMixin',
)


def create_types_field(verbose_name):
    return ArrayField(
        base_field=models.CharField(max_length=512),
        verbose_name=verbose_name,
        null=False, blank=True, default=list
    )


def create_division_field(**kw):
    return models.ForeignKey(
        'Division',
        **{
            **dict(
                verbose_name = pgettext_lazy('wcd_geo_db:field', 'Division'),
                null=True, on_delete=models.SET_NULL, blank=False
            ),
            **kw
        }
    )



def codes_indexes():
    return [
        GinIndex(
            name='%(app_label)s_%(class)s_codes_idx',
            fields=['codes'],
            opclasses=('jsonb_ops',)
        ),
    ]


class CodesDefinableMixin(models.Model):
    class Meta:
        abstract = True
        indexes = codes_indexes()

    codes = models.JSONField(
        verbose_name=pgettext_lazy('wcd_geo_db', 'Codes'),
        null=False, blank=True, default=dict
    )


class GroupingMixin(models.Model):
    class Meta:
        abstract = True

    grouping = models.ForeignKey(
        'self',
        verbose_name=pgettext_lazy('wcd_geo_db', 'Grouping entity'),
        on_delete=models.SET_NULL, null=True, blank=True, default=None
    )


class NamedMixin(models.Model):
    class Meta:
        abstract = True

    name = models.TextField(
        verbose_name=pgettext_lazy('wcd_geo_db', 'Name')
    )

    def __str__(self):
        return self.name


class SynonymizedMixin(models.Model):
    class Meta:
        abstract = True

    synonyms = models.TextField(
        verbose_name=pgettext_lazy('wcd_geo_db', 'Synonyms'),
        null=False, blank=True, default=''
    )
