# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-12-22 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vmprofile', '0008_auto_20161222_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpuprofile',
            name='arch',
        ),
        migrations.RemoveField(
            model_name='cpuprofile',
            name='os',
        ),
        migrations.AddField(
            model_name='runtimedata',
            name='arch',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='runtimedata',
            name='os',
            field=models.CharField(default='', max_length=25),
        ),
    ]
