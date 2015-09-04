# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_hydrometeologique', '0008_auto_20150904_1117'),
        ('Donnees_de_base', '0009_auto_20150904_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commune',
            name='departement',
        ),
        migrations.DeleteModel(
            name='Poste',
        ),
        migrations.RemoveField(
            model_name='sectioncommunale',
            name='commune',
        ),
        migrations.RemoveField(
            model_name='sitesentinelle',
            name='sectionCommunale',
        ),
        migrations.DeleteModel(
            name='Commune',
        ),
        migrations.DeleteModel(
            name='Departement',
        ),
        migrations.DeleteModel(
            name='SectionCommunale',
        ),
        migrations.DeleteModel(
            name='SiteSentinelle',
        ),
    ]
