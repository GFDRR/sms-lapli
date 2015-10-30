# import os
# import os.path
# import sys
# from django.conf import settings
# sys.path.append("../")
# os.environ["DJANGO_SETTINGS_MODULE"] = "smslapli.settings"
# #django.setup()

from base.models import *
import csv

#ts = TypeStationPluviometrique.objects.all()[0]

# with open('scripts/depFakeDatas.csv', 'r+') as csvfile:
#     reader = csv.reader(csvfile)
#     va = 0
#     for row in reader:
#         va+=1
#         if va == 1:
#             continue
#         print(row[2])
#         #dep = Departement(departement=row[2], description="Le departement du/de : "+row[2], id_code=row[1])
#         #dep.scave()
#         dep = Departement()
#         dep.departement = row[2]
#         dep.description = row[2]+"Je pense donc je suis"
#         dep.id_code = row[1]
#         Departement.save(dep)

# with open('scripts/comFakeDatas.csv', 'r+') as csvfile:
#     reader = csv.reader(csvfile)
#     va = 0
#     for com in reader:
#         va+=1
#         if va == 1:
#             continue
#         departe = Departement.objects.get(id_code = com[3])
#         commun = com[2]
#         descc = "Cogito ergo sum"
#         id_code = com[1]
#         print(departe,commun,descc,id_code)
#         laCom = Commune()
#         laCom.departement=departe
#         laCom.description=descc
#         laCom.id_code=id_code
#         laCom.commune=commun
#         laCom.save()

with open('scripts/sctComFakeDatas2.csv', 'r+') as csvfile:
	reader = csv.reader(csvfile)
	va=0
	for sctCom in reader:
		va += 1
		if va == 1:
			continue 
		print(sctCom[4], sctCom[5], sctCom[3], sctCom[7])
		sct= SectionCommunale()
		sct.commune = Commune.objects.get(commune=sctCom[7])
		sct.sectionCommunale = sctCom[4]
		sct.nomOfficiel = sctCom[5]
		sct.description = "Une section communale dependant de la commune ::"+sctCom[7]
		sct.id_code = sctCom[2]
		sct.save()
unPost = Poste(nomPoste="Observateur",description="Assurer la lecture des pluviometres")
unPost.save()