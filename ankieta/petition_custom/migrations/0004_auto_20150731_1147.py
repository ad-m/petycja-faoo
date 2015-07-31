# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('petition_custom', '0003_auto_20150728_0359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('second_name', models.CharField(max_length=100, verbose_name='Second name')),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('modified_on', models.DateTimeField(auto_now=True, verbose_name='Modified on')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('organization', models.CharField(max_length=100, verbose_name='Organization')),
                ('newsletter', models.BooleanField(default=True, verbose_name='Newsletter acceptation')),
                ('petition', models.ForeignKey(verbose_name='Petition', to=settings.PETITION_PETITION_MODEL)),
            ],
            options={
                'swappable': 'PETITION_SIGNATURE_MODEL',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='petition',
            options={},
        ),
        migrations.AlterField(
            model_name='petition',
            name='text_top',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
