# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-04 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20170925_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='client',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='link',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
