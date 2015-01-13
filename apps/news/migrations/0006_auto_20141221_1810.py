# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0005_entry_front_page_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(to='teams.Team'),
        ),
        migrations.AlterField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
