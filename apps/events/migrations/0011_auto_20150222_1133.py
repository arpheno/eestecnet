# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0010_auto_20150124_0131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'permissions': (('view_application', 'Can view Application'),)},
        ),
    ]
