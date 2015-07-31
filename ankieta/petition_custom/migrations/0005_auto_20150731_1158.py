# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition_custom', '0004_auto_20150731_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signature',
            name='organization',
            field=models.CharField(max_length=100, verbose_name='Organization', blank=True),
            preserve_default=True,
        ),
    ]
