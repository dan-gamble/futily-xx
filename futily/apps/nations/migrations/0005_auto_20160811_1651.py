# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 15:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0004_auto_20160811_1649'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nation',
            old_name='total_informs',
            new_name='total_inform',
        ),
    ]
