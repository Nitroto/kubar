"""
Production Settings for Heroku
"""
from .base import *

CORS_ORIGIN_WHITELIST = []
CSRF_TRUSTED_ORIGINS = ['kubar.herokuapp.com']
