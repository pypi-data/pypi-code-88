from django.db import models, router

from .collector import DeleteCollector, UndeleteCollector
from .managers import SoftDeletionManager


class SoftDeletionModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        abstract = True
        default_manager_name = 'objects'

    def delete(self, using=None, keep_parents=False):
        using = using or router.db_for_write(self.__class__, instance=self)
        assert self.pk is not None, (
                "%s object can't be deleted because its %s attribute is "
                "set to None." %
                (self._meta.object_name, self._meta.pk.attname)
        )

        collector = DeleteCollector(using=using)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()

    delete.alters_data = True

    def hard_delete(self):
        super().delete()

    def undelete(self, using=None, keep_parents=False):
        using = using or router.db_for_write(self.__class__, instance=self)

        collector = UndeleteCollector(using=using)
        collector.collect([self], keep_parents=keep_parents)
        return collector.undelete()

    undelete.alters_data = True

    @classmethod
    def has_unique_fields(cls):
        """Checks if one of the fields of this model has a unique constraint
        set (unique=True)
        """
        for field in cls._meta.fields:
            if field.unique:
                return True
        return False
