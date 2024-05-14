from django.contrib.auth.forms import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import Profile
from .tasks import send_email_to_new_users

@receiver(post_save, sender=User)
def createUser(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user = user,
            name = user.first_name,
            username = user.username,
            email = user.email,
        )
        user.save()
        
        # CALLING CELERY SEND EMAIL TASK
        send_email_to_new_users.delay_on_commit(user.id)

        
        
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
        
        
    
    
    