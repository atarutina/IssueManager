# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_bug_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='bug',
            name='issue_type',
            field=models.CharField(choices=[('Bug', 'BUG'), ('Feature', 'FTR')], default='Bug', max_length=10),
        ),
    ]
