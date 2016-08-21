# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-21 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20160811_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='club',
            options={'ordering': ['-total_players', '-average_rating', 'name'], 'verbose_name': 'Club', 'verbose_name_plural': 'Clubs'},
        ),
        migrations.AddField(
            model_name='club',
            name='average_rating',
            field=models.FloatField(default=0),
        ),
    ]