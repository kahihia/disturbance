# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-01 06:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mooring', '0116_refundfailed'),
    ]

    operations = [
        migrations.AddField(
            model_name='refundfailed',
            name='completed_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='refundfailed',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
