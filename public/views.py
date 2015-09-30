from django.shortcuts import render
from django.http import *
from Donnees_de_base.models import *
from Donnees_hydrometeologique.models import *
import json

# Create your views here.


def rpluie(request):
    return render(request, "public/temp_rapport.html", {})


def acc(request):
    return render(request, "public/accueil_rapport.html", {})


def json_rap(request):
    """
        Recuperation des donnes et
        Encodage en JSON
    """
    obsv = ObservationPluviometrique.objects.select_related('idStation') # getting all Observation entries in all relationship
    foundCommune = [] #list of all found Commune
    numberFound = [] # occurence of a commune
    sumOfRead = [] # store the sum of rain's quantity
    dep = []
    datex = []
    for qtt in obsv:
        if qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune in foundCommune: #getting the name of the communes
            ids = foundCommune.index(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune)
            numberFound[ids] = numberFound[ids]+1 # increment the number of occurence of commune
            sumOfRead[ids] = sumOfRead[ids] + float(float(qtt.quantite))
            datex.append(qtt.dateDebut)
        else:
            foundCommune.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.commune)
            numberFound.append(1)
            sumOfRead.append(float(qtt.quantite))
            dep.append(qtt.idStation.idSiteSeninnelle.sectionCommunale.commune.departement.departement)
            datex.append(qtt.dateDebut)

    overAll=[]
    for index in range(len(foundCommune)):
        overAll.append({'dep':dep[index], 'com': foundCommune[index], 'date': datex[index], 'moy': (sumOfRead[index]/numberFound[index])})#lack of precision in the date
    reponseJson = {'table': overAll}
    #hh = {'id': 1, 'personne': [{'nom': 'Alexis', 'prenom': 'Rulx Philome'}, {'nom': 'Philers beme', 'prenom': 'Chana'}]}
    #hh = {'f': foundCommune , 'nbr' : numberFound , 'sum' : sumOfRead, 'dep' : dep}
    return JsonResponse(reponseJson)


def imp(request):
    recupAll = ObservationPluviometrique.objects.select_related('idStation')
    dd = []
    for e in recupAll:
        dd.append(e)
    return render(request, "public/test.html", {'val':dd})