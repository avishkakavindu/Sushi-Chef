# Generated by Django 3.1.5 on 2021-01-27 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0052_auto_20210118_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 6, 13, 8, 9, 869214)),
        ),
    ]