from base.models import PersonneContact
from hydromet.models import Observation
from datetime import *

__author__ = 'esdras'

from django import template

register = template.Library()

@register.filter
def notification(texte):
    nmbAgent = PersonneContact.objects.filter(isactif=False).count();
    msgNotValidate = Observation.objects.filter(valider = False).count()

    dt = datetime.now()
    dateFin = str(dt.year)+'-'+str(dt.month)+'-'+str(dt.day)
    dtD=date.today() - timedelta(days=1)
    dateDebut = str(dtD.year)+'-'+str(dtD.month)+'-'+str(dtD.day)
    
    personNotSentMsg = PersonneContact.objects.all().count()-Observation.objects.filter(dateDebut=dateDebut, dateFin=dateFin).values('observer').distinct().count()
    
    listQueryDash = {"nbAgent":str(nmbAgent), "msgNotValidate":str(msgNotValidate), "personNotSentMsg":str(personNotSentMsg)}
    result = listQueryDash[texte]
    
    return result

