# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0003_auto_20160925_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='nation',
            name='page',
            field=models.ForeignKey(to='nations.Nations', null=True),
        ),
    ]
