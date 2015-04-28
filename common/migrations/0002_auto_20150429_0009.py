# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='Group',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                   primary_key=True, serialize=False,
                                                   to='auth.Group')),
                ('applicable',
                 models.ForeignKey(related_name='packages', to='common.Applicable')),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('accepted', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('group', models.ForeignKey(to='common.Group')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('group', models.ForeignKey(to='common.Group')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(to='common.Questionnaire'),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                         through='common.Participation'),
        ),
    ]
