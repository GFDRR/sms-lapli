# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0008_sitesentinelle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personnecontact',
            name='nomPoste',
        ),
        migrations.DeleteModel(
            name='PersonneContact',
        ),
    ]
