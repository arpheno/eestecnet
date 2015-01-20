# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20150120_1835'),
        ('events', '0008_auto_20150115_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='questionaire',
            field=models.OneToOneField(null=True, blank=True, to='feedback.AnswerSet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='questionaire',
            field=models.ForeignKey(related_name='eventstwo', blank=True, to='feedback.QuestionSet', help_text=b'Optional: If you want your participants to answer more questions other than writing about their motivation, you can include it here', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='feedbacksheet',
            field=models.ForeignKey(related_name='events', blank=True, to='feedback.QuestionSet', null=True),
            preserve_default=True,
        ),
    ]
