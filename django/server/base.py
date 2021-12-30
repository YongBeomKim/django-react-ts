""" 'django-admin startproject' using Django 3.2.10.
https://docs.djangoproject.com/en/3.2/topics/settings/
https://docs.djangoproject.com/en/3.2/ref/settings/"""


FILE_SQL = "db.sqlite3"
FILE_SETTING = 'settings.ini'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# https://docs.python.org/ko/3/library/configparser.html
import configparser
from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent


# Setting Params from `settings.ini`
config = configparser.ConfigParser(interpolation=None)
config.read(BASE_DIR / FILE_SETTING)


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
PSQL_KEY = 'PSQL'
SECRET_KEY = config['DJANGO']['secret_key']
DB_HOSTS = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / FILE_SQL,
    },
    "psql":{
        key.upper(): config[PSQL_KEY][key]  
        for key in config[PSQL_KEY]
    },
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "server.staticfiles",  # Customized Static
    "django_extensions",
    'corsheaders'
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# CORS_ORIGIN_ALLOW_ALL = True 
CORS_ORIGIN_WHITELIST = [
    'http://3.34.63.174:8000',
    'http://localhost:3000',
    'https://localhost:8000',
    'http://127.0.0.1:8000',
    'http://0.0.0.0:8000',
]
CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'server.urls'

# https://docs.djangoproject.com/en/4.0/topics/templates/#module-django.template.backends.django
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            "libraries": {
                "react": "server.templatetags.react",
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
WSGI_APPLICATION = 'server.wsgi.application'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (BASE_DIR.joinpath("../react")),
]
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("../media")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery Configuration Options
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-result_backend
CELERY_TIMEZONE = "Asia/Seoul"
CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_BROKER_URL = "amqp://rabbit:celerydj@localhost:5672/rabbithost"
# CELERY_RESULT_BACKEND = 'rpc://localhost'
# CELERY_TASK_TRACK_STARTED = True

# Issues with mysql
# https://github.com/celery/django-celery-results
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH=191

# Configure Celery to use the django-celery-results backend.
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-celery-results-using-the-django-orm-cache-as-a-result-backend
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
