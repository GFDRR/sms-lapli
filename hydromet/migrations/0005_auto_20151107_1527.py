# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_limite_code'),
        ('hydromet', '0004_auto_20151107_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observateur',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('actif', models.BooleanField(default=True)),
                ('personne', models.OneToOneField(to='base.Personne')),
                ('station', models.ForeignKey(to='hydromet.Station')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='stationobservers',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='stationobservers',
            name='personne',
        ),
        migrations.RemoveField(
            model_name='stationobservers',
            name='station',
        ),
        migrations.RemoveField(
            model_name='observation',
            name='observer',
        ),
        migrations.DeleteModel(
            name='StationObservers',
        ),
        migrations.AddField(
            model_name='observation',
            name='observateur',
            field=models.ForeignKey(to='hydromet.Observateur', null=True, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='observateur',
            unique_together=set([('station', 'personne')]),
        ),
    ]
