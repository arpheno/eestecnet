# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('teams', '0003_auto_20150113_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'permissions': (('view_board', 'Can view board'),)},
        ),
        migrations.AlterModelOptions(
            name='memberimage',
            options={'permissions': (('view_memberimage', 'Can view memberimage'),)},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'permissions': (('view_team', 'Can view team'),)},
        ),
    ]
