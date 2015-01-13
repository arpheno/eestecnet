# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0003_auto_20141117_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='application',
            name='target',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
