# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0004_answerset_filled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'permissions': (('view_answer', 'Can view answer'),)},
        ),
        migrations.AlterModelOptions(
            name='answerset',
            options={'permissions': (('view_answerset', 'Can view answerset'),)},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'permissions': (('view_question', 'Can view question'),)},
        ),
        migrations.AlterModelOptions(
            name='questionset',
            options={'permissions': (('view_questionset', 'Can view questionset'),)},
        ),
    ]
