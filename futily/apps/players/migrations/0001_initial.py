# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0002_auto_20160924_1840'),
        ('nations', '0001_initial'),
        ('clubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('ea_id', models.PositiveIntegerField()),
                ('cached_url', models.CharField(max_length=1000, null=True, blank=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('common_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('image', models.CharField(max_length=255, null=True, blank=True)),
                ('image_sm', models.CharField(max_length=255, null=True, blank=True)),
                ('image_md', models.CharField(max_length=255, null=True, blank=True)),
                ('image_lg', models.CharField(max_length=255, null=True, blank=True)),
                ('image_special_totw_md', models.CharField(max_length=255, null=True, blank=True)),
                ('image_special_totw_lg', models.CharField(max_length=255, null=True, blank=True)),
                ('position', models.CharField(blank=True, max_length=3, null=True, choices=[(b'GK', b'GK'), (b'RWB', b'RWB'), (b'RB', b'RB'), (b'CB', b'CB'), (b'LB', b'LB'), (b'LWB', b'LWB'), (b'CDM', b'CDM'), (b'CM', b'CM'), (b'CAM', b'CAM'), (b'RM', b'RM'), (b'RW', b'RW'), (b'RF', b'RF'), (b'LM', b'LM'), (b'LW', b'LW'), (b'LF', b'LF'), (b'CF', b'CF'), (b'ST', b'ST')])),
                ('position_full', models.CharField(max_length=100, null=True, blank=True)),
                ('position_line', models.CharField(blank=True, max_length=3, null=True, choices=[(b'GK', b'Goalkeepers'), (b'DEF', b'Defenders'), (b'MID', b'Midfielders'), (b'ATT', b'Attackers')])),
                ('playstyle', models.CharField(max_length=100, null=True, blank=True)),
                ('playstyle_id', models.CharField(max_length=100, null=True, blank=True)),
                ('height', models.PositiveIntegerField(null=True, blank=True)),
                ('weight', models.PositiveIntegerField(null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('age', models.PositiveIntegerField(null=True, blank=True)),
                ('acceleration', models.PositiveIntegerField(null=True, blank=True)),
                ('aggression', models.PositiveIntegerField(null=True, blank=True)),
                ('agility', models.PositiveIntegerField(null=True, blank=True)),
                ('balance', models.PositiveIntegerField(null=True, blank=True)),
                ('ball_control', models.PositiveIntegerField(null=True, blank=True)),
                ('crossing', models.PositiveIntegerField(null=True, blank=True)),
                ('curve', models.PositiveIntegerField(null=True, blank=True)),
                ('dribbling', models.PositiveIntegerField(null=True, blank=True)),
                ('finishing', models.PositiveIntegerField(null=True, blank=True)),
                ('free_kick_accuracy', models.PositiveIntegerField(null=True, blank=True)),
                ('gk_diving', models.PositiveIntegerField(null=True, blank=True)),
                ('gk_handling', models.PositiveIntegerField(null=True, blank=True)),
                ('gk_kicking', models.PositiveIntegerField(null=True, blank=True)),
                ('gk_positioning', models.PositiveIntegerField(null=True, blank=True)),
                ('gk_reflexes', models.PositiveIntegerField(null=True, blank=True)),
                ('heading_accuracy', models.PositiveIntegerField(null=True, blank=True)),
                ('interceptions', models.PositiveIntegerField(null=True, blank=True)),
                ('jumping', models.PositiveIntegerField(null=True, blank=True)),
                ('long_passing', models.PositiveIntegerField(null=True, blank=True)),
                ('long_shots', models.PositiveIntegerField(null=True, blank=True)),
                ('marking', models.PositiveIntegerField(null=True, blank=True)),
                ('penalties', models.PositiveIntegerField(null=True, blank=True)),
                ('positioning', models.PositiveIntegerField(null=True, blank=True)),
                ('potential', models.PositiveIntegerField(null=True, blank=True)),
                ('reactions', models.PositiveIntegerField(null=True, blank=True)),
                ('short_passing', models.PositiveIntegerField(null=True, blank=True)),
                ('shot_power', models.PositiveIntegerField(null=True, blank=True)),
                ('sliding_tackle', models.PositiveIntegerField(null=True, blank=True)),
                ('sprint_speed', models.PositiveIntegerField(null=True, blank=True)),
                ('standing_tackle', models.PositiveIntegerField(null=True, blank=True)),
                ('stamina', models.PositiveIntegerField(null=True, blank=True)),
                ('strength', models.PositiveIntegerField(null=True, blank=True)),
                ('vision', models.PositiveIntegerField(null=True, blank=True)),
                ('volleys', models.PositiveIntegerField(null=True, blank=True)),
                ('foot', models.CharField(max_length=10, null=True, blank=True)),
                ('skill_moves', models.PositiveIntegerField(null=True, blank=True)),
                ('weak_foot', models.PositiveIntegerField(null=True, blank=True)),
                ('traits', jsonfield.fields.JSONField(null=True, blank=True)),
                ('specialities', jsonfield.fields.JSONField(null=True, blank=True)),
                ('workrate_att', models.CharField(max_length=10, null=True, blank=True)),
                ('workrate_def', models.CharField(max_length=10, null=True, blank=True)),
                ('player_type', models.CharField(max_length=100, null=True, blank=True)),
                ('item_type', models.CharField(max_length=100, null=True, blank=True)),
                ('overall_rating', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_1', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_2', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_3', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_4', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_5', models.PositiveIntegerField(null=True, blank=True)),
                ('card_att_6', models.PositiveIntegerField(null=True, blank=True)),
                ('quality', models.CharField(db_index=True, max_length=100, null=True, blank=True)),
                ('color', models.CharField(db_index=True, max_length=100, null=True, blank=True)),
                ('is_gk', models.NullBooleanField(default=False)),
                ('is_special_type', models.NullBooleanField(default=False)),
                ('is_loan', models.NullBooleanField(default=False)),
                ('model_name', models.CharField(max_length=100, null=True, blank=True)),
                ('base_id', models.PositiveIntegerField(max_length=100, null=True, blank=True)),
                ('club', models.ForeignKey(blank=True, to='clubs.Club', null=True)),
                ('league', models.ForeignKey(blank=True, to='leagues.League', null=True)),
                ('nation', models.ForeignKey(blank=True, to='nations.Nation', null=True)),
            ],
            options={
                'ordering': ['-overall_rating', '-ea_id'],
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
    ]
