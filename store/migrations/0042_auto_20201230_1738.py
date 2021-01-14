# Generated by Django 3.1.2 on 2020-12-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_chef_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='customer',
        ),
        migrations.AddField(
            model_name='chefreview',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=models.SET('Anonumous User'), related_name='chefreview_set', to='store.customer'),
            preserve_default=False,
        ),
    ]