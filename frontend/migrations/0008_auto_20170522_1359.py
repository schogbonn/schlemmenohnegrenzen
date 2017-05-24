# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_remove_cluster_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitingGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitingGroupNum', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='firstVisit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='household1', to='frontend.VisitingGroup'),
        ),
        migrations.AddField(
            model_name='household',
            name='secondVisit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='household2', to='frontend.VisitingGroup'),
        ),
        migrations.AddField(
            model_name='household',
            name='thirdVisit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='household3', to='frontend.VisitingGroup'),
        ),
    ]