# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-09 20:57
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('requirements', ckeditor.fields.RichTextField(blank=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.Program')),
            ],
        ),
    ]
