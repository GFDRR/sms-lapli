from django.shortcuts import render
from django.http import *
from base.models import Limite
from django.template import Context
from hydromet.models import Observation
from django.template.loader import get_template
#from xhtml2pdf import pisa

# Create your views here.

def home(request):
    return render(request, "public/index.html", {'menu_active':'accueil'})

def faq(request):
    return render(request, "public/faq.html", {'menu_active':'faq'})

def pluviometrie(request):
    departement_lst = Limite.objects.filter(typelimite__nom='Département');
    return render(request, "public/pluviometrie.html", {'menu_active':'pluviometrie','dep_lst': departement_lst})

def imp(request):
    recupAll = Observation.objects.select_related('idStation')
    dd = []
    for e in recupAll:
        dd.append(e)
    return render(request, "public/test.html", {'val': dd})





