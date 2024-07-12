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
            name='StoreCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Store Category',
                'verbose_name_plural': 'Store Categories',
                'db_table': 'store_categories',
            },
        ),
        migrations.CreateModel(
            name='StoreOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('delivered', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Store Order',
                'verbose_name_plural': 'Store Orders',
                'db_table': 'store_orders',
            },
        ),
        migrations.CreateModel(
            name='StoreProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('picture', models.ImageField(upload_to='uploads/store/products/')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storecategory')),
            ],
            options={
                'verbose_name': 'Store Product',
                'verbose_name_plural': 'Store Products',
                'db_table': 'store_products',
            },
        ),
        migrations.CreateModel(
            name='StoreOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storeorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.storeproduct')),
            ],
            options={
                'verbose_name': 'Store Order Item',
                'verbose_name_plural': 'Store Order Items',
                'db_table': 'store_order_items',
            },
        ),
    ]