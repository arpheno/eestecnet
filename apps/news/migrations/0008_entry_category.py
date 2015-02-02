# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('news', '0007_auto_20150113_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.CharField(default=b'news', max_length=20,
                                   choices=[(b'news', b'EESTEC News'),
                                            (b'carreer', b'Carreer Offer')]),
            preserve_default=True,
        ),
    ]
