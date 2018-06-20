# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-20 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0007_auto_20160518_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processflowdiagramitem',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='processflowdiagramitem',
            name='left',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='processflowdiagramitem',
            name='top',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='processflowdiagramitem',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
