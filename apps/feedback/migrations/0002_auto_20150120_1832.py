# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default=b'feedback', max_length=30, choices=[(b'feedback', b'feedback'), (b'questionaire', b'questionaire')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='question',
            name='official',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
