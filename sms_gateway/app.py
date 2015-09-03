from rapidsms.apps.base import AppBase
from Donnees_de_base.models import *   # importing all models from Donnees_de_Base where data about Contacts are stored
import datetime
import re

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
            if msg.text.isdigit():
                    val_float = float(msg.text)
                    #Ici operation avec les unites disponibles
                    dt = datetime.datetime.now()
                    date = dt.day+'/'+dt.month+'/'dt.year # now date

                    #getting the Personne's id
                    pers_id = 0
                    for pers in PersonneContact.objects.filter(telephonePersonnel=msg.peer):
                        pers_id = pers.id

                    #getting the StationPluviometrique's id
                    stat_id = 0
                    for station in StationPluviometrique.objects.all():
                        if pers_id == station.cfPersCnt.id:
                            stat_id = station.cfPersCnt.id

                    #Will Save here
                    obsv= ObservationPluviometrique(quantite=val_float,dateDebut=date,dateFin=date,description="Un texte comme ca",idStation=stat_id,numeroJour=23,valider=0)
                    obsv.save()
                    #station = StationPluviometrique(latitude,longitude,hauteur,idSiteSeninnelle,nomStation,typeStation,cfPersCnt)
                    msg.respond('digit')
                    return True
            elif msg.text.isalnum():
                msg.respond("Bad Entry")
                return True
            else:
                if re.match('[-+]?[0-9]*[.]?[0-9]*',msg.text) is not None:  #See if we can always use the text received as a float number
                    msg.respond(msg.text)
                    #Will Save here
                    return True
                else:
                    msg.respond("Bad Entry")
                    return True

            return True


        return True