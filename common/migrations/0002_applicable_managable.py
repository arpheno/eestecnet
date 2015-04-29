# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicable',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('polymorphic_ctype',
                 models.ForeignKey(related_name='polymorphic_common.applicable_set+',
                                   editable=False, to='contenttypes.ContentType',
                                   null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Managable',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('polymorphic_ctype',
                 models.ForeignKey(related_name='polymorphic_common.managable_set+',
                                   editable=False, to='contenttypes.ContentType',
                                   null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
