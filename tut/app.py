__author__ = 'esdras'

from rapidsms.apps.base import AppBase


def isfloat(value):
      try:
        float(value)
        return True
      except ValueError:
        return False


process_en_cours = False

class Inbox(AppBase):

    def handle(self, msg):

        global process_en_cours

        #step 1. reception de message.

        if isfloat(msg.text) and float(msg.text)>1.0 and process_en_cours == False:
            process_en_cours = True
            msg.respond('Voulez-vous envoyez '+msg.text+' a la CNSA? si oui envoyer 1 sinon envoyer 0.') #if save
            return True

        elif process_en_cours == True: #on verifie si un processus est en cours de validation

            #step 2. validation, annulation et enregistrement a la base.

            if msg.text == '1':
                #save in base
                #           #
                #############
                msg.respond('Message recu!!') #if save
                process_en_cours = False
                return True

            elif msg.text == '0':
                process_en_cours = False
                msg.respond('Votre message viens d\'etre annuler')
                return True


        elif msg.text == 'aide':
            msg.respond('Tapez le niveau d\'eau puis envoyer vers +509********')
            return True














