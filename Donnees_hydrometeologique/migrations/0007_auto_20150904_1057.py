# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_hydrometeologique', '0006_auto_20150903_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationpluviometrique',
            name='quantite',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15),
        ),
    ]
