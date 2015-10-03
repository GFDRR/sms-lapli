# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationpluviometrique',
            name='valider',
            field=models.BooleanField(verbose_name=b'Validation'),
        ),
    ]
