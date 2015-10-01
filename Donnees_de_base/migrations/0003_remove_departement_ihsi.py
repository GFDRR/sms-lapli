# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0002_auto_20150930_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departement',
            name='ihsi',
        ),
    ]
