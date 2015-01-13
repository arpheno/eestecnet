# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='team',
            field=models.ForeignKey(editable=False, to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set([('user', 'team')]),
        ),
        migrations.AddField(
            model_name='entry',
            name='author',
            field=models.ManyToManyField(to='teams.Team'),
            preserve_default=True,
        ),
    ]
