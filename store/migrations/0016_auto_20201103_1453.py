# Generated by Django 3.1.2 on 2020-11-03 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20201026_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
    ]