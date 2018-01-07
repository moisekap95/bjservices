# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-03 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20170925_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
