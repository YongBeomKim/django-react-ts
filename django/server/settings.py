from .base import *
from .logger import *


# Application definition
INSTALLED_APPS += [
    'api',
]


DEBUG = True
# DATABASES_NAME = 'PSQL'
DATABASES_NAME = 'SQLITE3'
DATABASES = {"default": DB_HOSTS[DATABASES_NAME],}


# https://dzone.com/articles/how-to-fix-django-cors-error
# https://channels.readthedocs.io/en/stable/topics/channel_layers.html
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    ALLOWED_HOSTS=['*']
    INTERNAL_IPS = "127.0.0.1"
    CORS_ORIGIN_ALLOW_ALL = True
    
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }