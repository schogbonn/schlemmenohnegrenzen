# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_auto_20170605_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='handy2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]