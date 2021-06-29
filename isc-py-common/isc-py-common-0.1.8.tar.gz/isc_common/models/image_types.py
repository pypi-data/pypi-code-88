import logging

from django.db.models import SmallIntegerField

from isc_common.models.base_ref import BaseRefHierarcy, BaseRefManager, BaseRefQuerySet

logger = logging.getLogger(__name__)


class Image_typesQuerySet(BaseRefQuerySet):
    def delete(self):
        return super().delete()

    def create(self, **kwargs):
        return super().create(**kwargs)

    def filter(self, *args, **kwargs):
        return super().filter(*args, **kwargs)


class Image_typesManager(BaseRefManager):

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
        return Image_typesQuerySet(self.model, using=self._db)


class Image_types(BaseRefHierarcy):
    height = SmallIntegerField(null=True, blank=True)
    width = SmallIntegerField(null=True, blank=True)

    objects = Image_typesManager()

    def __str__(self):
        return f'ID:{self.id}'

    def __repr__(self):
        return self.__str__()

    class Meta:
        verbose_name = 'Image types'
