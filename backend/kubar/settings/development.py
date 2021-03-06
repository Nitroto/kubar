from .base import *

DEBUG = True
SITE_HOST = 'http://localhost:8000'

ALLOWED_HOSTS = []

INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

LANGUAGE_CODE = 'en'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'kubar_dev',
        'USER': 'comstream',
        'PASSWORD': 'comstreamdev',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
