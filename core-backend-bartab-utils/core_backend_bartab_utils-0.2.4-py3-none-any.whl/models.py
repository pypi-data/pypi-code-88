from django.db import models
from shortuuidfield import ShortUUIDField
from django.db.models import CharField
from django.utils.translation import gettext_lazy as _
from bartab_core.utils.validate import is_valid_short_uuid, is_valid_uuid
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class AbstractBaseModel(models.Model):
    """
    Base abstract model, that has `uuid` instead of `id` and includes `created_at`, `updated_at` fields.
    """
    uuid = ShortUUIDField(
        primary_key=True, editable=False, unique=True, max_length=22)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.uuid}>'


class UserField(CharField):
    description = 'User field'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 36

        kwargs['blank'] = False
        kwargs['null'] = False

        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add: bool):
        value = super().pre_save(model_instance, add)

        if not is_valid_uuid(value):
            raise IntegrityError("Invalid short uuid")

        return value

class MicroserviceForginKey(CharField):
    description = _("Key used by different BarTab microservice")


    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 22

        kwargs['blank'] = False
        kwargs['null'] = False

        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add: bool):
        value = super().pre_save(model_instance, add)

        if not is_valid_short_uuid(value):
            raise IntegrityError("Invalid short uuid")
        
        return value
