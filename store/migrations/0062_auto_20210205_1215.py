# Generated by Django 3.1.5 on 2021-02-05 06:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0061_auto_20210201_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payherepaymentdetail',
            name='payment_id',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Payhere', 'Payhere'), ('Cash On Delivery', 'Cash On Delivery')], default='Payhere', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 15, 12, 14, 27, 684911)),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
