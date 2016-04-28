from .base import *

DEBUG = False

ALLOWED_HOSTS = ['107.170.47.238', 'cmmatsd.com', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'NAME': 'cmma',
	'USER': 'cmma',
	'HOST': 'localhost',
	'PORT': '5432',
    }
}
