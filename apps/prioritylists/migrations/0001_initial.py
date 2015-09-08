# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import common.util


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(null=True, blank=True)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_prioritylists.priority_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.CreateModel(
            name='PriorityList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commitment', models.ForeignKey(to='teams.Commitment')),
                ('event', models.ForeignKey(to='events.BaseEvent')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_prioritylists.prioritylist_set+', editable=False, to='contenttypes.ContentType', null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='prioritylists.Priority')),
            ],
            options={
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.AlterUniqueTogether(
            name='prioritylist',
            unique_together=set([('event', 'commitment')]),
        ),
        migrations.AddField(
            model_name='priority',
            name='priority_list',
            field=models.ForeignKey(to='prioritylists.PriorityList'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='priority',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='priority',
            unique_together=set([('priority', 'priority_list')]),
        ),
    ]
