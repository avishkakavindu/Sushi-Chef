# Generated by Django 3.1.2 on 2021-01-18 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_auto_20210118_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 28, 12, 3, 5, 537237)),
        ),
    ]
