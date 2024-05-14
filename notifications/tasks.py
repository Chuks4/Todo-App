from celery import shared_task
from .models import Notification
from activities.models import TodoItem


@shared_task(bind=True)
def send_notifications(self):
    uncompleted = TodoItem.objects.filter(completed=False)
    title = 'Return to your task'
    message = 'You are yet to complete {{uncompleted}} task'
    
    
    for task in uncompleted:
        owner = task.owner
        notify = Notification.objects.create(owner=owner, title=title, message=message)
        notify.save()