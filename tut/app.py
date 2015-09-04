from rapidsms.apps.base import AppBase
from Donnees_de_base.models import PersonneContact
from Donnees_hydrometeologique.models import ObservationPluviometrique, TypeStationPluviometrique


class PingPong(AppBase):
    def handle(self, msg):
        if msg.text == 'infos':
            msg.respond('Vous pouvez envoyer des donnees pluviometriques dans cette format (Identifiant: description)')
            return True
        else:
            a = ""
            descript = ""
            g = 0

            for i in range(0, len(msg.text)):

                if msg.text[i] ==':':
                   g = 1

                if g == 0:
                    a += msg.text[i]

                else:
                    descript += msg.text[i]

            identifiant = a.split(" ")
           # if msg.text == 'Esdras SUY: je suis la':
            for personne in PersonneContact.objects.all():
                if personne.nomPersonne == identifiant[0] and personne.prenomPersonne == identifiant[1]:
                    type = TypeStationPluviometrique(typeStation = "Station2", description = descript)
                    type.save()
            msg.respond(identifiant[0]+"yes"+identifiant[1])
            return True

        return False

        # class Sms(AppBase):
        #     def option(self, msg):
        #         if msg.text == '123':
        #             msg.respond('Identifiez vous: ')
        #             if msg.text == 'Esdras':
        #                 msg.respond('Ok')
