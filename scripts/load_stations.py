from hydromet.models import StationPluviometrique, TypeStationPluviometrique
import csv

ts = TypeStationPluviometrique.objects.all()[0]

with open('stations.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        coords = row[2].split(',')
        print row[0], row[1], coords[0], coords[1]
        s = StationPluviometrique()
        s.longitude = float(coords[0])
        s.latitude = float(coords[1])
        s.nomStation = row[0]
        s.typeStation = ts
        s.save()
