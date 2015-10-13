# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(max_length=40, choices=[('Ouest', 'OUEST'), ('Nord', 'NORD'), ('Nordouest', 'NORD-OUEST'), ('Nordest', 'NORD-EST'), ('Sud', 'SUD'), ('Sudest', 'SUD-EST'), ('Artibonite', 'ARTIBONITE'), ('Nippes', 'NIPPES'), ('Centre', 'CENTRE'), ('Grandanse', "GRAND'ANSE")], verbose_name='Departement'),
        ),
    ]
