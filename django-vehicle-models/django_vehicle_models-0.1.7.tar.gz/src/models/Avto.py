from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Avto(models.Model):
    # id = models.IntegerField(blank=True , verbose_name='Stock #', primary_key=True)
    title = models.CharField(max_length=255, blank=True, verbose_name='Title')
    make = models.CharField(max_length=255, blank=True, verbose_name='Automaker')
    vehicle_class = models.CharField(max_length=255, blank=True, verbose_name='vehicle Class')
    model = models.CharField(max_length=255, blank=True, verbose_name='Model')
    series = models.CharField(max_length=255, blank=True, verbose_name='Series')
    year_car = models.CharField(max_length=255, blank=True, verbose_name='Year of car')
    selling_branch = models.CharField(max_length=255, blank=True, verbose_name='Selling Branch')
    vin_status = models.CharField(max_length=255, blank=True, verbose_name='VIN (Status)')
    loss = models.CharField(max_length=255, blank=True, verbose_name='Loss')
    primary_damage = models.CharField(max_length=255, blank=True, verbose_name='Primary Damage')
    secondary_damage = models.CharField(max_length=255, blank=True, verbose_name='Secondary Damage')
    title_sale_doc = models.CharField(max_length=255, blank=True, verbose_name='Title/Sale Doc')
    start_code = models.CharField(max_length=255, blank=True, verbose_name='Start Code')
    key_fob = models.CharField(max_length=255, blank=True, verbose_name='Key/Fob')
    odometer = models.CharField(max_length=255, blank=True, verbose_name='Odometer', default='')
    airbags = models.CharField(max_length=255, blank=True, verbose_name='Airbags')
    vehicle = models.CharField(max_length=255, blank=True, verbose_name='Vehicle')
    body_style = models.CharField(max_length=255, blank=True, verbose_name='Body Style')
    engine = models.CharField(max_length=255, blank=True, verbose_name='Engine')
    transmission = models.CharField(max_length=255, blank=True, verbose_name='Transmission')
    drive_line_type = models.CharField(max_length=255, blank=True, verbose_name='Drive Line Type')
    fuel_type = models.CharField(max_length=255, blank=True, verbose_name='Fuel Type')
    cylinders = models.CharField(max_length=255, blank=True, verbose_name='Cylinders')
    restraint_system = models.CharField(max_length=255, blank=True, verbose_name='Restraint System')
    exterior_interior = models.CharField(max_length=255, blank=True, verbose_name='Exterior/Interior')
    manufactured_in = models.CharField(max_length=255, blank=True, verbose_name='Manufactured In')
    vehicle_class = models.CharField(max_length=255, blank=True, verbose_name='Vehicle Class')
    description = models.CharField(max_length=255, blank=True, verbose_name='Description')
    data1 = models.CharField(max_length=255, blank=True, verbose_name='Description')
    data2 = models.CharField(max_length=255, blank=True, verbose_name='Description')
    img1 = models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='img1')
    img2 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img2')
    img3 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img3')
    img4 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img4')
    img5 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img5')
    img6 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img6')
    img7 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img7')
    img8 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img8')
    img9 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img9')
    img10 = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name='img10')
    url = models.CharField(max_length=255, blank=True, verbose_name='img1')
    factory_options1 = models.TextField(blank=True, verbose_name='Factory Options1')
    factory_options2 = models.TextField(blank=True, verbose_name='Factory Options2', default='')
    equipment_details1 = models.TextField(blank=True, verbose_name='Equipment Details1')
    equipment_details2 = models.TextField(blank=True, verbose_name='Equipment Details2', default='')
    vehicle_equipment1 = models.TextField(blank=True, verbose_name='Vehicle Equipment1')
    vehicle_equipment2 = models.TextField(blank=True, verbose_name='Vehicle Equipment2', default='')
    technical_specifications1 = models.TextField(blank=True, verbose_name='Technical Specifications1')
    technical_specifications2 = models.TextField(blank=True, verbose_name='Technical Specifications2', default='')
    buy_now_price = models.CharField(max_length=255, blank=True, verbose_name='Buy now price', default='')
    current_bid = models.CharField(max_length=255, blank=True, verbose_name='Current Bid', default='')
    actual_cash_value = models.CharField(max_length=255, blank=True, verbose_name='Actual cash value', default='')
    estimated_repair_cost = models.CharField(max_length=255, blank=True, verbose_name='Estimated repair cost',
                                             default='')
    YESNOT = (
        ('yes', 'yes'),
        ('not', 'not'),
        ('new', 'new'),
    )
    publish = models.CharField(blank=True, max_length=15, choices=YESNOT, verbose_name='Publish')
    coefficient = models.CharField(max_length=255, blank=True, verbose_name='Coefficient1',
                                   help_text='Coefficient number with a dot')
    new_cash_value = models.CharField(max_length=255, blank=True, verbose_name='New buy it now price',
                                      help_text='Buy now price * Coefficient1')
    coefficient2 = models.CharField(max_length=255, blank=True, verbose_name='Coefficient2',
                                    help_text='Coefficient number with a dot')
    our_price = models.CharField(max_length=255, blank=True, verbose_name='Our price', help_text='Our price')
    new_our_price = models.CharField(max_length=255, blank=True, verbose_name='New our price',
                                     help_text='Our price * Coefficient2')
    BUY = (
        (None, 'No_info'),
        ('BB', 'New buy it now price'),
        ('AA', 'New our price'),
    )
    choose_price = models.CharField(max_length=150, blank=True, verbose_name='Сhoose a price', help_text="Price in xml",
                                    choices=BUY, default='')
    end_price = models.CharField(max_length=255, blank=True, verbose_name='End price', help_text='End price')
    locations = (
        ('et', 'estonia'),
        ('us', 'united states'),
    )
    location = models.CharField(blank=True, max_length=20, default='-', choices=locations,
                                verbose_name="current location")
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  default=User.objects.get(username="vehicle.lv").id)

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']
        app_label = 'avto'
