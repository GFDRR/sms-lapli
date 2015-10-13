# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_auto_20151008_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departement',
            name='departement',
            field=models.CharField(choices=[('Ouest', 'OUEST'), ('Nord', 'NORD'), ('Nordouest', 'NORD-OUEST'), ('Nordest', 'NORD-EST'), ('Sud', 'SUD'), ('Sudest', 'SUD-EST'), ('Artibonite', 'ARTIBONITE'), ('Nippes', 'NIPPES'), ('Centre', 'CENTRE'), ('Grandanse', "GRAND'ANSE")], max_length=40, verbose_name='Departement'),
        ),
    ]
