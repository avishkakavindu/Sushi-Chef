# Generated by Django 3.1.2 on 2021-01-18 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0050_auto_20210104_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 12, 2, 53, 970875)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(choices=[('Payhere', 'Payhere'), ('Cash On Delivery', 'Cash On Delivery')], max_length=50),
        ),
    ]
