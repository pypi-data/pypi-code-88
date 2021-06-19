import logging
import os
import json
from urllib.parse import quote

from django.db.models.fields.reverse_related import ManyToManyRel, ManyToOneRel, OneToOneRel

from django_project_backup.utils.couchdb.serializers import Serializer
from django_project_backup.utils.couchdb.stream import CouchdbStream

from ..settings import EXCLUDED_MODELS, \
                       DO_FAILSAFE_BACKUP, FAILSAFE_BACKUP_PATH_UPDATE, FAILSAFE_BACKUP_PATH_DELETE

logger = logging.getLogger('django_project_backup.utils.{}'.format(__name__))
_STREAM = None


def get_stream():
    global _STREAM
    if _STREAM is None:
        _STREAM = CouchdbStream()
    return _STREAM


def object_should_backup(instance):
    app_label = instance._meta.app_label
    _model_name = '%s.%s' % (instance._meta.app_label, instance._meta.object_name)
    model_name = _model_name.lower()

    logger.debug('Checking if model "{}" should backup'.format(model_name))

    return model_name not in EXCLUDED_MODELS and not app_label.startswith('migration')


def get_serialized(instance):
    serializer = Serializer()
    # using freshly obtained queryset should prevent faulty transactions to be backed up
    objects = instance.__class__.objects.filter(pk=instance.pk)
    serialized = json.loads(serializer.serialize(objects,
                                                 use_natural_foreign_keys=True))[0]

    return serialized


def get_related_objects(instance):
    related_objects = []
    instance_fields = instance._meta.get_fields(include_hidden=True)

    related_m2m_fields = [f.related_name or f.name + '_set'
                          for f in instance_fields
                          if type(f) == ManyToManyRel]  # !noqa
    related_many_to_one_fields = [f.related_name
                                  for f in instance_fields
                                  if type(f) == ManyToOneRel and f.related_name is not None and not f.related_name.endswith('+')]
    related_one_to_one_fields = [f.related_name
                                 for f in instance_fields
                                 if type(f) == OneToOneRel and f.related_name is not None]

    for f in related_m2m_fields:
        objs = getattr(instance, f).all()
        logger.debug('related_m2m {}:{}'.format(f, objs))
        related_objects += list(objs)
    for f in related_many_to_one_fields:
        objs = getattr(instance, f).all()
        logger.debug('related_many_to_one {}:{}'.format(f, objs))
        related_objects += list(objs)
    for f in related_one_to_one_fields:
        obj = getattr(instance, f, None)
        if obj is not None:
            logger.debug('related_one_to_one {}:{}'.format(f, obj))
            related_objects.append(obj)

    return related_objects


def do_failsafe_backup(serialized):
    file_name = quote(serialized['_id'], safe='')  # safe filename path
    with open(os.path.join(FAILSAFE_BACKUP_PATH_UPDATE,
                           '{}.json'.format(file_name)), 'w') as fd:
        json.dump(serialized, fd)


def do_backup(instance):
    serialized = get_serialized(instance)

    logger.debug('Backing up model "{}"'.format(serialized['_id']))

    try:
        stream = get_stream()
        stream.send(serialized)
    except:
        logger.exception('Error backing up serialized model')
        if DO_FAILSAFE_BACKUP:
            do_failsafe_backup(serialized)


def do_failsafe_delete(serialized):
    file_name = quote(serialized['_id'], safe='')  # safe filename path
    with open(os.path.join(FAILSAFE_BACKUP_PATH_DELETE,
                           '{}.json'.format(file_name)), 'w') as fd:
        json.dump(fd, serialized)


def do_delete(instance):
    serialized = getattr(instance, '__dpb__object', None)

    if serialized is not None:
        logger.info('Deleting backed up model "{}"'.format(serialized['_id']))
        try:
            stream = get_stream()
            stream.db.delete_document(serialized['_id'])
        except KeyError:
            logger.warning('Document "{}" has not been backed up'.format(serialized['_id']))
            pass
        except:
            logger.exception('Error deleting model')
            if DO_FAILSAFE_BACKUP:
                do_failsafe_delete(serialized)
        else:
            related_objects = getattr(instance, '__dpb__related_objects', None)
            if related_objects is not None:
                for obj in related_objects:
                    if object_should_backup(obj):
                        logger.debug('Backing up related model: {}'.format(obj))
                        obj.refresh_from_db()
                        obj.save()
