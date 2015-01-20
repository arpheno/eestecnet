# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20150120_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question',
            name='official',
        ),
        migrations.AddField(
            model_name='questionset',
            name='category',
            field=models.CharField(default=b'feedback', max_length=30, choices=[(b'feedback', b'feedback'), (b'questionaire', b'questionaire')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='questionset',
            name='official',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
