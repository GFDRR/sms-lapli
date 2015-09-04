# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_hydrometeologique', '0007_auto_20150904_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observationdirectionvent',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationhumidite',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationpluviometrique',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='observationtemperature',
            name='idStation',
        ),
        migrations.RemoveField(
            model_name='stationpluviometrique',
            name='idSiteSeninnelle',
        ),
        migrations.RemoveField(
            model_name='stationpluviometrique',
            name='typeStation',
        ),
        migrations.DeleteModel(
            name='ObservationDirectionVent',
        ),
        migrations.DeleteModel(
            name='ObservationHumidite',
        ),
        migrations.DeleteModel(
            name='ObservationPluviometrique',
        ),
        migrations.DeleteModel(
            name='ObservationTemperature',
        ),
        migrations.DeleteModel(
            name='StationPluviometrique',
        ),
        migrations.DeleteModel(
            name='TypeStationPluviometrique',
        ),
    ]
