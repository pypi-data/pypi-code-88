from django.apps import apps

def get_model(db_table):
    for model in apps.get_models():
        if model._meta.db_table==db_table:
            return model
