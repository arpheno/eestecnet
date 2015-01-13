# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteFeedback',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True, auto_created=True)),
                ('content', models.TextField()),
                ('read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, editable=False,
                                           to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WebsiteFeedbackImage',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('image', models.ImageField(upload_to=b'userfeedback')),
                ('entity', models.ForeignKey(to='pages.WebsiteFeedback')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
