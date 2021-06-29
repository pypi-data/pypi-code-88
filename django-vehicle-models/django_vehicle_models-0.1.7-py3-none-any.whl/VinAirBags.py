from django.db import models


class VinAirBags(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255, verbose_name='VIN (Status)')
    curtain_loc = models.CharField(max_length=255, blank=True, verbose_name='Curtain Air Bag Locations', default='')
    seat_cushion_loc = models.CharField(max_length=255, blank=True, verbose_name='Seat Cushion Air Bag Locations', default='')
    front_loc = models.CharField(max_length=255, blank=True, verbose_name='Front Air Bag Locations', default='')
    knee_loc = models.CharField(max_length=255, blank=True, verbose_name='Knee Air Bag Locations', default='')
    side_loc = models.CharField(max_length=255, blank=True, verbose_name='Side Air Bag Locations', default='')


    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'

