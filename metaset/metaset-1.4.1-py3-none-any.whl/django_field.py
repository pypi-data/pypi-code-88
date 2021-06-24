import json

try:
    from django.utils.translation import gettext_lazy

    try:
        # Django >= 3.1
        from django.db import JSONField
        from django.forms import JSONField as JSONFormField
    except ImportError:
        # For Django < 3.1
        from django.contrib.postgres.fields import JSONField
        from django.contrib.postgres.forms import JSONField as JSONFormField
# avoid import failures for non Django builds.
except ImportError:
    JSONField = object
    JSONFormField = object
    gettext_lazy = lambda a: a  # noqa: E731


from . import MetaSet


def _recur_serialize_metaset(value):
    """Transform a MetaSet to a JSON serializable value"""
    try:
        return {k: _recur_serialize_metaset(v) for k, v in value.items()}
    except AttributeError:
        return list(value)


class MetaFormField(JSONFormField):
    def prepare_value(self, value):
        if value is None:
            return None
        return super().prepare_value(_recur_serialize_metaset(value))


class MetaSetField(JSONField):
    """A categorized set field."""

    description = gettext_lazy("Dict of sets")

    def __init__(self, *args, **kwargs):
        kwargs["blank"] = True
        kwargs["default"] = MetaSet
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["default"]
        del kwargs["blank"]
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context=None):
        if value is None:
            return value
        if isinstance(value, str):
            # Django >= 3.1
            value = json.loads(value)
        return MetaSet.from_dict(value)

    def to_python(self, value):
        if isinstance(value, MetaSet):
            return value
        if value is None:
            return None
        return MetaSet.from_dict(value)

    def get_db_prep_save(self, value, connection, prepared=False):
        if value is not None:
            value = _recur_serialize_metaset(value)
        return super().get_db_prep_value(value, connection, prepared)

    def validate(self, value, model_instance):
        if value is not None:
            value = _recur_serialize_metaset(value)
        return super().validate(value, model_instance)

    def formfield(self, **kwargs):
        defaults = {"form_class": MetaFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)
