from django.conf import settings
import os  
from celery import Celery
from celery.schedules import crontab

# Using Celery with Django
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
server_name = 'server'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{server_name}.settings')

# Using a string here means the worker doesn't have to serialize
# - namespace='CELERY':should have a `CELERY_` prefix.
app = Celery(server_name)
app.config_from_object('django.conf:settings', namespace='CELERY_STOCK')

# Celery Periodic Tasks
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#entries
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        # 'task': 'games.tasks.send_email',
        # 'schedule': crontab(minute='*/1'),
        'schedule': 5,
        'args': ('django@python.com','This is the sample.'),
    },
}

# Load task modules Django apps.
app.conf.timezone = 'Asia/Seoul'
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



## games/tasks.py
# import time
# from celery import shared_task

# @shared_task
# def sum(a, b):
#     time.sleep(3)
#     return a + b

# @shared_task
# def send_email(email, message):
#     time.sleep(5)
#     print(f'A sample message is sent to : {email}\n Message is : {message}')