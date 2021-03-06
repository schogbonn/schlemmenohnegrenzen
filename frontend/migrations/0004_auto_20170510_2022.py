# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_household_signup_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='cluster',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='frontend.Cluster'),
            preserve_default=False,
        ),
    ]
