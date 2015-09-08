__author__ = 'esdras'

from django import forms
from .models import *


#Here test all input for string and security card (cin, nif).
class ValidationInput:

    #test if string valid
    def isValidInput(self, value):
        if value.isdigit():
            return False

        else:
            charSpeciaux = [ord(' '), ord('-'), ord("'")]
            value = value.upper()

            for i in range(0, len(value)-1):
                if ord(value[i]) < ord('A') and ord(value[i]) not in charSpeciaux or ord(value[i])>ord('Z'):
                    return False
            return True

    #test if the id of security card is valid
    def isvalidIdPersonne(self, value, forme):

        if value.count("-") != forme.count("-") or len(value) != len(forme):
            return False
        else:
            for i in range(0, len(value)-1):
                if value[i] == "-":
                    if value[i] != forme[i]:
                        return False
                else:
                    if not self.isInt(value[i]):
                        return False
                return True

    #private method for testing if int
    def isInt(self, char):
        try:
            int(char)
            return True
        except ValueError:
            return False

class DepartementForm(forms.ModelForm):
    class Meta:
        #Added the fields of Departement manually for the validation test
        model = Departement
        fields = ["departement", "description"]

    #Test input departement before validation
    def clean_departement(self):

        dataInput = self.cleaned_data.get('departement')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Departement invalid!")

        return dataInput



class CommuneForm(forms.ModelForm):
    class Meta:
        #Added the fields of Commune manually for the validation test
        model = Commune
        fields = ["departement", "commune", "description"]

    #Test input Commune before validation
    def clean_commune(self):
        dataInput = self.cleaned_data.get('commune')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Commune invalid!")

        return dataInput


class SectionCommunaleForm(forms.ModelForm):
    class Meta:
        #Added the fields of SectionCommunale manually for the validation test
        model = SectionCommunale
        fields = ["commune", "sectionCommunale", "description"]

    #Test input SectionCommunale before validation
    def clean_sectionCommunale(self):
        dataInput = self.cleaned_data.get('sectionCommunale')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Section communale invalide!")

        return dataInput


class SiteSentinelleForm(forms.ModelForm):
    class Meta:
        #Added the fields of SiteSentinelle manually for the validation test
        model = SiteSentinelle
        fields = ["sectionCommunale", "localite", "latitude", "longitude", "hauteur"]

    #Test input SiteSentinelle before validation
    def clean_localite(self):
        dataInput = self.cleaned_data.get('localite')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Localite incorrect!")

        return dataInput


class PosteForm(forms.ModelForm):
    class Meta:
        #Added the fields of Poste manually for the validation test
        model = Poste
        fields = ["nomPoste", "description"]

    #Test input Poste before validation
    def clean_nomPoste(self):
        dataInput = self.cleaned_data.get('nomPoste')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Nom de Poste incorrect!")

        return dataInput





class PersonneContactForm(forms.ModelForm):
    class Meta:
        #Added the fields of PersonneContact manually for the validation test
        model = PersonneContact
        fields = ["nomPoste", "nomPersonne", "prenomPersonne", "telephoneBureau", "telephonePersonnel", "emailPersonnel", "adressePersonnelle", "nif", "cin", "dateEmbauche"]

    #Test input nomPersonne before validation
    def clean_nomPersonne(self):
        dataInput = self.cleaned_data.get('nomPersonne')
        valid = ValidationInput()

        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Nom incorrect!")

        return dataInput

    #Test input prenomPersonne before validation
    def clean_prenomPersonne(self):
        dataInput = self.cleaned_data.get('prenomPersonne')
        valid = ValidationInput()
        if not valid.isValidInput(dataInput):
            raise forms.ValidationError("Prenom incorrect!")

        return dataInput
    # #Test input telephoneBureau before validation and say if number exist
    # def clean_telephoneBureau(self):

    #     telephoneBureau = self.cleaned_data.get('telephoneBureau')

    #     if PersonneContact.objects.filter(telephoneBureau = telephoneBureau).exists():
    #         raise forms.ValidationError("Ce numero existe!")

    #     return telephoneBureau

    # #Test input telephonePersonnel before validation and say if number exist
    # def clean_telephonePersonnel(self):

    #     telephonePersonnel = self.cleaned_data.get('telephonePersonnel')

    #     if PersonneContact.objects.filter(telephonePersonnel = telephonePersonnel).exists():
    #         raise forms.ValidationError("Ce numero existe!")

    #     return telephonePersonnel

    #Test input cin before validation
    def clean_cin(self):
        cin = self.cleaned_data.get('cin')
        valid = ValidationInput()
        if cin:
            if not valid.isvalidIdPersonne(cin, "XX-XX-XX-XXXX-XX-XXXXX"):
                raise forms.ValidationError("Format cin incorrect ou il y a erreur saisie. format:(XX-XX-XX-XXXX-XX-XXXXX)")

        return cin

    #Test input nif before validation
    def clean_nif(self):
        nif = self.cleaned_data.get('nif')
        valid = ValidationInput()
        if nif:
            if not valid.isvalidIdPersonne(nif, "XXX-XXX-XXX-X"):
                raise forms.ValidationError("Format nif incorrect ou il y a erreur saisie. format:(XXX-XXX-XXX-X)")

        return nif

    # #Test if person already exist in the db.
    # def clean(self):
    #     nom = self.cleaned_data.get('nomPersonne')
    #     prenom = self.cleaned_data.get('prenomPersonne')

    #     if PersonneContact.objects.filter(nomPersonne = nom).exists() and PersonneContact.objects.filter(prenomPersonne = prenom).exists():
    #         raise forms.ValidationError("Cette personne existe deja!")