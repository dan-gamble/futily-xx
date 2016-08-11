# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-11 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clubs.Club'),
        ),
        migrations.AlterField(
            model_name='player',
            name='league',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nations.Nation'),
        ),
    ]