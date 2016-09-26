# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def create_nations(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Nations = apps.get_model('nations', 'Nations')
    Page = apps.get_model('pages', 'Page')

    content_type = ContentType.objects.get_for_model(Nations)

    page = Page.objects.create(
        title='Nations', slug='nations', content_type=content_type, parent=Page.objects.get(id=1)
    )

    Nations.objects.create(page=page)


def assign_nations(apps, schema_editor):
    Nation = apps.get_model('nations', 'Nation')
    Nations = apps.get_model('nations', 'Nations')

    for nation in Nation.objects.all():
        nation.page = Nations.objects.get(page__slug='nations')
        nation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('nations', '0003_auto_20160925_1718'),
    ]

    operations = [
        # migrations.RunPython(create_nations),
        migrations.AddField(
            model_name='nation',
            name='page',
            field=models.ForeignKey(default=9, to='nations.Nations'),
            preserve_default=False,
        ),
        # migrations.RunPython(assign_nations)
    ]
