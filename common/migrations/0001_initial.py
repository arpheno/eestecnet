# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import common.util


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmable',
            fields=[
                ('confirmable_identifier', models.AutoField(serialize=False, primary_key=True)),
                ('confirmed', models.BooleanField(default=False, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Applicable',
            fields=[
                ('confirmable_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Confirmable')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.confirmable',),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('content', models.TextField(null=True, blank=True)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_common.content_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('full_size', models.ImageField(upload_to=b'images')),
                ('thumbnail', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_common.image_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.util.Reversable),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('string', models.CharField(max_length=200)),
                ('latitude', models.FloatField(null=True, blank=True)),
                ('longitude', models.FloatField(null=True, blank=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_common.location_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Confirmation',
            fields=[
                ('notification_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='common.Notification')),
                ('requested', models.DateField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('confirmable', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='common.Confirmable', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('common.notification',),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=300)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_common.report_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('object_id', models.PositiveIntegerField()),
                ('url', models.URLField(max_length=255)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('polymorphic_ctype', models.ForeignKey(related_name='polymorphic_common.url_set+', editable=False, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='notification',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_common.notification_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='confirmable',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_common.confirmable_set+', editable=False, to='contenttypes.ContentType', null=True),
            preserve_default=True,
        ),
    ]
