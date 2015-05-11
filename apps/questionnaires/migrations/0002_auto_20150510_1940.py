# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_auto_20150506_1104'),
        ('contenttypes', '0001_initial'),
        ('questionnaires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('answer', models.TextField()),
                ('polymorphic_ctype',
                 models.ForeignKey(related_name='polymorphic_questionnaires.answer_set+',
                                   editable=False, to='contenttypes.ContentType',
                                   null=True)),
                ('question', models.ForeignKey(to='questionnaires.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('participation', models.ForeignKey(to='accounts.Participation')),
                ('polymorphic_ctype', models.ForeignKey(
                    related_name='polymorphic_questionnaires.response_set+',
                    editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='answer',
            name='response',
            field=models.ForeignKey(to='questionnaires.Response'),
            preserve_default=True,
        ),
    ]
