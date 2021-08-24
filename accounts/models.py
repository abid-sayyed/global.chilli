from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    pass




class CustomerProfile(models.Model):
    profile_username= models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='ProfilePicture/', blank=True) # have used pillow for this
    full_name= models.CharField(max_length= 100,blank= True)
    contact_no =models.CharField( max_length=10,blank =True)
    address = models.CharField(max_length= 300,blank= True)

    def __str__(self):
        return self.full_name
    
    def get_absolute_url(self):
        return reverse('profile_detail')



    

