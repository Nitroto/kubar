from .base import *

DEBUG = False
CHECKLIST_SUPPRESS_ERRORS = True

FRONTEND_SITE_HOST = 'foo'
ALLOWED_HOSTS = []

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

MIGRATION_MODULES = DisableMigrations()

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SITE_HOST = 'http://test'

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
