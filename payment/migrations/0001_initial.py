# Generated by Django 5.0.6 on 2024-05-13 06:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cvc', models.CharField(max_length=3)),
                ('date', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=19)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Payment Card',
                'verbose_name_plural': 'Payment Cards',
                'db_table': 'payment_cards',
            },
        ),
        migrations.CreateModel(
            name='ShippingInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=40)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Shipping Information',
                'verbose_name_plural': 'Shipping Informations',
                'db_table': 'shipping_informations',
            },
        ),
    ]