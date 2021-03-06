# Generated by Django 3.1.2 on 2021-01-04 11:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_auto_20210104_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 14, 16, 47, 45, 749025)),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerreview_set', to='store.customer'),
        ),
    ]
