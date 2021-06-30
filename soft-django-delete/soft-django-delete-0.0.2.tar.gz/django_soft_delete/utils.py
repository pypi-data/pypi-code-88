def check_local_deleted_at(model):
    return any([f.name == "deleted_at" for f in model._meta.local_fields])


def is_soft_delete_model(model):
    return any([f.name == "deleted_at" for f in model._meta.fields])
