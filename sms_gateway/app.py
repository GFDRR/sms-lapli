from rapidsms.apps.base import AppBase
from base.models import *   # importing all models from Donnees_de_Base where data about Contacts are stored
from hydromet.models import *
from datetime import timedelta
from django.utils import timezone
from datetime import datetime, date
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
            obs_id = PersonneContact.objects.filter(telephonePersonnel = tel).first().id
            if msg.text == "data":
                data_of_the_day = ""
                a = Observation
                for i in a.objects.filter(dateFin = datetime.now()):
                    if i.observer.id == obs_id:
                        data_of_the_day += str(i.dateDebut) + " : " + str(i.quantitePluie) + " "
                msg.respond(data_of_the_day)
                return True
            elif msg.text == "data month":
                month = datetime.now().month
                year = datetime.now().year
                if month in [1,3,5,7,8,10,12]:
                    n_day = 31
                elif month in [4,6,9,11]:
                    n_day = 30
                elif month == 2:
                    if year % 4 == 0 or year % 400  == 0 and year % 100 != 0:
                        n_day = 29
                    else:
                        n_day = 28
                data = ""
                max = min = 0
                date_min = date_max = ""
                first_loop = True
                today = timezone.now().date()
                MonthBeforeToday = timezone.now().date() - timedelta(days = n_day)
                dataOfTheLastMonth = Observation.objects.filter(dateDebut__gt = MonthBeforeToday, dateDebut__lt = today)
                for i in dataOfTheLastMonth:
                    if i.observer.id == obs_id:
                        if first_loop:
                            max = min = i.quantitePluie
                            first_loop = False
                        if i.quantitePluie < min:
                            min = i.quantitePluie
                            date_min = i.dateDebut
                        if i.quantitePluie > max:
                            max = i.quantitePluie
                            date_max = i.dateDebut
                msg.respond("MAX : " + str(date_max) + " -> " + str(max) + " / " + "MIN : " + str(date_min) + " -> " + str(min))
                return True
            elif msg.text == "data week":
                today = timezone.now().date()
                sevenDayBeforeToday = timezone.now().date() - timedelta(days=7)
                dataOfTheSevenLastDays = Observation.objects.filter(dateDebut__gt = sevenDayBeforeToday, dateDebut__lt = today)
                data = ""
                for i in dataOfTheSevenLastDays:
                    if i.observer.id == obs_id:
                        data += str(i.dateDebut) + " : " + str(i.quantitePluie) + " "
                msg.respond(data)
                return True
            else:
                pat_zero = '0'
                matched = re.match(pat_zero, msg.text)
                if isFloat(msg.text):
                    if matched:
                        msg.respond("Vous avez un nombre commencant par 0. Il n'y avait pas de pluie?")
                        return True

                    val_float = float(msg.text)

                    person = PersonneContact.objects.get(telephonePersonnel=tel)
                    station = StationObservers.objects.get(observer=person).station
                    

                    recup_last_value = Observation.objects.filter(observer = obs_id, dateDebut = timezone.now().date() - timedelta(days=1)).order_by('-id').first()
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
                        o.dateDebut = timezone.now().date() - timedelta(days=1)
                        o.dateFin = timezone.now().date()
                        o.valider = False
                        o.save()
                        info = 'Donnee sauvegardee. Merci!'

                    msg.respond(info)
                    return True
                else:
                    msg.respond("Verifier la valeur envoye SVP! On attend un nombre Ex: 12.9 ou 12")
                    return True

        return False
