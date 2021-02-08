# Generated by Django 3.1.5 on 2021-02-05 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0063_auto_20210205_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 15, 12, 27, 54, 119130)),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Payhere', 'payhere'), ('Cash On Delivery', 'cashondelivery')], max_length=50),
        ),
    ]