# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20170510_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster',
            name='clusterNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='household',
            name='cluster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='frontend.Cluster'),
        ),
    ]