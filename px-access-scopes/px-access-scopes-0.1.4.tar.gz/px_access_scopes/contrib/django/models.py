from django.db import models
from django.contrib.contenttypes.models import ContentType


__all__ = 'Scope',


class Scope(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def get_content_type(cls):
        return ContentType.objects.get_for_model(cls)
