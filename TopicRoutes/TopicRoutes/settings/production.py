from TopicRoutes.settings.base import *

import os

DEBUG = os.environ['DJANGO_DEBUG']

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = '*'


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'TopicRoutesProd',
        'HOST': 'topicroutes.database.windows.net',
        'USER': os.environ['DJANGO_DATABASE_USER'],
        'PASSWORD': os.environ['DJANGO_DATABASE_PASSWORD']
    }
}