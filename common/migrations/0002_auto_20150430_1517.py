# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmable',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('requested', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('author',
                 models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Applicable',
            fields=[
                ('confirmable_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='common.Confirmable')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('common.confirmable',),
        ),
        migrations.AddField(
            model_name='confirmation',
            name='confirmable',
            field=models.ForeignKey(to='common.Confirmable'),
        ),
        migrations.AddField(
            model_name='confirmation',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_common.confirmation_set+',
                                    editable=False, to='contenttypes.ContentType',
                                    null=True),
        ),
        migrations.AddField(
            model_name='confirmable',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_common.confirmable_set+',
                                    editable=False, to='contenttypes.ContentType',
                                    null=True),
        ),
    ]
