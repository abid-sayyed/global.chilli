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

    foodmenu = models.ImageField(upload_to='FoodMenu/') # have used pillow for this
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    

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



   
   
        
    # def Phone(self):
    #     return self.employee.contact_no --not working

   
   