# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151112_0932'),
        ('hydromet', '0002_station_actif'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservateurHydromet',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('actif', models.BooleanField(default=True)),
                ('personne', models.OneToOneField(to='base.Personne')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='observateur',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='observateur',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='observateur',
            name='station',
        ),
        migrations.RemoveField(
            model_name='log',
            name='observateur',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='observateur',
        ),
        migrations.DeleteModel(
            name='Observateur',
        ),
        migrations.AddField(
            model_name='log',
            name='observateurhydromet',
            field=models.ForeignKey(to='hydromet.ObservateurHydromet', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='observation',
            name='observateurhydromet',
            field=models.ForeignKey(to='hydromet.ObservateurHydromet', blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='observateurhydromet',
            unique_together=set([('station', 'personne')]),
        ),
    ]
