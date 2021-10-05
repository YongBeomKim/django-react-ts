# Build paths inside the project like this: BASE_DIR / 'subdir'.
# https://docs.python.org/ko/3/library/configparser.html
import configparser
from pathlib import Path
from datetime import timedelta
BASE_DIR = Path(__file__).resolve().parent.parent

# Setting Params from `settings.ini`
config = configparser.ConfigParser(interpolation=None)
config.read(BASE_DIR / 'settings.ini')

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
PSQL_KEY = 'PSQL'
SECRET_KEY = config['DJANGO']['secret_key']
DB_HOSTS = {
    'sqlite3': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    "psql":{
        key.upper(): config[PSQL_KEY][key]  
        for key in config[PSQL_KEY]
    },
}


# REST_FRAMEWORK
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
}


# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    "ALGORITHM": "HS256",
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    "server.staticfiles",  # Customized Static
    "django_extensions",
    "rest_framework",
    'rest_framework_simplejwt',
    # Celery Crontab
    'django_celery_results',
    'django_celery_beat',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'server.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            # https://docs.djangoproject.com/en/3.1/topics/templates/#module-django.template.backends.django
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
USE_TZ = False

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    (BASE_DIR.joinpath("static")),
]
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("media")


# Celery Configuration Options
# The CELERY_ namespace is also optional, but recommended 
# (to prevent overlap with other Django settings)
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-result_backend
CELERY_TIMEZONE = "Asia/Seoul"
# CELERY_BROKER_URL = "amqp://rabbit:celerydj@localhost:5672/rabbithost"
CELERY_BROKER_URL = 'redis://localhost:6379'
#CELERY_RESULT_BACKEND = 'rpc://localhost'
#CELERY_TASK_TRACK_STARTED = True

# Issues with mysql
# https://github.com/celery/django-celery-results
DJANGO_CELERY_RESULTS_TASK_ID_MAX_LENGTH=191

# Configure Celery to use the django-celery-results backend.
# https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#django-celery-results-using-the-django-orm-cache-as-a-result-backend
CELERY_RESULT_BACKEND = 'django-db'
# celery setting.
CELERY_CACHE_BACKEND = 'django-cache'
# django setting.
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#     }
# }