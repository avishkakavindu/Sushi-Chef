# Generated by Django 3.1.2 on 2021-02-11 08:27

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0077_auto_20210211_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.AlterField(
            model_name='coupon',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 21, 13, 57, 44, 188696)),
        ),
        migrations.CreateModel(
            name='ChefReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.DecimalField(decimal_places=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chefreview_set', to='store.chef')),
                ('customer', models.ForeignKey(on_delete=models.SET('Anonumous User'), related_name='chefreview_set', to='store.customer')),
            ],
        ),
    ]
