# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0006_auto_20160316_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='hauteur',
            field=models.DecimalField(blank=True, null=True, default=0, max_digits=8, decimal_places=2),
        ),
    ]
