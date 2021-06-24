from django.contrib import admin
from django.apps import apps
from django.db.utils import ImproperlyConfigured, OperationalError, ProgrammingError

from .models import Model

def get_count(db_table):
    model = get_model(db_table)
    if model:
        return model.objects.all().count()


def get_model(db_table):
    for model in apps.get_models():
        if model._meta.db_table==db_table:
            return model

def init_models():
    models = {m._meta.db_table: m for m in Model.objects.all()}
    db_tables = []
    for m in apps.get_models():
        defaults = {
            'app':m._meta.app_label,
            'name':m.__name__,
            'is_admin':m in admin.site._registry,
            'is_middleware':m in admin.site._registry
        }
        kwargs = {k:v for k,v in defaults.items() if k!='is_middleware'}
        db_table = m._meta.db_table
        db_tables.append(db_table)
        count = get_count(m)
        if db_table not in models:
            defaults['count'] = count
            model, created = Model.objects.get_or_create(defaults,db_table=db_table)
            models[db_table] = model
    for db_table in filter(lambda db_table:db_table not in models,db_tables):
        Model.objects.filter(db_table=db_table).delete()

def update_count(model,count):
    if model.count!=count:
        Model.objects.filter(pk=model.pk).update(count=count)
