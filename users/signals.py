from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Profile.objects.create(user=user)

def updateProfile(sender, instance, created, **kwargs):
    print("!!!!!!!!")  

    if created==False:
        user = instance
        profile = Profile.objects.get(user=user)      
        profile.save()


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=User)

