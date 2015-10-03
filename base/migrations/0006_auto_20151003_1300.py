# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20151003_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectioncommunale',
            name='nomOfficiel',
            field=models.CharField(max_length=45, blank=True),
        ),
    ]
