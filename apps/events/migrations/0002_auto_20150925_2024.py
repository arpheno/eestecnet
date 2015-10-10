# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('letter', models.TextField(null=True, blank=True)),
                ('priority', models.IntegerField(null=True, blank=True)),
                ('accepted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('thumbnail', models.ImageField(upload_to=b'event_thumbnails')),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', editable=False)),
                ('max_participants', models.PositiveIntegerField(null=True, blank=True)),
                ('participation_fee', models.PositiveIntegerField(default=0)),
                ('scope', models.CharField(default=b'international', max_length=15)),
                ('location', models.CharField(max_length=30, null=True, blank=True)),
                ('start_date', models.DateField(help_text='When does your Event start?')),
                ('end_date', models.DateField(null=True, blank=True)),
                ('deadline', models.DateTimeField(null=True, blank=True)),
                ('pax_report', models.TextField(null=True, blank=True)),
                ('organizer_report', models.TextField(null=True, blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'eventimages')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('confirmation', models.TextField(null=True, editable=False, blank=True)),
                ('target', models.ForeignKey(to='events.Event')),
            ],
            options={
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival', models.DateTimeField()),
                ('arrive_by', models.CharField(max_length=20, choices=[(b'plane', b'Plane'), (b'bus', b'Bus'), (b'train', b'Train'), (b'car', b'Car'), (b'other', b'other'), (b'own', b'Own arrival')])),
                ('arrival_number', models.CharField(max_length=30, null=True, verbose_name='Bus/Train/Plane Number', blank=True)),
                ('departure', models.DateTimeField(null=True, blank=True)),
                ('depart_by', models.CharField(blank=True, max_length=20, null=True, choices=[(b'plane', b'Plane'), (b'bus', b'Bus'), (b'train', b'Train'), (b'car', b'Car'), (b'other', b'other'), (b'own', b'Own departure')])),
                ('comment', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='participation',
            name='transportation',
            field=models.OneToOneField(null=True, blank=True, to='events.Transportation'),
            preserve_default=True,
        ),
    ]
