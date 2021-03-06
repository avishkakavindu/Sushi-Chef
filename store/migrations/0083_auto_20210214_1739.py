# Generated by Django 3.1.2 on 2021-02-14 12:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0082_auto_20210212_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 24, 17, 39, 16, 990168)),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productreview_set', to='store.customer'),
        ),
    ]
