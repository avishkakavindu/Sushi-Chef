# Generated by Django 3.1.5 on 2021-01-30 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0056_auto_20210130_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 14, 40, 0, 574997)),
        ),
    ]
