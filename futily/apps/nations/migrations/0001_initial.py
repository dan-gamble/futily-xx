# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nation',
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
                ('image', models.CharField(max_length=255, null=True, blank=True)),
                ('image_sm', models.CharField(max_length=255, null=True, blank=True)),
                ('image_md', models.CharField(max_length=255, null=True, blank=True)),
                ('image_lg', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Nation',
                'verbose_name_plural': 'Nations',
            },
        ),
    ]
