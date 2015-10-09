from django import forms
#from requests.packages.urllib3 import request
from base.forms import ValidationInput
from .models import *
from django.contrib.auth.models import User, Permission, Group

__author__ = 'esdras'


class StationForm(forms.ModelForm):
    class Meta:
        #Added the fields of Station manually for the validation test
        model = Station
        fields = ["latitude", "longitude", "hauteur", "uniteMesure", "idSiteSeninnelle", "nomStation", "typeStation", "idStation"]

    #Test input nomStation before validation
    def clean_nomStation(self):

        dataInput = self.cleaned_data.get('nomStation')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput, "True"):
            raise forms.ValidationError("Nom station incorrect!")

        return dataInput


class TypeStationForm(forms.ModelForm):
    class Meta:
        #Added the fields of TypeStation manually for the validation test
        model = TypeStation
        fields = ["typeStation", "description"]

    #Test input typeStation before validation
    def clean_typeStation(self):

        dataInput = self.cleaned_data.get('typeStation')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput, "True"):
            raise forms.ValidationError("Type station incorrect!")

        return dataInput

class ObservationForm(forms.ModelForm):

    #Test input Poste before validation
    # def clean_valider(self):
    #      dataInput = self.cleaned_data.get('valider')
    #      user = User.objects.all()
    #      current_user = request.user

    class Meta:
        #Added the fields of Observation manually for the validation test
        model = Observation
        fields = ["idStation", "observer", "dateDebut", "dateFin", "temperatureMax", "temperatureMin", "quantitePluie", "description", "valider"]


class UniteDeMesureForm(forms.ModelForm):
    class Meta:
        model = UniteDeMesure
        fields = ["uniteMesure", "formule", "description"]

class StationObserversForm(forms.ModelForm):
    class Meta:
        model = StationObservers
        fields = ["station", "observer"]
