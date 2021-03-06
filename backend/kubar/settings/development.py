from .base import *

assert SECURE_SSL_REDIRECT

SECURE_SSL_REDIRECT = False
SITE_HOST = 'http://localhost:8000'

ALLOWED_HOSTS = ['*']

CSRF_COOKIE_SECURE = False
CORS_ORIGIN_WHITELIST = ['http://localhost:8080', 'http://127.0.0.1:8080']
CSRF_TRUSTED_ORIGINS = ['localhost', '127.0.0.1']

LANGUAGE_CODE = 'en'

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
