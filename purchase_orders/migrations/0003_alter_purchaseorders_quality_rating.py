# Generated by Django 5.0.4 on 2024-05-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0002_alter_purchaseorders_acknowledgment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorders',
            name='quality_rating',
            field=models.FloatField(blank=True, null=True),
        ),
    ]