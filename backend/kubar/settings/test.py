from .base import *


class DisableMigrations(object):
    """
    Wrapper to be used with MIGRATION_MODULES to disable all migrations
    Disable Migrations using MIGRATION_MODULES = DisableMigrations()
    """

    # Inspired by this fix
    # https://github.com/henriquebastos/django-test-without-migrations/
    # blob/master/test_without_migrations/management/commands/_base.py
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


DEBUG = False
CHECKLIST_SUPPRESS_ERRORS = True

MIGRATION_MODULES = DisableMigrations()

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

SITE_HOST = 'http://test'
