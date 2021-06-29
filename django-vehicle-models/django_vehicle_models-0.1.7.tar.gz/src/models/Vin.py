from django.db import models


class Vin(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255, blank=True, verbose_name='VIN (Status)')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'