# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songsdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('time_stamp', models.DateTimeField()),
            ],
        ),
    ]
