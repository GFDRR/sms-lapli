# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0007_auto_20151107_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='typeobservation',
            field=models.ForeignKey(to='hydromet.TypeObservation', verbose_name="Type de l'Observation", blank=True, null=True),
        ),
    ]
