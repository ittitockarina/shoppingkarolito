# Generated by Django 5.0.6 on 2024-06-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='merchant_order_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
