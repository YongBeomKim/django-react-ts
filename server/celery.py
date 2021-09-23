# Using Celery with Django
# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
server_name = 'server'


import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{server_name}.settings')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app = Celery(server_name)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Periodic Tasks
# https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#entries
app.conf.beat_schedule = {
    # 'add-every-5-seconds': {
    #     'task': 'notifications.tasks.send_email',
    #     # 'schedule': crontab(minute='*/1'),
    #     'schedule': 5,
    #     'args': ('django@python.com','This is the sample.'),
    # },
}

# Load task modules Django apps.
app.conf.timezone = 'Asia/Seoul'
app.autodiscover_tasks() 


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')