# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('polymorphic_ctype',
                 models.ForeignKey(related_name='polymorphic_common.content_set+',
                                   editable=False, to='contenttypes.ContentType',
                                   null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
