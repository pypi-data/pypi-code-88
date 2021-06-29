from django.db import models


class VinSpec(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255, verbose_name='VIN (Status)')
    make = models.CharField(max_length=255, blank=True, verbose_name='Manufacturer short', default='') #"Variable": "Make"
    model = models.CharField(max_length=255, blank=True, verbose_name='Model name', default='')#"Variable": "Model"
    series = models.CharField(max_length=255, blank=True, verbose_name='Series', default='')#"Variable": "Series"
    model_year = models.CharField(max_length=255, blank=True, verbose_name='Model Year', default='')#"Variable": "Model Year"
    vehicle_type = models.CharField(max_length=255, blank=True, verbose_name='Vehicle Type', default='')#"Variable": "Vehicle Type"
    body_class = models.CharField(max_length=255, blank=True, verbose_name='Body Class', default='')#"Variable": "Body Class"
    ncsa_body_type = models.CharField(max_length=255, blank=True, verbose_name='NCSA Body Type', default='')#"Variable": "NCSA Body Type"
    doors = models.IntegerField(blank=True, verbose_name='Doors', null=True)#"Variable": "Doors"
    seats_number = models.IntegerField(blank=True, verbose_name='Number of Seats', null=True)#"Variable": "Number of Seats"
    drive_type = models.CharField(max_length=255, blank=True, verbose_name='Drive Type', default='')#"Variable": "Drive Type"
    engine_model = models.CharField(max_length=255, blank=True, verbose_name='Engine Model', default='')#"Variable": "Engine Model"
    engine_config = models.CharField(max_length=255, blank=True, verbose_name='Engine Configuration', default='')#"Variable": "Engine Configuration"
    cylinder_count = models.IntegerField(blank=True, verbose_name='Engine Number of Cylinders', null=True) #"Variable": "Engine Number of Cylinders"
    engine_power_kw = models.FloatField(blank=True, verbose_name='Engine Power (KW)', null=True)#"Variable": "Engine Power (KW)"
    displacement_l = models.FloatField(blank=True, verbose_name='Engine displacement (L)', null=True)#"Variable": "Displacement (L)"
    top_speed_mph = models.FloatField(blank=True, verbose_name='Top Speed (MPH)', null=True)#"Variable": "Top Speed (MPH)"
    fuel_type = models.CharField(max_length=255, blank=True, verbose_name='Fuel Type - Primary', default='')#"Variable": "Fuel Type - Primary"
    plant_country = models.CharField(max_length=255, blank=True, verbose_name='Country of manufacture', default='')#"Variable": "Plant Country"
    base_price_usd = models.IntegerField(blank=True, verbose_name='Base Price ($)', null=True)#"Variable": "Base Price ($)"
    transmission_style = models.CharField(max_length=255, blank=True, verbose_name='Transmission Style', default='')
    transmission_speeds = models.CharField(max_length=255, blank=True, verbose_name='Transmission Speeds', default='')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'

