# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_hydrometeologique', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observationpluviometrique',
            name='quantite',
            field=models.DecimalField(default=0, max_digits=15, decimal_places=2),
        ),
    ]
