# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0001_initial'),
        ('events', '0007_auto_20150113_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='feedbacksheet',
            field=models.ForeignKey(blank=True, to='feedback.QuestionSet', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participation',
            name='feedback',
            field=models.OneToOneField(null=True, blank=True, to='feedback.AnswerSet'),
            preserve_default=True,
        ),
    ]
