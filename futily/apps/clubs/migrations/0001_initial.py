# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('total_players', models.PositiveIntegerField(default=0)),
                ('total_bronze', models.PositiveIntegerField(default=0)),
                ('total_silver', models.PositiveIntegerField(default=0)),
                ('total_gold', models.PositiveIntegerField(default=0)),
                ('total_informs', models.PositiveIntegerField(default=0)),
                ('total_special', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cached_url', models.CharField(max_length=1000, null=True, blank=True)),
                ('name', models.CharField(max_length=100)),
                ('name_abbr', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('image_dark_sm', models.CharField(max_length=255, null=True, blank=True)),
                ('image_dark_md', models.CharField(max_length=255, null=True, blank=True)),
                ('image_dark_lg', models.CharField(max_length=255, null=True, blank=True)),
                ('image_normal_sm', models.CharField(max_length=255, null=True, blank=True)),
                ('image_normal_md', models.CharField(max_length=255, null=True, blank=True)),
                ('image_normal_lg', models.CharField(max_length=255, null=True, blank=True)),
                ('league', models.ForeignKey(blank=True, to='leagues.League', null=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Club',
                'verbose_name_plural': 'Clubs',
            },
        ),
    ]
