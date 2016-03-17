# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prix_marche', '0006_auto_20160316_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marche',
            name='hauteur',
            field=models.DecimalField(verbose_name='Hauteur', null=True, default=0, max_digits=8, decimal_places=6, blank=True),
        ),
    ]
