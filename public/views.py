from django.shortcuts import render
from django.http import *
from base.models import *
from hydromet.models import *
from datetime import timedelta, datetime
from django.utils import formats

# Create your views here.


def rpluie(request):
    departement_lst = Departement.objects.all();
    return render(request, "public/rapports.html", {'dep_lst': departement_lst})


def acc(request):
    return render(request, "public/accueil_rapport.html", {})


def json_average_by_dep(request):
    obsv = Observation.objects.select_related('idStation')  # getting all Observation entries in all relationship
    foundDep = {}  # list of all found Commune
    numberFound = {}   # occurence of a commune
    sumOfRead = {}   # store the sum of rain's quantity
    dep = {}
    for qtt in obsv:
        dept = qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement
        #print(dept.departement)
        if dept.pk in foundDep:  # getting the name of the Departement
            # ids = foundDep.index(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement)
            numberFound[dept.pk] += 1  # increment the number of occurence of commune
            sumOfRead[dept.pk] += float(qtt.quantitePluie)
        else:
            # foundDep.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement)
            dept = qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement
            foundDep[dept.pk] = dept.departement
            numberFound[dept.pk] = 1
            sumOfRead[dept.pk] = float(qtt.quantitePluie)
            # dep.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement)

    overAll = []
    #for key, index in enumerate(foundDep):
    for (key, value) in foundDep.items():
        overAll.append({'dep': foundDep[key],
                        'moy': (sumOfRead[key] / numberFound[key])})  # lack of precision in the date
    reponseJson = {'table': overAll}
    # hh = {'id': 1, 'personne': [{'nom': 'Alexis', 'prenom': 'Rulx Philome'}, {'nom': 'Philers beme', 'prenom': 'Chana'}]}
    # hh = {'f': foundCommune , 'nbr' : numberFound , 'sum' : sumOfRead, 'dep' : dep}
    return JsonResponse(reponseJson)


def compBDep(request):
    import datetime
    days = [] #Getting the dates of the week
    date = datetime.date.today()
    #date = datetime.datetime.strptime("2015-01-27", "%Y-%m-%d").date()
    start_week = date - datetime.timedelta(date.weekday())
    for i in range(7):
        days.append(str(start_week + datetime.timedelta(i)))

    def avr_calc(dep, jours):
        avr = []
        obsv = Observation.objects.select_related('idStation').filter(dateDebut__range=[start_week, jours[6]]).order_by('dateDebut')
        for cal in jours:
            qtObsv = 0
            sumObsv = 0
            for lect in obsv:
                if lect.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement == dep and str(lect.dateDebut) == cal:
                    qtObsv += 1
                    sumObsv += float(lect.quantitePluie)
            if qtObsv == 0:
                avr.append(0.0)
            else:
                avr.append((sumObsv/qtObsv))
        print(avr)
        return avr
    rsltF = []
    deps = Departement.objects.all()
    for dep in deps:
        rsltF.append({'nomDep': dep.departement, 'moyDep': avr_calc(dep.departement, days)})
    return JsonResponse({'jr': days, 'table':rsltF})


def json_rap(request):
    """
        Recuperation des donnes et
        Encodage en JSON
    """
    obsv = Observation.objects.select_related('idStation')  # getting all Observation entries in all relationship
    foundCommune = []  # list of all found Commune
    numberFound = []  # occurence of a commune
    sumOfRead = []  # store the sum of rain's quantity
    dep = []
    datex = []
    for qtt in obsv:
        if qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune in foundCommune:  # getting the name of the communes
            ids = foundCommune.index(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune)
            numberFound[ids] = numberFound[ids] + 1  # increment the number of occurence of commune
            sumOfRead[ids] = sumOfRead[ids] + float(float(qtt.quantitePluie))
            datex.append(qtt.dateDebut)
        else:
            foundCommune.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune)
            numberFound.append(1)
            sumOfRead.append(float(qtt.quantitePluie))
            dep.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement)
            datex.append(qtt.dateDebut)

    overAll = []
    for index in range(len(foundCommune)):
        overAll.append({'dep': dep[index], 'com': foundCommune[index], 'date': datex[index], 'nbr': numberFound[index],
                        'moy': (sumOfRead[index] / numberFound[index])})  # lack of precision in the date
    reponseJson = {'table': overAll}
    # hh = {'id': 1, 'personne': [{'nom': 'Alexis', 'prenom': 'Rulx Philome'}, {'nom': 'Philers beme', 'prenom': 'Chana'}]}
    # hh = {'f': foundCommune , 'nbr' : numberFound , 'sum' : sumOfRead, 'dep' : dep}
    return JsonResponse(reponseJson)


def imp(request):
    recupAll = Observation.objects.select_related('idStation')
    dd = []
    for e in recupAll:
        dd.append(e)
    return render(request, "public/test.html", {'val': dd})


def json_graph(request):
    datas = Observation.objects.all()
    tous = []
    for info in datas:
        tous.append({'dates': info.dateDebut, 'qtt': info.quantitePluie})

    responsJson = {'table': tous}
    return JsonResponse(responsJson)


def station_map(request):
    departement_lst = Departement.objects.all();
    return render(request, "public/map_stations.html", {'departement_lst': departement_lst})


def json_map(request):
    stations_list = []
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    for station in Station.objects.all():
        observation = Observation.objects.filter(idStation=station.id).order_by('-pk').first()
        if not observation:
            quantite_pluie = '-'
            statut = 'off_activity'
            date_update = ''
        else:
            quantite_pluie = observation.quantitePluie
            statut = 'high_activity'
            date_update = datetime.combine(observation.dateFin, datetime.min.time())

        if date_update and date_update >= today:
            statut = 'high_activity'
        elif date_update and date_update < today and date_update >= today-timedelta(days=7):
            statut = 'low_activity'
        elif date_update:
            statut = 'no_activity'

        format_date = formats.date_format(date_update, "SHORT_DATE_FORMAT") if date_update else '--'

        stations_list.append(
            {'nomStation': station.nomStation, 'latitude': station.latitude, 'longitude': station.longitude,
             'qt': quantite_pluie, 'statut': statut, 'dateUpdate' : format_date, 'today': today})

    return JsonResponse({'stations_lst': stations_list})
    # return HttpResponse(stations)
