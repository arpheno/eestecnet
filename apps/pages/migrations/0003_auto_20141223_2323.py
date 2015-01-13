# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0002_websitefeedback_websitefeedbackimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitefeedback',
            name='email',
            field=models.EmailField(max_length=75, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='websitefeedback',
            name='subject',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
