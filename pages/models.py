from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import EmailField

# Create your models here.
class RestaurantDetail(models.Model):
    
    RestaurantName = models.TextField(max_length=30)
    LogoPicture = models.ImageField(upload_to='Logo/') # have used pillow for this
    AboutPicture = models.ImageField(upload_to='About/') # have used pillow for this
    TagLine = models.CharField(max_length=200)
    Discription = models.TextField()
    ContactNo = models.CharField(max_length= 20)
    Email= models.EmailField()
    Address= models.CharField(max_length=200)



    def __str__(self):
        return self.RestaurantName



class HomepageMenu(models.Model):

    home_picture_first = models.ImageField(upload_to='HomePicture/', blank= True) # have used pillow for this
    title_first = models.CharField(max_length=200,blank=True)

    home_picture_second = models.ImageField(upload_to='HomePicture/',blank = True) # have used pillow for this
    title_second = models.CharField(max_length=200,blank= True)

    home_picture_third = models.ImageField(upload_to='HomePicture/', blank= True) # have used pillow for this
    title_third = models.CharField(max_length=200, blank = True)

    foodmenu = models.ImageField(upload_to='HomePicture/',blank= True) # have used pillow for this
    title = models.CharField(max_length=200,blank= True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank= True,null=True)

    def __str__(self):
        return self.title_first

    

class FoodMenu(models.Model):

    foodmenu = models.ImageField(upload_to='FoodMenu/', blank=True) # have used pillow for this
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

    
    def __str__(self):
        return self.title



class Gallery(models.Model):

    
    GalleryPage = models.ImageField(upload_to='Gallery/') # have used pillow for this
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

