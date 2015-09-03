# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_hydrometeologique', '0003_auto_20150903_1456'),
        ('Donnees_de_base', '0006_auto_20150903_1446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesentinelle',
            name='sectionCommunale',
        ),
        migrations.DeleteModel(
            name='SiteSentinelle',
        ),
    ]
