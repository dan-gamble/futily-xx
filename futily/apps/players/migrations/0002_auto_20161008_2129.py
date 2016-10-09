# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ['-rating', 'ea_id'], 'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='overall_rating',
            new_name='rating',
        ),
    ]
