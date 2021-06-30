from django.db import connections
from django.db.models import deletion

from . import utils
from .collector import CollectorAction


def CASCADE(collector, field, sub_objs, using):
    collector.collect(sub_objs, source=field.remote_field.model,
                      source_attr=field.name, nullable=field.null)
    if field.null and not connections[
        using].features.can_defer_constraint_checks and not \
            utils.is_soft_delete_model(
                field.remote_field.model):
        collector.add_field_update(field, None, sub_objs)


def CASCADE_NO_REVIVE(collector, field, sub_objs, using):
    if collector.action_type == CollectorAction.DELETE:
        CASCADE(collector, field, sub_objs, using)


def PROTECT(collector, field, sub_objs, using):
    return deletion.PROTECT(collector, field, sub_objs, using)


def SET_DEFAULT(collector, field, sub_objs, using):
    return deletion.SET_DEFAULT(collector, field, sub_objs, using)


def SET_NULL(collector, field, sub_objs, using):
    return deletion.SET_NULL(collector, field, sub_objs, using)


def SET(value):
    return deletion.SET(value)


def DO_NOTHING(collector, field, sub_objs, using):
    return deletion.DO_NOTHING(collector, field, sub_objs, using)
