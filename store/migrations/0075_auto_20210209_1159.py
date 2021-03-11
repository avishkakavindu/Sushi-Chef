# Generated by Django 3.1.2 on 2021-02-09 06:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0074_auto_20210208_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='telephone_no',
            field=models.CharField(default='0123456789', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 19, 11, 59, 1, 171409)),
        ),
    ]