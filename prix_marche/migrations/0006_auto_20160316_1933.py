# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prix_marche', '0005_auto_20160315_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marche',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='marche',
            name='longitude',
        ),
    ]
