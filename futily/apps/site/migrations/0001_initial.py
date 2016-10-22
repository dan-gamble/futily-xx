# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('page', models.OneToOneField(related_name='+', primary_key=True, serialize=False, editable=False, to='pages.Page')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
