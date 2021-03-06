# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.IntegerField(unique=True)),
                ('date_assigned', models.DateField()),
                ('proof', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_removed', models.DateTimeField(blank=True, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('UPC', models.CharField(max_length=20)),
                ('bottle_size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stray',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_assigned', models.DateField()),
                ('proof', models.DecimalField(decimal_places=2, max_digits=5)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Product')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.Product'),
        ),
    ]
