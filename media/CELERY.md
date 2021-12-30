# Celery with Django

[![Celery with Django](https://i.ytimg.com/vi/Sre0SJEpiaU/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLAtXwCqzYXQRWd9RqYjBnVFatIV9g)](https://www.youtube.com/playlist?list=PL1WVjBsN-_NLBFi3lU4xnwy-AFTbdbxiX)


[![Python Django - Creating a job scheduler](https://i.ytimg.com/vi/C3wipLP4gNc/hqdefault.jpg?sqp=-oaymwEbCKgBEF5IVfKriqkDDggBFQAAiEIYAXABwAEG&rs=AOn4CLDq6w6ozA19HtILXqazmrqFNrJTEQ)](https://youtu.be/Lzy4G1wZ7NQ)

[is in Building and launching a REAL Django website](https://www.youtube.com/playlist?list=PL5VlxT4gkOFBLLgAKWp7CBwe-kpy7CxWz)

<br/>

## Introduction
This project is just to demonstrate how celery can be integrated with django project to call task asynchronously as well as synchronously if required. Tasks can also be executed on schedule as well as periodically.

<br/>

## Learning points
- Celery configuration
- Write celery task in django app
- Call task asynchronously
- Execute task periodically

<br/>

## Apps.py script run automatically
```python
# apps.py
from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'

    # Automatic Starting Script
    def ready(self):
    	from jobs import updater
    	updater.start()
```

<br/>

## Celery Tutorial Steps
- [Using Celery with Django](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html#first-steps-with-django)

```r
# Run celery worker to receive tasks and execute
$ celery -A server worker -l info -Q celery,high

# Run celery beat for sending task periodically to workers
$ celery -A server beat

# Run command line events monitor
$ celery -A server events

# Monitor flower web `http://localhost:5555`
$ pip install flower
$ celery -A server flower
```

<br/>

## 1 Asynchronous Task
### Django with Ipython
- [Django 에서 Celery 활용하기 1 ~4](https://devlog.jwgo.kr/2019/07/02/using-celery-with-django-1/)

```r
$ ./manage.py shell -i ipython
Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.27.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

### RabbitMQ
- [Installing on Debian and Ubuntu | RabbitMQ](https://www.rabbitmq.com/install-debian.html)
- [Install Latest RabbitMQ Server on Ubuntu 20.04](https://computingforgeeks.com/how-to-install-latest-rabbitmq-server-on-ubuntu-linux/)
- [Ubuntu 에서 RabbitMQ 설치하기](https://jonnung.dev/rabbitmq/2019/01/30/rabbitmq-installation-on-ubuntu/)
- [Python Celery & RabbitMQ Tutorial](https://kimdoky.github.io/tech/2019/01/23/celery-rabbitmq-tuto/)
- [Celery Using RabbitMQ](https://docs.celeryproject.org/en/4.4.2/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq)
- [celery 에러 핸들링](https://yuda.dev/223)

```r
$ apt install rabbitmq-server
```

RabbitMQ 에 User(`rabbit`) 와 Virtual Host(`rabbit_host`) 를 생성하고, Virtual Host 에 접속가능한 <i style="color:orange">사용자 권한</i> 을 설정 및 추가 합니다. Though the broker url is `amqp://myusername:mypassword@localhost:5672/myvirtualhost`

```r
$ rabbitmqctl add_user username password
Adding user "username" ...

$ rabbitmqctl add_vhost user_host
Adding vhost "user_host" ...

$ rabbitmqctl set_user_tags username user_tag   
$ rabbitmqctl set_permissions -p userhost username ".*" ".*" ".*"
Setting permissions for user "username" in vhost "user_host" ...

$ rabbitmqctl list_users                               
Listing users ...
username	[user_host]
```

RabbitMQ url in celery

```python
# settings.py
CELERY_BROKER_URL = 'amqp://username:password@localhost:5672/user_host'
```


### Celery First Steps with Django
- After Celery works, the task's status is changed.

```r
$ celery -A server worker -l info

[tasks]
  . notification.tasks.sum
  . server.celery.debug_task
[2021-09-15] Connected to amqp://guest:**@127.0.0.1:5672//
```

<br/>

## 2 Django Celery Results
### django-celery-results
- [django-celery-results | Celery Result Backends](https://django-celery-results.readthedocs.io/en/latest/)
- [django-celery-results | Github](https://github.com/celery/django-celery-results)
- [CELERY_RESULTS_BACKEND](https://docs.celeryproject.org/en/stable/userguide/configuration.html#file-system-backend-settings)

```r
$ python manage.py makemigrations

Operations to perform:
  Apply all migrations: django_celery_results:


$ python manage.py inspectdb                             
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
...


$ celery -A server worker -l info

--------------- celery@pop-os v5.1.2 (sun-harmonics)
--- ***** ----- Linux-5.8.0-7630-generic-x86_64
-- ******* ---- 
- *** --- * --- [config]
- ** ---------- .> app:       server:
- ** ---------- .> transport: amqp://guest:**@localhost:5672
- ** ---------- .> results:     
- ** ---------- .> concurrency: 12 (prefork) 
- *** --- * --- .> task events: OFF
-- ******* ----
--- ***** ----- [queues]
--------------- .> celery exchange=celery(direct) key=celery


$ ./manage.py shell_plus --ipython

In [1]: from notification.tasks import sum
In [2]: t = sum.delay(10, 20)
In [3]: t.status  # Task Working Check..
Out[3]: 'PENDING'
In [4]: t.status  # Task Finished Check..
Out[4]: 'SUCCESS'
```

<br/>

## 3 Setup Periodic Tasks
### django-celery-beat
- [Celery Periodic Tasks #Entries](https://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html#entries)
- [django-celery-beat Github](https://github.com/celery/django-celery-beat)
- [Crontab schedules](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html#crontab-schedules)

```r
# Celery Status Monitoring...
$ celery -A server worker -l info


$ celery -A server beat -l info
celery beat v5.1.2 (sun-harmonics) is starting.
__    -    ... __   -        _
LocalTime -> 2021-09-15 19:08:36
Configuration ->
    . broker -> amqp://guest:**@localhost:5672//
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%INFO
    . maxinterval -> 5.00 minutes (300s)
[2021-09-15 19:08:36,134: INFO/MainProcess] beat: Starting...
```

<br/>

## 4-1 Monitoring and Management
### Celery Cli
- [Celery Monitoring and Management Guide](https://docs.celeryproject.org/en/stable/userguide/monitoring.html)

```r
$ celery -A server worker -l info
 -------------- celery@pop-os v5.1.2 (sun-harmonics)


$ celery -A server worker -n test@example.com
 -------------- test@example.com v5.1.2 (sun-harmonics)


$ celery -A server status                    
->  test@example.com: OK
->  celery@pop-os: OK


$ celery -A server inspect active
->  test@example.com: OK
    - empty -
->  celery@pop-os: OK
    - empty -

2 nodes online.


$ celery -A server inspect revoked
->  celery@pop-os: OK
    - empty -

1 node online.


$ celery -A server inspect stats    
->  celery@pop-os: OK
{
  ...
  "pool": {
    "max-concurrency": 12,
    "max-tasks-per-child": "N/A",
    "processes": [
      36886,36887,36888,... (12개 병렬가능)
    ],
  },
  ...
  "total": {
    "notification.tasks.send_email": 42
  },
  "uptime": 864
}
   
1 node online.

$ celery -A server purge -Q test
WARNING:This will remove all tasks from queue: test.
         There is no undo for this operation!

(to skip this prompt use the -f option)
Are you sure you want to delete all tasks? [y/N]: 
```

<br/>

## 4-2 Event
### Celery Cli
- [flower Monitoring](https://github.com/mher/flower)
```r
$ celery -A server control enable_events
->  celery@pop-os: OK
        task events enabled
[2021-09-18:INFO/MainProcess] Events of group {task} enabled by remote.

$ celery -A server events
 cli terminal monitoring

$ pip install flower
$ celery -A server flower
```