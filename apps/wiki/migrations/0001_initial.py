# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import froala_editor.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalLink',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('url', models.URLField()),
                ('comment', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('number', models.IntegerField()),
                ('source', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WikiPage',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('content', froala_editor.fields.FroalaField(
                    default=b'This page does not exist yet, you can create it by '
                            b'clicking Update.')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reference',
            name='page',
            field=models.ForeignKey(to='wiki.WikiPage'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='externallink',
            name='page',
            field=models.ForeignKey(to='wiki.WikiPage'),
            preserve_default=True,
        ),
    ]
