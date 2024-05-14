from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Todo.settings')

app = Celery('Todo')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc = False
app.conf.update(timezone = 'Africa/Lagos')

#  CELERY BEAT SETTINGS
app.conf.beat_schedule = {
     'send_notification_every_48hrs': {
         'task' : 'notifications.tasks.send_notifications',   # Add the appname.task filename.tasks function name
         'schedule' : crontab(hour=12, minute=35)
     }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self:request!r}')