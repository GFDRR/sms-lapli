# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0011_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='unitedemesure',
            name='formule',
            field=models.CharField(default='', verbose_name='Formule', max_length=20),
            preserve_default=False,
        ),
    ]
