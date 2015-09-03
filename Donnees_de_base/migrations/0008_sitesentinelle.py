# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Donnees_de_base', '0007_auto_20150903_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSentinelle',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('localite', models.CharField(max_length=45)),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('hauteur', models.DecimalField(decimal_places=2, max_digits=8, default=0)),
                ('sectionCommunale', models.ForeignKey(to='Donnees_de_base.SectionCommunale')),
            ],
        ),
    ]
