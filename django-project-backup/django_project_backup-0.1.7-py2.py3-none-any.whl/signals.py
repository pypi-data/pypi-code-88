import logging

from django.db.models.signals import post_save, pre_delete, post_delete, m2m_changed  # , pre_save

from .utils.commons import do_backup, get_serialized, object_should_backup, get_related_objects

logger = logging.getLogger('django_project_backup.{}'.format(__name__))


"""
def prepare_model(sender, instance, **kwargs):
    if not kwargs.get('raw', False) and not getattr(instance, '__dpb__updating', False) and instance.pk is not None:
        if _object_should_backup(instance):
            app_label = instance._meta.app_label

            logger.debug('prepare_model {} {} {} {}'.format(app_label, sender, instance, kwargs))

            # setattr(instance, '__dpb__related_objects', get_related_objects(instance))
            setattr(instance, '__dpb__object', get_serialized(instance))
"""


def update_model(sender, instance, created, **kwargs):
    if not kwargs.get('raw', False) and not getattr(instance, '__dpb__updating', False):
        if object_should_backup(instance):
            app_label = instance._meta.app_label

            if created:
                logger.debug('create_model {} {} {} {}'.format(app_label, sender, instance, kwargs))
            else:
                logger.debug('update_model {} {} {} {}'.format(app_label, sender, instance, kwargs))

            do_backup(instance)


def prepare_delete_model(sender, instance, **kwargs):
    if object_should_backup(instance):
        app_label = instance._meta.app_label

        logger.debug('prepare_delete_model {} {} {} {}'.format(app_label, sender, instance, kwargs))

        setattr(instance, '__dpb__related_objects', get_related_objects(instance))
        setattr(instance, '__dpb__object', get_serialized(instance))


def delete_model(sender, instance, **kwargs):
    if object_should_backup(instance):
        app_label = instance._meta.app_label

        logger.debug('delete_model {} {} {} {}'.format(app_label, sender, instance, kwargs))


def update_model_relations(sender, instance, action, **kwargs):
    if not kwargs.get('raw', False):
        if object_should_backup(instance):
            app_label = instance._meta.app_label

            logger.debug('update_model_relations {} {} {} {} {}'.format(app_label, action, sender, instance, kwargs))

            do_backup(instance)


# https://docs.djangoproject.com/en/3.2/topics/signals/#listening-to-signals

# pre_save.connect(prepare_model, weak=False)  # wip (when updating model natural key)
post_save.connect(update_model, weak=False)
pre_delete.connect(prepare_delete_model, weak=False)
post_delete.connect(delete_model, weak=False)
m2m_changed.connect(update_model_relations, weak=False)
