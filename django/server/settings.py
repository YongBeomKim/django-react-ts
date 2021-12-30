from .base import *
from .logger import *

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = False
ALLOWED_HOSTS = [
    "3.34.63.174",
    "0.0.0.0",
    "127.0.0.1",
]

# https://stackoverflow.com/questions/38841109/csrf-validation-does-not-work-on-django-using-https
# https://docs.djangoproject.com/en/dev/releases/4.0/#format-change
CSRF_TRUSTED_ORIGINS = ['http://3.34.63.174']
FOLDER_NAME = "../media"
DATABASES = {
    "default": DB_HOSTS['sqlite3'], # psql
}

# Enviorment texts (DEBUG / boolean)
REACT_DEV_URL = "http://localhost:3000/"
REACT_HOST_URL = "/static/dist/"

# Application definition
# INSTALLED_APPS += [
# ]

# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://dzone.com/articles/how-to-fix-django-cors-error
if DEBUG:

    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    ALLOWED_HOSTS=['*']
    CORS_ORIGIN_ALLOW_ALL = True
    INTERNAL_IPS = "127.0.0.1"