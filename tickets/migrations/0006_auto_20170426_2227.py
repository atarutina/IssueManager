# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_auto_20170426_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Delivered', 'Delivered'), ('Fixed', 'Fixed'), ('Closed', 'Closed')], default='Open', max_length=10),
        ),
    ]