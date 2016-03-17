# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20160315_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='observatoire',
            name='actif',
            field=models.BooleanField(default=True),
        ),
    ]
