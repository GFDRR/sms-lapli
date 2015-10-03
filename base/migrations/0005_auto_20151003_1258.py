# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151003_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectioncommunale',
            name='nomOfficiel',
            field=models.CharField(unique=True, max_length=45, blank=True),
        ),
        migrations.AlterField(
            model_name='sectioncommunale',
            name='sectionCommunale',
            field=models.CharField(max_length=45, verbose_name=b'Section Communale'),
        ),
    ]
