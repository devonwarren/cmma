# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_rank'),
        ('users', '0002_auto_20160409_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ranks',
            field=models.ManyToManyField(blank=True, to='programs.Rank'),
        ),
    ]
