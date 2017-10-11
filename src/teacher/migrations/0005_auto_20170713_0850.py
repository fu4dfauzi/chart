# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20170713_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='contact',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='years_of_experience',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]