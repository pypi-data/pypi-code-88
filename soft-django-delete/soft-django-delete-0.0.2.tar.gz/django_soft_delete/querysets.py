from collections import Counter

from django.db.models.query import QuerySet


class SoftDeletionQuerySet(QuerySet):
    def delete(self):
        counter = Counter()
        assert self.query.can_filter(), "Cannot use 'limit' or " \
                                        "'offset' with delete."
        for o in self:
            _, dictionary = o.delete()
            counter += Counter(dictionary)
        self._result_cache = None
        return sum(counter.values()), dict(counter)

    delete.alters_data = True

    def undelete(self):
        counter = Counter()
        assert self.query.can_filter(), "Cannot use 'limit' or " \
                                        "'offset' with delete."
        for o in self:
            _, dictionary = o.undelete()
            counter += Counter(dictionary)
        self._result_cache = None
        return sum(counter.values()), dict(counter)

    undelete.alters_data = True

    def hard_delete(self):
        return super(SoftDeletionQuerySet, self).delete()

    def alive(self):
        return self.filter(deleted_at__isnull=True)

    def dead(self):
        return self.filter(deleted_at__isnull=False)

    def update_or_create(self, defaults=None, **kwargs):
        """
        Regular update_or_create() fails on soft-deleted, existing record
        with unique constraint on non-id field
        If object is soft-deleted we don't update-or-create it but reset the
        deleted field to None.
        """
        if not defaults:
            defaults = {}

        if 'deleted_at' in defaults:
            # Check if object is already soft-deleted
            deleted_object = self.filter(**kwargs).exclude(
                deleted_at=None).first()

            if deleted_object and not defaults['deleted_at']:
                deleted_object.undelete()

            if not deleted_object and defaults['deleted_at']:
                defaults.pop('deleted_at')
                obj, created = super(SoftDeletionQuerySet,
                                     self).update_or_create(defaults, **kwargs)
                obj.delete()
                return obj, created

        obj, created = super(SoftDeletionQuerySet, self).update_or_create(
            defaults, **kwargs)

        return obj, created
