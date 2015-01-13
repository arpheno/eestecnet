# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('headline', models.CharField(unique=True, max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('entry_image', models.ImageField(upload_to=b'entryimages')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('privileged', models.BooleanField(default=False)),
                ('board', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
