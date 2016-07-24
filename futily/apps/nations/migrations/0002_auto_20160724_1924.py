# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nation',
            options={'ordering': ['name'], 'verbose_name': 'Nation', 'verbose_name_plural': 'Nations'},
        ),
    ]
