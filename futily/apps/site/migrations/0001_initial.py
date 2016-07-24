# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('page', models.OneToOneField(related_name='+', primary_key=True, serialize=False, editable=False, to='pages.Page')),
                ('content_primary', cms.models.fields.HtmlField(verbose_name=b'primary content', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
