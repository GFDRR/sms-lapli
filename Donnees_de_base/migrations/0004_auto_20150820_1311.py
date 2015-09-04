# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0003_auto_20150819_1215'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnecontact',
            name='sectionCommunale',
        ),
        migrations.DeleteModel(
            name='PersonneContact',
        ),
    ]
