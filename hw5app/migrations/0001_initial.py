# Generated by Django 5.1.7 on 2025-04-06 11:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('registration_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('added_date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='hw5app.client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw5app.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw5app.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='hw5app.OrderProduct', to='hw5app.product'),
        ),
    ]
