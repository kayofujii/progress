from __future__ import absolute_import, unicode_literals
from celery import shared_task

from time import sleep

@shared_task(bind=True)
def go_to_sleep(self, duration):
    print('9')
    sleep(duration)
    return 'Done'

@shared_task
def add(x, y):
    return x + y
