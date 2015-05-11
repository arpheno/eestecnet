# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participationconfirmation',
            name='confirmable_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True,
                                       primary_key=True, serialize=False,
                                       to='common.Confirmable'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='participationconfirmation',
            name='confirmation_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True,
                                       to='common.Confirmation'),
            preserve_default=True,
        ),
    ]
