from django.shortcuts import render
from django.http import *
from Donnees_de_base.models import *
from Donnees_hydrometeologique.models import *

# Create your views here.


def rpluie(request):
    return render(request, "public/temp_rapport.html", {})


def acc(request):
    return render(request, "public/accueil_rapport.html", {})


def json_rap(request):

    return JsonResponse({'ti': 'moi'})