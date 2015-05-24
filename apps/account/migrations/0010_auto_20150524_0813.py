# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150113_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eestecer',
            name='curriculum_vitae',
            field=models.FileField(default=b'/media/cvs/example.dat', null=True, upload_to=b'cvs', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='eestecer',
            name='thumbnail',
            field=models.ImageField(default=b'/media/cvs/example.jpg', null=True, upload_to=b'users', blank=True),
            preserve_default=True,
        ),
    ]
