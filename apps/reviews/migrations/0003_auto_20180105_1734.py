# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20180103_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='position',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='company',
            field=models.CharField(max_length=150),
        ),
    ]
