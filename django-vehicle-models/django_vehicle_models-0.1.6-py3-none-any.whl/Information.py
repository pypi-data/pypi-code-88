from django.db import models


class Information(models.ModelBase):
    name = models.CharField(max_length=255 , blank=True , verbose_name='Contact name')
    phone = models.CharField(max_length=255 , blank=True , verbose_name='Phone number')
    email = models.CharField(max_length=255 , blank=True , verbose_name='E-mail')
    company = models.CharField(max_length=255 , blank=True , verbose_name='Company name')
    code = models.CharField(max_length=255 , blank=True , verbose_name='Company code')
    country = models.CharField(max_length=255 , blank=True , verbose_name='Country')
    city = models.CharField(max_length=255 , blank=True , verbose_name='City')
    description = models.CharField(max_length=255 , blank=True , verbose_name='Description')
    test1 = models.CharField(max_length=255 , blank=True , verbose_name='Test')
    address = models.CharField(max_length=255 , blank=True , verbose_name='Address')
    postal_code = models.CharField(max_length=255 , blank=True , verbose_name='Postal code')
    ru_description = models.CharField(max_length=255 , blank=True , verbose_name='Ru Description')
    es_description = models.CharField(max_length=255 , blank=True , verbose_name='Es Description')
    pass_tipcars = models.CharField(max_length=255 , blank=True , verbose_name='TIPCARS password')
    kod_firmy = models.CharField(max_length=255 , blank=True , verbose_name='TIPCARS kod_firmy')

    class Meta:
        verbose_name = "Contact details xml"
        ordering = ['id']
        app_label = 'avto'


