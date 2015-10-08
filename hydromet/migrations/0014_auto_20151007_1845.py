# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0013_auto_20151007_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
