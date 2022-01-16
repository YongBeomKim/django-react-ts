# Enviorment Setting
FILE_SQL3 = "db.sqlite3"
FILE_SETTING = 'settings.ini'
MEDIA_FOLDER = "../media"
REACT_FOLDER = "../react"
REACT_DEV_URL = "http://localhost:3000/"
REACT_HOST_URL = "/static/dist/"
SHELL_PLUS = 'ipython'


# https://docs.djangoproject.com/en/dev/releases/4.0/#format-change
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1']
CORS_ALLOW_CREDENTIALS = True
ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
]
CORS_ORIGIN_WHITELIST = [
    'http://0.0.0.0:8000',
    'http://127.0.0.1:8000',
    'http://localhost:3000',
]


# Build paths inside the project like this: BASE_DIR / 'subdir'.
import configparser
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG = configparser.ConfigParser(interpolation=None)
CONFIG.read(BASE_DIR / FILE_SETTING)


# Database : Quick-start development settings
# https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
SECRET_KEY = CONFIG['DJANGO']['secret_key']
PSQL_KEY = 'PSQL'
DB_HOSTS = {
    'SQLITE3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / FILE_SQL3,
    },
    PSQL_KEY: {
        KEY.upper() : CONFIG[PSQL_KEY][KEY]
        for KEY in CONFIG[PSQL_KEY]
    },
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',

    # Customized Static Collection
    # 'django.contrib.staticfiles',
    'server.staticfiles',
    'django_extensions',
    'corsheaders',
    'channels',

    # Celery
    'django_celery_results',
    'django_celery_beat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'
ASGI_APPLICATION = 'server.asgi.application'
WSGI_APPLICATION = 'server.wsgi.application'
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
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath(MEDIA_FOLDER)


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (BASE_DIR.joinpath(REACT_FOLDER)),
]
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Celery Configuration Options
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-result_backend
# CELERY_BROKER_URL = "amqp://rabbit:celerydj@localhost:5672/rabbithost"
# CELERY_TASK_TRACK_STARTED = True
CELERY_TIMEZONE = "Asia/Seoul"
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'


# Issues with MYSQL
# https://github.com/celery/django-celery-results
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH = 191


# Configure Celery to use the django-celery-results backend.
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-celery-results-using-the-django-orm-cache-as-a-result-backend
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}