# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='organizing_committee',
            field=models.ManyToManyField(to='teams.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name=b'events',
                                         through='events.Participation',
                                         to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='target',
            field=models.ForeignKey(editable=False, to='events.Event'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('applicant', 'target')]),
        ),
        migrations.CreateModel(
            name='IncomingApplication',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('events.application',),
        ),
        migrations.CreateModel(
            name='OutgoingApplication',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('events.application',),
        ),
    ]
