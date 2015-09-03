from rapidsms.apps.base import AppBase
from Donnees_de_base.models import *   # importing all models from Donnees_de_Base where data about Contacts are stored
from Donnees_hydrometeologique.models import *
from datetime import datetime
import re


def isFloat(val):
        try:
            float(val)
            return True
        except:
            return False
class SmsGateway(AppBase):

    def handle(self,msg):
        valid_numbers = [] # An empty list

        for tel in PersonneContact.objects.all():
            valid_numbers.append(tel.telephonePersonnel)# Getting all personnal Phone

        if '50937612070' not in valid_numbers:
            #msg.respond('TEst')
            return False #Return false because we don't want to answer an unknow number
                         #We must shut the default messge from the default app in this case
        else: #If this number is in the list, will work with the text message
            if isFloat(msg.text):
                val_float = float(msg.text)
                #Ici operation avec les unites disponibles
                dt = datetime.now()
                date = str(dt.year)+'-'+str(dt.month)+'-'+str(dt.day) # now date

                #getting the Personne's id
                pers_id = 0
                for pers in PersonneContact.objects.filter(telephonePersonnel=msg.peer):
                    pers_id = pers.id

                #getting the StationPluviometrique's id
                stat_id = 0
                for station in StationPluviometrique.objects.all():
                    if pers_id == station.cfPersCnt.id:
                        stat_id = station
                #Will Save here
                obsv= ObservationPluviometrique(quantite=val_float,dateDebut=date,dateFin=date,description="Un texte comme ca",idStation=stat_id,numeroJour=23,valider=0)
                obsv.save()

                msg.respond('Donnees sauvegardees! Merci!'+str(dt.year)+' '+str(pers_id))
                return True
            else:
                msg.respond('Bad Entry')
                return True


        return False