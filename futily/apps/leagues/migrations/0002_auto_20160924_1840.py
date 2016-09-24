# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='slug',
            field=models.SlugField(unique=True, null=True, blank=True),
        ),
    ]
