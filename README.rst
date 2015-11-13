SMS-Lapli
========================

Haiti Code for Resilience SMS Rainfall Data Collection Project based on RapidSMS

Presentation
------------
"SMS Lapli" is a project that aims to optimize and facilitate the collection and management of rainfall data over the entire national territory. Apart from the most obvious interfaces (such as web forms or automatic stations), the database can be updated by sending a simple SMS. Indeed, observers perform a daily reading of the manual stations and sending the results directly to the database using SMS. The project is also focusing on a double validation of the observation's data for a better quality control.

Challenge
------------
Facilitate the management and especially the collection of the rainfall data without requiring a significant investment (eg without purchasing a smartphone or a tablet and an internet plan for each observer).

Getting Started
---------------

Below you will find basic setup instructions for the ``smslapli``
project. To begin you should have the following applications installed on your
local development system:

- `Python >= 2.7 (including Python 3) <http://www.python.org/getit/>`_
- `pip >= 7.0.3 <http://www.pip-installer.org/>`_
- `virtualenv >= 13.0.3 <http://www.virtualenv.org/>`_

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    virtualenv smslapli-env

On Posix systems you can activate your environment like this::

    source smslapli-env/bin/activate

On Windows, you'd use::

    smslapli-env\Scripts\activate

Then::

    cd smslapli
    pip install -U -r requirements/base.txt

Run migrate::

    python manage.py migrate

Load Base Data::

    python manage.py loaddata base/fixtures/initial_data.json
    python manage.py loaddata hydromet/fixtures/initial_data.json

You should now be able to run the development server::

    python manage.py runserver
    
Open http://localhost:8000 in your web browser and you should see **the public home page** of the project.

You can also access the admin section : 

- by using this link : http://localhost:8000/admin/
- by clicking the admin green button at the the top of every pages of the public section of the website

**You need a valid account to access the admin section**.

To have a valid login account (a super user), please create one with the following command and follow the instructions::

    python manage.py createsuperuser

