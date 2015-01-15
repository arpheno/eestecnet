# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('a', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnswerSet',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('q', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionSet',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.TextField(max_length=30)),
                ('parents',
                 models.ManyToManyField(related_name='parents_rel_+', editable=False,
                                        to='feedback.QuestionSet', blank=True,
                                        help_text=b'Which questionaires do you want to '
                                                  b'include',
                                        null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(to='feedback.QuestionSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answerset',
            name='parent',
            field=models.ForeignKey(to='feedback.QuestionSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(to='feedback.AnswerSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='q',
            field=models.ForeignKey(to='feedback.Question', null=True),
            preserve_default=True,
        ),
    ]
