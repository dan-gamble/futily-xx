# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20151002_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=2048)),
                ('content', models.TextField()),
                ('twitter_link', models.CharField(max_length=4096)),
                ('linkedin_link', models.CharField(max_length=4096)),
                ('email_link', models.CharField(max_length=4096)),
            ],
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=1024, null=True, blank=True)),
                ('link_text', models.CharField(max_length=512)),
                ('target', models.CharField(default=b'_self', max_length=128, choices=[(b'_blank', b'New window'), (b'_self', b'Same window')])),
                ('order', models.PositiveIntegerField(default=b'0')),
            ],
            options={
                'ordering': ('order', 'pk'),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FooterLinkGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=1024, null=True, blank=True)),
                ('link_text', models.CharField(max_length=512)),
                ('target', models.CharField(default=b'_self', max_length=128, choices=[(b'_blank', b'New window'), (b'_self', b'Same window')])),
                ('order', models.PositiveIntegerField(default=b'0')),
                ('page', models.ForeignKey(blank=True, to='pages.Page', null=True)),
            ],
            options={
                'ordering': ('order', 'pk'),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='footerlink',
            name='group',
            field=models.ForeignKey(related_name='children', to='footer.FooterLinkGroup'),
        ),
        migrations.AddField(
            model_name='footerlink',
            name='page',
            field=models.ForeignKey(blank=True, to='pages.Page', null=True),
        ),
    ]
