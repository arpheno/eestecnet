# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEvent',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True,
                                                   primary_key=True, serialize=False,
                                                   to='auth.Group')),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('accepted', models.BooleanField(default=False)),
                ('confirmed', models.BooleanField(default=False)),
                ('package', models.ForeignKey(to='events.Package')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('question', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('package', models.ForeignKey(to='events.Package')),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            bases=('events.baseevent',),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('baseevent_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True,
                                      primary_key=True, serialize=False,
                                      to='events.BaseEvent')),
            ],
            bases=('events.baseevent',),
        ),
        migrations.AddField(
            model_name='question',
            name='questionnaire',
            field=models.ForeignKey(to='events.Questionnaire'),
        ),
        migrations.AddField(
            model_name='package',
            name='event',
            field=models.ForeignKey(related_name='packages', to='events.BaseEvent'),
        ),
        migrations.AddField(
            model_name='package',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL,
                                         through='events.Participation'),
        ),
    ]
