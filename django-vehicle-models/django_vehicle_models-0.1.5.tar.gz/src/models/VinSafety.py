from django.db import models


class VinSafety(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255, verbose_name='VIN (Status)')
    abs = models.CharField(max_length=255, blank=True, verbose_name='Anti-lock Braking System (ABS)', default='')
    esc = models.CharField(max_length=255, blank=True, verbose_name='Electronic Stability Control (ESC)', default='')
    traction_control = models.CharField(max_length=255, blank=True, verbose_name='Traction Control', default='')
    assn = models.CharField(max_length=255, blank=True, verbose_name='Active Safety System Note', default='')
    apas = models.CharField(max_length=255, blank=True, verbose_name='Automatic Pedestrian Alerting Sound (for Hybrid and EV only)', default='')
    edr = models.CharField(max_length=255, blank=True, verbose_name='Event Data Recorder (EDR)', default='')
    cib = models.CharField(max_length=255, blank=True, verbose_name='Crash Imminent Braking (CIB)', default='')
    bsw = models.CharField(max_length=255, blank=True, verbose_name='Blind Spot Warning (BSW)', default='')
    fcw = models.CharField(max_length=255, blank=True, verbose_name='Forward Collision Warning (FCW)', default='')
    ldw = models.CharField(max_length=255, blank=True, verbose_name='Lane Departure Warning (LDW)', default='')
    dbs = models.CharField(max_length=255, blank=True, verbose_name='Dynamic Brake Support (DBS)', default='')
    paeb = models.CharField(max_length=255, blank=True, verbose_name='Pedestrian Automatic Emergency Braking (PAEB)', default='')
    acn = models.CharField(max_length=255, blank=True, verbose_name='Automatic Crash Notification (ACN) / Advanced Automatic Crash Notification (AACN)', default='')
    drl = models.CharField(max_length=255, blank=True, verbose_name='Daytime Running Light (DRL)', default='')
    headlamp_source = models.CharField(max_length=255, blank=True, verbose_name='Headlamp Light Source', default='')
    sahlbs = models.CharField(max_length=255, blank=True, verbose_name='Semiautomatic Headlamp Beam Switching', default='')
    adb = models.CharField(max_length=255, blank=True, verbose_name='Adaptive Driving Beam (ADB)', default='')
    rcta = models.CharField(max_length=255, blank=True, verbose_name='Rear Cross Traffic Alert', default='')
    raeb = models.CharField(max_length=255, blank=True, verbose_name='Rear Automatic Emergency Braking', default='')
    bsi = models.CharField(max_length=255, blank=True, verbose_name='Blind Spot Intervention (BSI)', default='')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'