# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

import common.util


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150523_2158'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField()),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_questionnaires.answer_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_questionnaires.question_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('group', models.ForeignKey(to='accounts.Group')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_questionnaires.questionnaire_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('participation', models.ForeignKey(to='accounts.Participation')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_questionnaires.response_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(to='questionnaires.Questionnaire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questionnaires.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='response',
            field=models.ForeignKey(to='questionnaires.Response'),
            preserve_default=True,
        ),
    ]
