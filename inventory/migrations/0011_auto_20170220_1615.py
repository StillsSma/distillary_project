# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_remove_inventoryitem_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='date_assigned',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='date_removed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
