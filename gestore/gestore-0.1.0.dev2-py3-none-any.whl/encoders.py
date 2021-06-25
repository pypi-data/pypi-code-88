from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile

from django_countries.fields import Country


class GestoreEncoder(DjangoJSONEncoder):
    """
    A custom encoder that allows us to serialize unserializable objects
    like `ImageFieldFile` and `Country` objects.
    """
    def default(self, o, *args, **kwargs):
        if isinstance(o, ImageFieldFile):
            return str(o)
        if isinstance(o, Country):
            return o.code

        return super(GestoreEncoder, self).default(o)
