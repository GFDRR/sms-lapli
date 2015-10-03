# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydromet', '0001_initial'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personnecontact',
            name='cfAtachStation',
            field=models.ForeignKey(verbose_name='Affectation Station', to='hydromet.StationPluviometrique'),
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='nomPoste',
            field=models.ForeignKey(verbose_name='Poste', to='base.Poste'),
        ),
        migrations.AddField(
            model_name='commune',
            name='departement',
            field=models.ForeignKey(verbose_name='Departement', to='base.Departement'),
        ),
    ]
