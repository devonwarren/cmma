# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 02:11
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='title', unique=True, verbose_name='URL')),
                ('image', models.ImageField(upload_to='programs')),
                ('trainers', models.ManyToManyField(to='staff.Trainer')),
            ],
        ),
    ]
