# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('year', models.PositiveIntegerField()),
                ('cp', models.OneToOneField(related_name=b'cp_in_board',
                                            to=settings.AUTH_USER_MODEL)),
                ('treasurer', models.OneToOneField(related_name=b'treasurer_in_board',
                                                   to=settings.AUTH_USER_MODEL)),
                ('vcea', models.OneToOneField(related_name=b'ea_in_board',
                                              to=settings.AUTH_USER_MODEL)),
                ('vcia', models.OneToOneField(related_name=b'ia_in_board',
                                              to=settings.AUTH_USER_MODEL)),
                ('vcpa', models.OneToOneField(related_name=b'pa_in_board',
                                              to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MemberImage',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('image', models.ImageField(upload_to=b'memberimages')),
                ('source', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID', serialize=False, auto_created=True,
                                  primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('type', models.CharField(default=b'lc', max_length=30,
                                          choices=[(b'body', b'Body'),
                                                   (b'team', b'International Team'),
                                                   (b'lc', b'Local Committee'),
                                                   (b'jlc', b'Junior Local Committee'),
                                                   (b'observer', b'Observer')])),
                ('thumbnail',
                 models.ImageField(null=True, upload_to=b'memberthumbs', blank=True)),
                ('thumbsource', models.CharField(max_length=100, null=True, blank=True)),
                ('teamstub', models.TextField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('facebook', models.URLField(null=True, blank=True)),
                ('website', models.URLField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('founded', models.PositiveIntegerField(null=True, blank=True)),
                ('users',
                 models.ManyToManyField(related_name=b'teams', through='news.Membership',
                                        to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='memberimage',
            name='property',
            field=models.ForeignKey(related_name=b'images', to='teams.Team'),
            preserve_default=True,
        ),
    ]
