from celery import Celery
from celery.schedules import crontab
from celery import signals
from django.conf import settings
import logging
import os  
from .base import BASE_DIR
from .logger import LOG_FOLDER


# Using Celery with Django
# https://docs.celeryproje ct.org/en/stable/django/first-steps-with-django.html
server_name = 'server'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{server_name}.settings')


# Load task modules Django apps.
# - namespace='CELERY':should have a `CELERY_` prefix.
app = Celery(server_name)
app.config_from_object('django.conf:settings', namespace='CELERY_KRX')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'Asia/Seoul'


# Celery Periodic Tasks
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#entries
app.conf.beat_schedule = {
    # 'krx-crawler': {
    #     'task': 'krx.tasks.crawler',
    #     'schedule': 60,
    #     # 'schedule': crontab(minute='*/1'),
    #     # 'args': ('django@python.com','This is the sample.'),
    # },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# Django Logging in Celery
# https://wdicc.com/logging-in-celery-and-django/
@signals.setup_logging.connect
def on_celery_setup_logging(**kwargs):
    LOG_LEVELS = 'INFO'
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                # 'format': '%(asctime)s%(process)d/%(thread)d%(name)s%(funcName)s %(lineno)s%(levelname)s%(message)s',
                'format': '%(asctime)s %(name)s %(funcName)s\n %(message)s',
                'datefmt': "%Y/%m/%d %H:%M:%S",
                'maxBytes': 1024*1024*1,
                'backupCount': 5
            }
        },
        'handlers': {
            'celery': {
                'level': LOG_LEVELS,
                'class': 'logging.FileHandler',
                'filename': BASE_DIR.joinpath(LOG_FOLDER + 'celery.log'),
                'formatter': 'default'
            },
            'default': {
                'level': LOG_LEVELS,
                'class': 'logging.StreamHandler',
                'formatter': 'default'
            }
        },
        'loggers': {
            'celery': {
                'handlers': ['celery'],
                'level': LOG_LEVELS,
                'propagate': False
            },
        },
        'root': {
            'handlers': ['default'],
            'level': LOG_LEVELS
        },
    }
    logging.config.dictConfig(config)