# Generated by Django 3.1.5 on 2021-02-01 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0060_auto_20210201_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 11, 13, 49, 32, 529164)),
        ),
    ]