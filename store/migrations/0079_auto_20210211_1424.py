# Generated by Django 3.1.2 on 2021-02-11 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0078_auto_20210211_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 14, 24, 38, 841574)),
        ),
    ]
