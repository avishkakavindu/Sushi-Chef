# Generated by Django 3.1.2 on 2020-12-25 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_auto_20201225_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.coupon'),
        ),
    ]
