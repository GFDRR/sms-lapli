from base.models import PersonneContact
from hydromet.models import Observation

__author__ = 'alexing'

from django import template

register = template.Library()

@register.filter
def notification(texte):
    nmbAgent = PersonneContact.objects.filter(isactif=False).count();
    msgNotValidate = Observation.objects.filter(valider = False).count()
    listQueryDash = {"nbAgent":str(nmbAgent), "msgNotValidate":str(msgNotValidate)}
    result = listQueryDash[texte]
    return result

