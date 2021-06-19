# Generated by Django 3.0.10 on 2020-09-08 12:57

import delivery.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New order'), ('in_progress', 'In progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='new', max_length=100, verbose_name='Status')),
                ('payment_method', models.CharField(choices=[('cash', 'Cash payment'), ('privat24', 'Privat 24'), ('cash_on_delivery', 'Cash on delivery'), ('cashless_payment', 'Cashless payment')], max_length=100, verbose_name='Payment method')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Middle name')),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('mobile', models.CharField(max_length=255, verbose_name='Mobile number')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('comment', models.TextField(blank=True, max_length=1000, verbose_name='Comment')),
                ('delivery', delivery.models.DeliveryMethodField(null=True, on_delete=django.db.models.deletion.CASCADE, to='delivery.DeliveryMethod', verbose_name='Delivery method')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_retail', models.FloatField(verbose_name='Retail price')),
                ('price_wholesale', models.FloatField(default=0, verbose_name='Wholesale price')),
                ('price_usd', models.FloatField(default=0)),
                ('price_eur', models.FloatField(default=0)),
                ('price_uah', models.FloatField(default=0)),
                ('initial_currency', models.PositiveIntegerField(choices=[(980, 'UAH'), (840, 'USD'), (978, 'EUR')], default=980, verbose_name='Currency')),
                ('qty', models.PositiveIntegerField(default=1, verbose_name='Quantity')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order', verbose_name='Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.Product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Ordered product',
                'verbose_name_plural': 'Ordered products',
            },
        ),
    ]
