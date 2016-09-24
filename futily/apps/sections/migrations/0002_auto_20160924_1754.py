# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentsection',
            name='type',
            field=models.CharField(max_length=100, choices=[(b'Heros', [('homepage-hero', b'Homepage hero'), ('landing-hero', b'Landing hero')]), (b'Text', [('dual-column', b'Dual column')]), (b'Misc', [('keyline', b'Keyline')])]),
        ),
    ]
