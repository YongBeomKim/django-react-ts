import time
from celery import shared_task


@shared_task
def sum(a, b):
    time.sleep(3)
    return a + b

@shared_task
def send_email(email, message):
    time.sleep(5)
    print(f'A sample message is sent to : {email}\n Message is : {message}')