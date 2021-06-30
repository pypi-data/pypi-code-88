from collections import Counter
from enum import Enum
from operator import attrgetter

from django.contrib.admin.utils import NestedObjects
from django.db import transaction
from django.db.models import signals, sql
from django.db.models.deletion import Collector
from django.utils.timezone import now

from . import utils


class CollectorAction(Enum):
    DELETE = "delete"
    UNDELETE = "undelete"


class SoftDeleteCollector(Collector):

    def __init__(self, action_type, using):
        self.action_type = action_type
        super().__init__(using=using)

    def _delete_instances(self, model, instances, deleted_at):
        count = 0
        if not utils.is_soft_delete_model(model):
            query = sql.DeleteQuery(model)
            pk_list = [obj.pk for obj in instances]
            count = query.delete_batch(pk_list, self.using)
        if utils.check_local_deleted_at(model):
            self._soft_delete_instances(model, instances, deleted_at)
            count = len(instances)

        return count

    def _soft_delete_instances(self, model, instances, deleted_at):

        query = sql.UpdateQuery(model)
        pk_list = []
        for ins in instances:
            pk_list.append(ins.pk)
            ins.deleted_at = deleted_at

        query.update_batch(pk_list,
                           {'deleted_at': deleted_at}, self.using)

    def _delete_qs(self, qs, deleted_at):
        count = 0
        model = qs.model
        if not utils.is_soft_delete_model(model):
            count = qs._raw_delete(using=self.using)
        if utils.check_local_deleted_at(model):
            count = qs.count()
            qs.update(**{'deleted_at': deleted_at})
        return count

    def delete(self):
        # sort instance collections
        for model, instances in self.data.items():
            self.data[model] = sorted(instances, key=attrgetter("pk"))

        # if possible, bring the models in an order suitable for databases that
        # don't support transactions or cannot defer constraint checks until
        # the
        # end of a transaction.
        self.sort()
        # number of objects deleted for each model label
        deleted_counter = Counter()
        deleted_at = now()

        with transaction.atomic(using=self.using, savepoint=False):
            for model, obj in self.instances_with_model():
                if not model._meta.auto_created:
                    signals.pre_delete.send(
                        sender=model, instance=obj, using=self.using
                    )

            for qs in self.fast_deletes:
                count = self._delete_qs(qs, deleted_at)
                deleted_counter[qs.model._meta.label] += count

            # update fields
            for model, instances_for_fieldvalues in self.field_updates.items():
                for (field,
                     value), instances in instances_for_fieldvalues.items():
                    query = sql.UpdateQuery(model)
                    query.update_batch([obj.pk for obj in instances],
                                       {field.name: value}, self.using)

            # reverse instance collections
            for instances in self.data.values():
                instances.reverse()

            for model, instances in self.data.items():
                count = self._delete_instances(model, instances, deleted_at)
                deleted_counter[model._meta.label] += count

                if not model._meta.auto_created:
                    for obj in instances:
                        signals.post_delete.send(
                            sender=model, instance=obj, using=self.using
                        )

        for instances_for_fieldvalues in self.field_updates.values():
            for (field, value), instances in instances_for_fieldvalues.items():
                for obj in instances:
                    setattr(obj, field.attname, value)

        return sum(deleted_counter.values()), dict(deleted_counter)

    @staticmethod
    def _undelete(instance):
        if instance.deleted_at:
            instance.deleted_at = None
            instance.save()

    def undelete(self):
        # sort instance collections
        for model, instances in self.data.items():
            self.data[model] = sorted(instances, key=attrgetter("pk"))

        self.sort()

        revive_counter = Counter()
        with transaction.atomic(using=self.using):
            for qs in self.fast_deletes:
                for qs_instance in qs:
                    if utils.is_soft_delete_model(qs.model):
                        revive_counter.update([qs_instance._meta.model_name])
                        self._undelete(qs_instance)

            for model, instances in self.data.items():
                for instance in instances:
                    if utils.is_soft_delete_model(model):
                        revive_counter.update([instance._meta.model_name])
                        self._undelete(instance)

        return sum(revive_counter.values()), dict(revive_counter)


class DeleteCollector(SoftDeleteCollector):
    def __init__(self, using):
        super().__init__(CollectorAction.DELETE, using)

    def related_objects(self, related, objs):
        """
        Get a QuerySet of objects related to `objs` via the relation `related`.
        """
        return related.related_model._default_manager.using(self.using).filter(
            **{"%s__in" % related.field.name: objs}
        )


class NestedDeleteCollector(DeleteCollector, NestedObjects):
    pass


class UndeleteCollector(SoftDeleteCollector):

    def __init__(self, using):
        super().__init__(CollectorAction.UNDELETE, using)

    def related_objects(self, related, objs):
        """
        Get a QuerySet of objects related to `objs` via the relation `related`.
        """
        filter_dict = {"%s__in" % related.field.name: objs}
        if utils.is_soft_delete_model(related.related_model):
            filter_dict["deleted_at__in"] = [obj.deleted_at for obj in objs]

        return related.related_model._base_manager.using(self.using).filter(
            **filter_dict)
