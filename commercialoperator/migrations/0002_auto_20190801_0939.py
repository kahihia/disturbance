# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-08-01 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationtype',
            name='licence_fee_1yr',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=6, verbose_name='Licence Fee (1 Year)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationtype',
            name='licence_fee_2mth',
            field=models.DecimalField(decimal_places=2, default=150.0, max_digits=6, verbose_name='Licence Fee (2 Months)'),
            preserve_default=False,
        ),
    ]
