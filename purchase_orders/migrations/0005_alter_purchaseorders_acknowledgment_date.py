# Generated by Django 5.0.4 on 2024-05-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase_orders', '0004_purchaseorders_order_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorders',
            name='acknowledgment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]