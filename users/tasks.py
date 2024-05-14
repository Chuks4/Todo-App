from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model


@shared_task(bind=True)
def send_email_to_new_users(self, user_id):
    user = get_user_model().objects.get(id=user_id)
    subject = "Welcome to Taskify"
    message = f"Hi {user.username} thank you for registering for Taskify, here we help you plan your day."
    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
