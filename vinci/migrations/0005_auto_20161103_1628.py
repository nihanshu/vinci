# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 16:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vinci', '0004_image_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='path',
            new_name='filepath',
        ),
        migrations.RemoveField(
            model_name='image',
            name='is_landscape',
        ),
    ]