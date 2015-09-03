from django import forms
from Donnees_de_base.forms import ValidationInput
from .models import *

__author__ = 'esdras'


class StationPluviometriqueForm(forms.ModelForm):
    class Meta:
        #Added the fields of StationPluviometrique manually for the validation test
        model = StationPluviometrique
        fields = ["latitude", "longitude", "hauteur", "idSiteSeninnelle", "nomStation", "typeStation"]

    #Test input nomStation before validation
    def clean_nomStation(self):

        dataInput = self.cleaned_data.get('nomStation')
        valid = ValidationInput

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Nom station incorrect!")

        return dataInput


class TypeStationPluviometriqueForm(forms.ModelForm):
    class Meta:
        #Added the fields of TypeStationPluviometrique manually for the validation test
        model = TypeStationPluviometrique
        fields = ["typeStation", "description"]

    #Test input typeStation before validation
    def clean_typeStation(self):

        dataInput = self.cleaned_data.get('typeStation')
        valid = ValidationInput

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Type station incorrect!")

        return dataInput

class ObservationPluviometriqueForm(forms.ModelForm):
    class Meta:
        #Added the fields of ObservationPluviometrique manually for the validation test
        model = ObservationPluviometrique
        fields = ["quantite", "dateDebut", "dateFin", "description", "idStation", "numeroJour", "valider"]