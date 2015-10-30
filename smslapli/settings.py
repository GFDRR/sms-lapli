# Django settings for smslapli project.

import os

# The top directory for this project. Contains requirements/, manage.py,
# and README.rst, a smslapli directory with settings etc (see
# PROJECT_PATH), as well as a directory for each Django app added to this
# project.
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# The directory with this project's templates, settings, urls, static dir,
# wsgi.py, fixtures, etc.
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'smslapli')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'smslapli.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'testbase',
#         'USER': 'esdras',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fr'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/public/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/public/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files to collect
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0k^@f)raql%=@)#7q251w$l(590dx_fjzuq9*+58u*r48q*$wc'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',

)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'smslapli.context_processors.get_infos',
    #'smslapli.context_processors.app_list',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
)

ROOT_URLCONF = 'smslapli.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'smslapli.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_PATH, 'fixtures'),
)

# A sample logging configuration.
# This logs all rapidsms messages to the file `rapidsms.log`
# in the project directory.  It also sends an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(name)-20s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'basic',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'basic',
            'filename': os.path.join(PROJECT_PATH, 'rapidsms.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'rapidsms': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

INSTALLED_APPS = (
    # 'd',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.sitemaps',

    # External apps
    'django_tables2',
    'selectable',

    # RapidSMS
    'rapidsms',
    'admin_reorder',
    'rapidsms.backends.database',
    'rapidsms.contrib.handlers',
    'rapidsms.contrib.httptester',
    'rapidsms.contrib.messagelog',
    'rapidsms.contrib.messaging',
    'rapidsms.contrib.registration',
    #"rapidsms.contrib.echo',

    # SMS Lapli Apps
    'base',
    'hydromet',
    'sms_gateway', #This is the one who will be used to handle sms

    # Must Be last
    'rapidsms.contrib.default',
)

INSTALLED_BACKENDS = {
    "message_tester": {
        "ENGINE": "rapidsms.backends.database.DatabaseBackend",
    },
    # "kannel-fake-smsc" : {
    #     "ENGINE":  "rapidsms.backends.kannel.KannelBackend",
    #     "sendsms_url": "http://127.0.0.1:13013/cgi-bin/sendsms",
    #     "sendsms_params": {"smsc": "FAKE",
    #                        "from": "123", # not set automatically by SMSC
    #                        "username": "esdras",
    #                        "password": "esdras1995"}, # or set in localsettings.py
    #     "coding": 0,
    #     "charset": "ascii",
    #     "encode_errors": "ignore", # strip out unknown (unicode) characters
    #},

    "kannel-usb0-smsc" : {
        "ENGINE":  "rapidsms.backends.kannel.KannelBackend",
        "sendsms_url": "http://127.0.0.1:14000/cgi-bin/sendsms",
        "sendsms_params": {"smsc": "usb0-modem",
                           "from": "+50934772370", # not set automatically by SMSC
                           "username": "rapidsms",
                           "password": "CHANGE-ME"}, # or set in localsettings.py
        "coding": 0,
        "charset": "ascii",
        "encode_errors": "ignore", # strip out unknown (unicode) characters
    },
}

# INSTALLED_BACKENDS = {
#     # ...
#     # other backends, if any
#     "kannel-fake-smsc" : {
#         "ENGINE":  "rapidsms.backends.kannel.KannelBackend",
#         "sendsms_url": "http://127.0.0.1:13013/cgi-bin/sendsms",
#         "sendsms_params": {"smsc": "FAKE",
#                            "from": "123", # not set automatically by SMSC
#                            "username": "rapidsms",
#                            "password": "CHANGE-ME"}, # or set in localsettings.py
#         "coding": 0,
#         "charset": "ascii",
#         "encode_errors": "ignore", # strip out unknown (unicode) characters
#     },
# }

DEFAULT_RESPONSE = "Message incorrect!"
LOGIN_REDIRECT_URL = '/'

RAPIDSMS_HANDLERS = (
    'rapidsms.contrib.echo.handlers.echo.EchoHandler',
    #'rapidsms.contrib.echo.handlers.ping.PingHandler',
    'tut.myhandlers.HelpHandler',
    'tut.myhandlers.SumHandler',
)

# SUIT_CONFIG = {
#     'ADMIN_NAME': 'SMS Lapli',
#     'SEARCH_URL': '',
#     'MENU': (
#         {'app': 'donnees_de_base', 'label': 'Structure de base', 'icon': 'icon-road', 'models': ('departement', 'commune', 'sectioncommunale', 'sitesentinelle', 'poste', 'personnecontact')},
#         {'app': 'donnees_hydrometeologique', 'label': 'Collecte Pluviometrique', 'icon': 'icon-filter', 'models': ('hydromet.TypeStationPluviometrique', 'hydromet.StationPluviometrique', 'hydromet.ObservationPluviometrique', 'hydromet.Log',)},
#         {'app': 'auth', 'label': 'Autorisation', 'icon': 'icon-lock', 'models': ('GROUP')},
#     )
# }

ADMIN_REORDER = (
    # Reorder app models
    {'app': 'base',  'label': 'Structure de base', 'models': ('base.Departement', 'base.Commune', 'base.SectionCommunale', 'base.SiteSentinelle', 'base.Poste', 'base.PersonneContact')},
    {'app': 'hydromet',  'label': 'Collecte Pluviometrique', 'models': ('hydromet.TypeStation', 'hydromet.Station', 'hydromet.Observation', 'hydromet.UniteDeMesure', 'hydromet.StationObservers', 'hydromet.Log')},
    {'app': 'auth',  'label': 'Autorisation',},
)
