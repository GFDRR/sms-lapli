# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0003_stationobservers_actif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stationobservers',
            old_name='observer',
            new_name='personne',
        ),
        migrations.AlterUniqueTogether(
            name='stationobservers',
            unique_together=set([('station', 'personne')]),
        ),
    ]
