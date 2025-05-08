from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    staff = models.OneToOneField(User,on_delete=models.CASCADE ,null=True,default=1) 
    #agar User or staff delete kare to uska profile bhi delete hoga 
    address = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    image= models.ImageField(default='avatar.jpg',upload_to='Profile_images')
    
    def __str__(self):
        return f'{self.staff.username}-Profile'