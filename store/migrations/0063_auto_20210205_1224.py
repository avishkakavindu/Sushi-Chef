# Generated by Django 3.1.5 on 2021-02-05 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0062_auto_20210205_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 15, 12, 24, 8, 62167)),
        ),
    ]
