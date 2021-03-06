# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-01 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        #('disturbance', '0005_auto_20180928_1423'),
        ('disturbance', '0007_auto_20180928_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compliance',
            name='customer_status',
            field=models.CharField(choices=[('due', 'Due'), ('future', 'Future'), ('with_assessor', 'Under Review'), ('approved', 'Approved'), ('discarded', 'Discarded')], default='future', max_length=20),
        ),
        migrations.AlterField(
            model_name='compliance',
            name='processing_status',
            field=models.CharField(choices=[('due', 'Due'), ('future', 'Future'), ('with_assessor', 'With Assessor'), ('approved', 'Approved'), ('discarded', 'Discarded')], max_length=20),
        ),
        # migrations.AlterField(
        #     model_name='proposaltype',
        #     name='name',
        #     field=models.CharField(choices=[('Disturbance', 'Disturbance'), ('Apiary', 'Apiary')], default='Disturbance', max_length=24, verbose_name='Application name (eg. Disturbance, Apiary)'),
        # ),
    ]
