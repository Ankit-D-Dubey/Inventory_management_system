from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.dispatch import receiver

#signals ko use karna hai kyuki jaise hi hum user create kare to uska ek profile bhi create hona chahiye automatically.
 
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(staff=instance)
        

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()