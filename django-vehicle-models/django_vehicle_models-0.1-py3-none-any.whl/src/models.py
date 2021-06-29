from django.db import models


# Create your models here.
class Avto(models.Model):
    #id = models.IntegerField(blank=True , verbose_name='Stock #', primary_key=True)
    title = models.CharField(max_length=255 , blank=True , verbose_name='Title')
    make = models.CharField(max_length=255 , blank=True , verbose_name='Automaker')
    vehicle_class = models.CharField(max_length=255 , blank=True , verbose_name='vehicle Class')
    model = models.CharField(max_length=255 , blank=True , verbose_name='Model')
    series = models.CharField(max_length=255 , blank=True , verbose_name='Series')
    year_car = models.CharField(max_length=255 , blank=True , verbose_name='Year of car')
    selling_branch = models.CharField(max_length=255 , blank=True , verbose_name='Selling Branch')
    vin_status = models.CharField(max_length=255 , blank=True , verbose_name='VIN (Status)')
    loss = models.CharField(max_length=255 , blank=True , verbose_name='Loss')
    primary_damage = models.CharField(max_length=255 , blank=True , verbose_name='Primary Damage')
    secondary_damage = models.CharField(max_length=255 , blank=True , verbose_name='Secondary Damage')
    title_sale_doc = models.CharField(max_length=255 , blank=True , verbose_name='Title/Sale Doc')
    start_code = models.CharField(max_length=255 , blank=True , verbose_name='Start Code')
    key_fob = models.CharField(max_length=255 , blank=True , verbose_name='Key/Fob')
    odometer = models.CharField(max_length=255 , blank=True , verbose_name='Odometer', default='')
    airbags = models.CharField(max_length=255 , blank=True , verbose_name='Airbags')
    vehicle = models.CharField(max_length=255 , blank=True , verbose_name='Vehicle')
    body_style = models.CharField(max_length=255 , blank=True , verbose_name='Body Style')
    engine = models.CharField(max_length=255 , blank=True , verbose_name='Engine')
    transmission = models.CharField(max_length=255 , blank=True , verbose_name='Transmission')
    drive_line_type = models.CharField(max_length=255 , blank=True , verbose_name='Drive Line Type')
    fuel_type = models.CharField(max_length=255 , blank=True , verbose_name='Fuel Type')
    cylinders = models.CharField(max_length=255 , blank=True , verbose_name='Cylinders')
    restraint_system = models.CharField(max_length=255 , blank=True , verbose_name='Restraint System')
    exterior_interior = models.CharField(max_length=255 , blank=True , verbose_name='Exterior/Interior')
    manufactured_in = models.CharField(max_length=255 , blank=True , verbose_name='Manufactured In')
    vehicle_class = models.CharField(max_length=255 , blank=True , verbose_name='Vehicle Class')
    description = models.CharField(max_length=255 , blank=True , verbose_name='Description')
    data1 = models.CharField(max_length=255 , blank=True , verbose_name='Description')
    data2 = models.CharField(max_length=255 , blank=True , verbose_name='Description')
    img1 = models.CharField(max_length=255 , blank=True , verbose_name='img1')
    img2 = models.CharField(max_length=255 , blank=True , verbose_name='img2')
    img3 = models.CharField(max_length=255 , blank=True , verbose_name='img3')
    img4 = models.CharField(max_length=255 , blank=True , verbose_name='img4')
    img5 = models.CharField(max_length=255 , blank=True , verbose_name='img5')
    img6 = models.CharField(max_length=255 , blank=True , verbose_name='img6')
    img7 = models.CharField(max_length=255 , blank=True , verbose_name='img7')
    img8 = models.CharField(max_length=255 , blank=True , verbose_name='img8')
    img9 = models.CharField(max_length=255 , blank=True , verbose_name='img9')
    img10 = models.CharField(max_length=255 , blank=True , verbose_name='img10')
    url = models.CharField(max_length=255 , blank=True , verbose_name='img1')
    factory_options1 = models.TextField(blank=True , verbose_name='Factory Options1')
    factory_options2 = models.TextField(blank=True , verbose_name='Factory Options2', default='')
    equipment_details1 = models.TextField(blank=True , verbose_name='Equipment Details1')
    equipment_details2 = models.TextField(blank=True , verbose_name='Equipment Details2', default='')
    vehicle_equipment1 = models.TextField(blank=True , verbose_name='Vehicle Equipment1')
    vehicle_equipment2 = models.TextField(blank=True , verbose_name='Vehicle Equipment2', default='')
    technical_specifications1 = models.TextField(blank=True , verbose_name='Technical Specifications1')
    technical_specifications2 = models.TextField(blank=True , verbose_name='Technical Specifications2', default='')
    buy_now_price = models.CharField(max_length=255 , blank=True , verbose_name='Buy now price', default='')
    current_bid = models.CharField(max_length=255 , blank=True , verbose_name='Current Bid', default='')
    actual_cash_value = models.CharField(max_length=255 , blank=True , verbose_name='Actual cash value', default='')
    estimated_repair_cost = models.CharField(max_length=255 , blank=True , verbose_name='Estimated repair cost', default='')
    YESNOT = (
        ('yes', 'yes'),
        ('not', 'not'),
        ('new', 'new'),
        )
    publish = models.CharField(blank=True, max_length=15, choices=YESNOT, verbose_name='Publish')
    coefficient = models.CharField(max_length=255, blank=True , verbose_name='Coefficient1', help_text='Coefficient number with a dot')
    new_cash_value = models.CharField(max_length=255, blank=True , verbose_name='New buy it now price', help_text='Buy now price * Coefficient1')
    coefficient2 = models.CharField(max_length=255, blank=True , verbose_name='Coefficient2', help_text='Coefficient number with a dot')
    our_price = models.CharField(max_length=255, blank=True, verbose_name='Our price', help_text='Our price')
    new_our_price = models.CharField(max_length=255, blank=True, verbose_name='New our price', help_text='Our price * Coefficient2')
    BUY = (
        (None, 'No_info'),
        ('BB', 'New buy it now price'),
        ('AA', 'New our price'),
        )
    choose_price = models.CharField(max_length=150 , blank=True , verbose_name='Сhoose a price', help_text="Price in xml", choices=BUY, default='')
    end_price = models.CharField(max_length=255 , blank=True , verbose_name='End price', help_text='End price')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering=['id']


class Information(models.Model):
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


class Vin(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Id of added car')
    vin_status = models.CharField(max_length=255 , blank=True , verbose_name='VIN (Status)')

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    class Meta:
        verbose_name = "Site iaai.com"
        ordering = ['id']


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