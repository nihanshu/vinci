# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 06:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinci', '0010_message_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 11, 29, 1, 10, 46, 580782)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 11, 29, 1, 10, 46, 580104)),
        ),
    ]