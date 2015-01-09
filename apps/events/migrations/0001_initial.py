# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('letter', models.TextField(null=True, blank=True)),
                ('priority', models.IntegerField(null=True, blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('category', models.CharField(default=b'workshop', max_length=40,
                                              choices=[(b'ssa', b'Soft Skills Academy'),
                                                       (b'exchange', b'Exchange'),
                                                       (b'workshop', b'Workshop'), (
                                                       b'operational',
                                                       b'Operational Event'),
                                                       (b'training', b'Training'),
                                                       (b'imw', b'IMW'), (b'recruitment',
                                                                          b'recruitment')])),
                ('scope', models.CharField(default=b'international', max_length=15,
                                           choices=[(b'local', b'Local'), (
                                           b'international', b'International')])),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('thumbnail', models.ImageField(upload_to=b'event_thumbnails')),
                ('max_participants', models.PositiveIntegerField(null=True, blank=True)),
                ('participation_fee', models.PositiveIntegerField(default=0)),
                ('location',
                 models.CharField(help_text='Where are you planning your Event?',
                                  max_length=30, null=True, blank=True)),
                (
                'start_date', models.DateField(help_text='When does your Event start?')),
                ('end_date',
                 models.DateField(help_text='When does your Event end?', null=True,
                                  blank=True)),
                ('deadline',
                 models.DateTimeField(help_text='Until when can participants apply?',
                                      null=True, blank=True)),
                ('description', models.TextField(
                    help_text='Please provide a detailed description for interesed '
                              'readers')),
                ('pax_report', models.TextField(null=True, blank=True)),
                ('organizer_report', models.TextField(null=True, blank=True)),
                ('applicants', models.ManyToManyField(related_name='applications',
                                                      through='events.Application',
                                                      to=settings.AUTH_USER_MODEL)),
                ('organizers', models.ManyToManyField(related_name='events_organized',
                                                      to=settings.AUTH_USER_MODEL)),
                ('organizing_committee', models.ManyToManyField(to='teams.Team')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('image', models.ImageField(upload_to=b'eventimages')),
                (
                'property', models.ForeignKey(related_name='images', to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneralQuestion',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.IntegerField(blank=True, max_length=10, null=True,
                                               help_text=b'1 is worst, 5 is best',
                                               choices=[(1, 1), (2, 2), (3, 3), (4, 4),
                                                        (5, 5)])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
                (
                'confirmation', models.TextField(null=True, editable=False, blank=True)),
                ('participant', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(to='events.Event')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('sheets', models.ManyToManyField(related_name='sheets_rel_+', null=True,
                                                  to='events.Sheet', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('arrival', models.DateTimeField()),
                ('arrive_by', models.CharField(max_length=20,
                                               choices=[(b'plane', b'Plane'),
                                                        (b'bus', b'Bus'),
                                                        (b'train', b'Train'),
                                                        (b'car', b'Car'),
                                                        (b'other', b'other'),
                                                        (b'own', b'Own arrival')])),
                ('arrival_number', models.CharField(max_length=30, null=True,
                                                    verbose_name='Bus/Train/Plane Number',
                                                    blank=True)),
                ('departure', models.DateTimeField(null=True, blank=True)),
                ('depart_by', models.CharField(blank=True, max_length=20, null=True,
                                               choices=[(b'plane', b'Plane'),
                                                        (b'bus', b'Bus'),
                                                        (b'train', b'Train'),
                                                        (b'car', b'Car'),
                                                        (b'other', b'other'),
                                                        (b'own', b'Own departure')])),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participation',
            name='transportation',
            field=models.OneToOneField(null=True, blank=True,
                                       to='events.Transportation'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mcquestion',
            name='sheet',
            field=models.ForeignKey(blank=True, to='events.Sheet', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='generalquestion',
            name='sheet',
            field=models.ForeignKey(to='events.Sheet'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='events',
                                         through='events.Participation',
                                         to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='target',
            field=models.ForeignKey(to='events.Event'),
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
