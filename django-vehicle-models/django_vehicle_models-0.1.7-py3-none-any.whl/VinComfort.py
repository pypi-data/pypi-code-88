from django.db import models


class VinComfort(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255, verbose_name='VIN (Status)')
    auto_windows = models.CharField(max_length=255, blank=True, verbose_name='Auto-Reverse System for Windows and Sunroofs', default='')
    tpms_type = models.CharField(max_length=255, blank=True, verbose_name='Tire Pressure Monitoring System (TPMS) Type', default='')
    keyless = models.CharField(max_length=255, blank=True, verbose_name='Keyless Ignition', default='')
    sae_from = models.CharField(max_length=255, blank=True, verbose_name='SAE Automation Level From', default='')
    sae_to = models.CharField(max_length=255, blank=True, verbose_name='SAE Automation Level To', default='')
    acc = models.CharField(max_length=255, blank=True, verbose_name='Adaptive Cruise Control (ACC)', default='')
    backup_camera = models.CharField(max_length=255, blank=True, verbose_name='Backup Camera', default='')
    parking_assist = models.CharField(max_length=255, blank=True, verbose_name='Parking Assist', default='')
    lane_centering = models.CharField(max_length=255, blank=True, verbose_name='Lane Centering Assistance', default='')
    lane_keeping = models.CharField(max_length=255, blank=True, verbose_name='Lane Keeping Assistance (LKA)', default='')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'
