# -*- coding: latin-1 -*-

from datetime import timedelta, datetime

from django.http import *
from django.utils import formats
from django.db.models import Q
from django.db.models import Avg

from hydromet.models import Station, Observation, Limite
from django.shortcuts import render


# ObservationForm.fields['valider'].widget.attrs['readonly'] = True

def map_overview(request):
    dept_lst = request.POST.getlist('sel_dept[]')

    stations_list = []
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    for station in Station.objects.filter(Q(limite__pk__in=dept_lst)|Q(limite__isnull=True)):
        observation = Observation.objects.filter(station=station).order_by('-pk').first()
        if not observation:
            quantite_pluie = '-'
            statut = 'no_activity'
            date_update = ''
        else:
            quantite_pluie = observation.value
            statut = 'high_activity'
            date_update = datetime.combine(observation.time_result, datetime.min.time())

        if date_update and date_update >= today:
            statut = 'high_activity'
        elif date_update and date_update < today and date_update >= today - timedelta(days=7):
            statut = 'low_activity'
        elif date_update:
            statut = 'no_activity'

        if not station.actif:
            statut = 'off_activity'

        format_date = formats.date_format(date_update, "SHORT_DATE_FORMAT") if date_update else '--'

        # typeObs = TypeStationTypeObservation.objects.filter(typestation=station.typestation)

        # if typeObs:
        # for type in typeObs:
        # print(type.typeobservation.nom.encode('utf-8'))

        # unite = observation.typeobservation.unitemesure
        # if not unite:
        # unite = 'N/A'

        stations_list.append(
            {'nomStation': station.nom, 'latitude': station.latitude, 'longitude': station.longitude,
             'qt': quantite_pluie, 'statut': statut, 'dateUpdate': format_date, 'today': today})

    return JsonResponse({'stations_lst': stations_list})


def chart_overview(request):
    dept_lst = request.POST.getlist('sel_dept[]')
    sel_month = request.POST.get('sel_month');
    time_selected = datetime.strptime(sel_month, "%Y-%m-%d");

    dept_list = []

    for limite in Limite.objects.filter(typelimite__niveau=1, pk__in=dept_lst):
        value=Observation.objects.filter(typeobservation__nom__contains='précipitation', limite=limite, time_result__month=time_selected.month).aggregate(Avg('value', default=0))
        dept_list.append(
            {'nom': limite.nom, 'val': value['value__avg'] })

    return JsonResponse({'dept_lst': dept_list})


def rapport(request):

    return render(request, "hydromet/rapport.html", { })
