# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0009_alerte_groupe'),
    ]

    operations = [
        migrations.AddField(
            model_name='alerte',
            name='description',
            field=models.TextField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='alerte',
            name='nom',
            field=models.CharField(max_length=45, blank=True),
        ),
    ]
