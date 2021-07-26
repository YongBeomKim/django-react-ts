from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a2@bz#xcoo4&l6kfwnnrcdnu-6009u%cgs7ns254220gfuv5(h'


DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
    "default": DB_HOSTS['sqlite3']
}
# Enviorment texts
REACT_DEV_URL = "http://localhost:3000/"
REACT_HOST_URL = "static/dist/"
SIMPLE_JWT['SIGNING_KEY'] = SECRET_KEY

# Application definition
# INSTALLED_APPS += [
# ]

if DEBUG:
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    INSTALLED_APPS += ['corsheaders', "debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    INTERNAL_IPS = "127.0.0.1"
    CORS_ORIGIN_WHITELIST = [
        'http://localhost:3000',
        'https://localhost:3000',
        'http://127.0.0.1:8000',
    ]
