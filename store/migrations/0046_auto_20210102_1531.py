# Generated by Django 3.1.2 on 2021-01-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0045_auto_20201231_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='review',
            field=models.TextField(default='Chef review default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productreview',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
