from base.models import Departement, Commune, SectionCommunale
import shapefile

import django
django.setup()


def load_departements():
    sf = shapefile.Reader('/Users/ortelius/projects/gfdrr-dev/haiti/admin/hti_boundaries_departements_adm1_cnigs_polygon.shp')
    print sf.fields
    records = sf.records()

    for i in range(0, len(records)): 
        print records[i][1]
        d = Departement()
        d.departement = records[i][1]
        d.id_code = records[i][0]
        d.save()

def load_communes():
    sf = shapefile.Reader('/Users/ortelius/projects/gfdrr-dev/haiti/admin/hti_boundaries_communes_adm2_cnigs_polygon.shp')
    #print sf.fields
    records = sf.records()

    for i in range(0, len(records)):
        d = Departement.objects.get(id_code=records[i][2])
        c = Commune()
        c.commune = records[i][1]
        c.departement = d
        c.id_code=records[i][0]
        c.save()

def load_sections_communales():
    sf = shapefile.Reader('/Users/ortelius/projects/gfdrr-dev/haiti/admin/hti_boundaries_sections_communales_adm3_cnigs_polygon.shp')
    print sf.fields
    records = sf.records()

    for i in range(0, len(records)):
        print records[i][3], records[i][6]
        c = Commune.objects.get(id_code=str(int(records[i][5])))
        sc = SectionCommunale() 
        sc.id_code=records[i][0]
        sc.sectionCommunale = records[i][3]
        sc.nomOfficiel = records[i][4]
        sc.commune = c
        sc.save()

#load_departements()
#load_communes()
load_sections_communales()
