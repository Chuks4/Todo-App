from django.contrib.auth.forms import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def createUser(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email,
        )
        subject = 'Welcome to Taskify'
        message = f'Hi {user.username} thank you for registering in Taskify, here we help you plan your day.'
        send_mail (
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        
        
@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    profile = instance
    user= profile.user
    user.delete()


@receiver(post_save, sender=Profile)
def editProfile(sender, instance, created, **kwargs):
    if not created:
        profile = instance
        user = profile.user
        
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        
        user.save()
        
        
    
    
    