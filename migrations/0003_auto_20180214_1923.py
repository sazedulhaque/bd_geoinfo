# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-14 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bd_geoinfo', '0002_auto_20180214_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cityarea',
            old_name='name_bd',
            new_name='name_bn',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='name_bd',
            new_name='name_bn',
        ),
        migrations.RenameField(
            model_name='division',
            old_name='name_bd',
            new_name='name_bn',
        ),
        migrations.RenameField(
            model_name='union',
            old_name='name_bd',
            new_name='name_bn',
        ),
        migrations.RenameField(
            model_name='upazila',
            old_name='name_bd',
            new_name='name_bn',
        ),
    ]
