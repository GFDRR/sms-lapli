.. _technical:

=======================
Technical Specification
=======================

Project Architecture
--------------------

* Django
* PostgreSQL + PostGIS
* RapidSMS
* Kannel
* istSOS
* Mobile Weather Station
* Web Front End 
* MapServer/GeoServer
* Deployment
* Backup and Recovery

Django
------

Project Structure
+++++++++++++++++

Settings
++++++++

Modules
+++++++

base
____

models
,,,,,,

hydromet
________

models
,,,,,,

views
,,,,,


PostgreSQL + PostGIS
--------------------

RapidSMS
--------

Kannel
------

istSOS
------

Mobile Weather Station
----------------------

Instruments
+++++++++++

Rain Gauge
__________

Wind Speed
__________

Wind Direction
______________

Sensors
+++++++

Temperature
___________

Humidity
________

Pressure
________

Luminosity
__________

Arduino
+++++++

Weather Shield
______________

Network Shield
______________

Software
++++++++

Web Front End
-------------

Leaflet
+++++++

MapServer/GeoServer
-------------------

Used to generate rainfall isoline chart etc

Deployment
----------

Ansible

Backup and Recovery
-------------------

