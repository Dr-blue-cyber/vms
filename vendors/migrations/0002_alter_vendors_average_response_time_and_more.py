# Generated by Django 5.0.4 on 2024-05-07 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendors',
            name='average_response_time',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='fullfillment_rate',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='on_time_delivery_rate',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='quality_rating_avg',
            field=models.FloatField(default=None),
        ),
    ]
