# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinci', '0006_auto_20161105_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='height',
        ),
        migrations.RemoveField(
            model_name='filter',
            name='width',
        ),
        migrations.AddField(
            model_name='filter',
            name='path',
            field=models.ImageField(default=0, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filter',
            name='url',
            field=models.FileField(upload_to='filters/'),
        ),
    ]