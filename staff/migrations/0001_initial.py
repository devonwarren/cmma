# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 02:04
from __future__ import unicode_literals

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, null=True, populate_from='__str__', unique=True, verbose_name='URL')),
                ('about', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
