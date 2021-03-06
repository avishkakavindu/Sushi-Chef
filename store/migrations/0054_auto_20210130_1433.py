# Generated by Django 3.1.5 on 2021-01-30 09:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0053_auto_20210127_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayherePaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_id', models.CharField(max_length=20)),
                ('order_id', models.CharField(max_length=20)),
                ('payment_id', models.CharField(max_length=20)),
                ('payhere_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payhere_currency', models.CharField(max_length=3)),
                ('method', models.CharField(max_length=10)),
                ('card_holder_name', models.CharField(max_length=255)),
                ('card_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 9, 14, 33, 6, 620781)),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productreview_set', to='store.customer'),
        ),
    ]
