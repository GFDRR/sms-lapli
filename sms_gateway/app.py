from rapidsms.apps.base import AppBase
from base.models import *   # importing all models from Donnees_de_Base where data about Contacts are stored
from hydromet.models import *
from datetime import *
import re


def isFloat(val):
        try:
            float(val)
            return True
        except:
            return False


class SmsGateway(AppBase):

    def handle(self,msg):
        valid_numbers = []  # An empty list

        for tel in PersonneContact.objects.all():
            valid_numbers.append(tel.telephonePersonnel)# Getting all personnal Phone

        tel = msg.peer.strip("+")
        if tel not in valid_numbers:
            # msg.respond('TEst')
            msg.respond('Not in  '+msg.peer)
            return True  # Return false because we don't want to answer an unknow number
                         # We must shut the default messge from the default app in this case
        else: # If this number is in the list, will work with the text message
            if msg.text == "daa":
                data_of_the_day = ""
                a = Observation
                for i in a.objects.filter(dateFin = datetime.now()):
                    data_of_the_day += str(i.quantitePluie) + ", "
                msg.respond(data_of_the_day)
                return True
            elif msg.text == "daam":
                max = ""
                min = ""
                msg.respond("bla bla bla")
                return True
            elif msg.text == "daaw":
                prime = sec = third = forth = fifth = sixth = seventh = ""
                msg.respond("week")
                return True
            else:
                pat_zero = '0'
                matched = re.match(pat_zero, msg.text)
                if isFloat(msg.text):
                    if matched:
                        msg.respond("Vous avez un nombre commencant par 0. Il n'y avait pas de pluie?")
                        return True

                    val_float = float(msg.text)
                    #Ici operation avec les unites disponibles
                    dt = datetime.now()
                    dateFin = str(dt.year)+'-'+str(dt.month)+'-'+str(dt.day)
                    dtD=date.today() - timedelta(days=1)
                    dateDebut = str(dtD.year)+'-'+str(dtD.month)+'-'+str(dtD.day)

                    person = PersonneContact.objects.get(telephonePersonnel=tel)
                    station = StationObservers.objects.get(observer=person).station

                    #id de la personne qui a envoye le sms
                    obs_id = PersonneContact.objects.filter(telephonePersonnel = tel).first().id

                    recup_last_value = Observation.objects.filter(observer = obs_id, dateDebut = dateDebut).order_by('-id').first()
                    if recup_last_value:
                        recup_last_value.quantitePluie = val_float
                        recup_last_value.save()
                        info = 'Donnee mise a jour'
                    else:
                        o = Observation()
                        o.idStation = station
                        o.observer = person
                        o.timestamp = datetime.now()
                        o.quantitePluie = val_float
                        o.dateDebut = dateDebut
                        o.dateFin = dateFin
                        o.valider = False
                        o.save()
                        info = 'Donnee sauvegardee. Merci!'

                    msg.respond(info)
                    return True
                else:
                    msg.respond("Verifier la valeur envoye SVP! On attend un nombre Ex: 12.9 ou 12")
                    return True

        return False
