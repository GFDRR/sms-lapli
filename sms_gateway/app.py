from rapidsms.apps.base import AppBase
from base.models import *  # importing all models from Donnees_de_Base where data about Contacts are stored
from hydromet.models import *
from django.db.models import Avg, Min, Max
from datetime import timedelta
from django.utils import timezone, formats
from datetime import datetime, date

import re


def isFloat(val):
    try:
        float(val)
        return True
    except:
        return False


def subtract_one_month(dt0):
    dt1 = dt0.replace(days=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(days=1)
    return dt3


class SmsGateway(AppBase):
    def handle(self, msg):

        tel = msg.peer.strip("+")
        today = datetime.now()

        observer = Observateur.objects.filter(actif=True, personne__telephone_bureau=tel, personne__actif=True).first()

        if not observer:
            return True  # Return false because we don't want to answer an unknow number

        else:  # If this number is in the list, will work with the text message
            obs_id = observer.pk
            if msg.text == "data":
                data_of_the_day = ""
                observations = Observation.objects.filter(time_result__day=today.day, observateur=observer).first()

                if observations:
                    data_of_the_day += str(formats.date_format(observations.time_result, "SHORT_DATETIME_FORMAT")) + " : " + str(observations.value) + " "
                else:
                    data_of_the_day = "Vous n'avez pas encore envoyé de données aujourd'hui."

                msg.respond(data_of_the_day)
                return True
            elif msg.text == "data month":
                month_before = today - timedelta(days=30) #subtract_one_month(today)
                observations = Observation.objects.filter(time_result__gte=month_before, time_result__lte=today).aggregate(Avg('value'), Max('value'), Min('value'))
                if observations:
                    #msg.respond("MAX : " + str(observations.value__max) + " / " + "MIN : " + str(observations.value__min))
                    msg.respond("Rapport pour les 30 derniers jours\nMAX : "+ str(observations['value__max']) + " | MIN : " + str(observations['value__min']) + " | MAX : "+ str(observations['value__avg']))
                else:
                    msg.respond("Vous n'avez pas encore envoyé de données aujourd'hui.")
                return True
            elif msg.text == "data week":
                sevenDayBeforeToday = today.date() - timedelta(days=7)
                dataOfTheSevenLastDays = Observation.objects.filter(time_result__gt=sevenDayBeforeToday,
                                                                    time_result__lt=today, observer=observer)
                data = ""
                for i in dataOfTheSevenLastDays:
                    data += str(i.time_result) + " : " + str(i.value) + " "
                msg.respond(data)
                return True
            else:
                pat_zero = '0'
                matched = re.match(pat_zero, msg.text)
                if isFloat(msg.text):
                    if matched:
                        msg.respond("Vous avez un nombre commencant par 0. Il n'y avait pas de pluie ?")
                        return True

                    # person = Personne.objects.get(telephonePersonnel=tel)
                    station = observer.station
                    # id_station = station.id
                    # formule = station.uniteMesure.formule
                    # formule = UniteDeMesure.objects.get(id = id_station).formule

                    val_float = float(msg.text)  # * float(formule)

                    log = Log()

                    last_value = Observation.objects.filter(observateur=observer, time_result__day=today.day).order_by(
                        '-id').first()

                    if last_value:
                        last_value.quantitePluie = val_float
                        last_value.save()
                        info = 'Vous avez envoyé : ' + str(val_float) + '. Donnée mise à jour'
                        # logSave(log, recup_last_value, person, val_float)
                    else:
                        o = Observation()
                        o.station = station
                        o.observateur = observer
                        o.time_start = timezone.now().date() - timedelta(days=1)
                        o.time_end = today
                        o.time_result = today
                        o.value = val_float
                        o.valider = False
                        o.save()
                        info = 'Vous avez envoyé : ' + str(val_float) + '. Donnée sauvegardée. Merci!'
                        # logSave(log, recup_last_value, person, val_float)

                    log.observation = last_value
                    log.observateur = observer
                    log.value = val_float
                    log.time_start = timezone.now().date() - timedelta(days=1)
                    log.time_end = today
                    log.time_result = today
                    log.save()
                    msg.respond(info)
                    return True
                else:
                    msg.respond("Verifier la valeur envoyé SVP! On attend un nombre Ex: 12.9 ou 12")
                    return True

        return False

