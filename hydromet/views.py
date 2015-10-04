from django.shortcuts import render

# Create your views here.
from hydromet.forms import ObservationForm

ObservationForm.fields['valider'].widget.attrs['readonly'] = True