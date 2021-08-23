from django.conf import settings
from typing import Tuple
from accounts.models import CustomUser, CustomerProfile
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date


# Create your models here.


class Feedback(models.Model):
    RATING_CHOICES = [
        ('excellent','Excellent'),
        ('good','Good'),
        ('average','Average'),
        ('poor','Poor'),
        
        ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,blank= True)
    quality_of_food = models.CharField(max_length=100,choices= RATING_CHOICES)
    portion_size = models.CharField(max_length=100,choices= RATING_CHOICES)
    ease_of_ordering = models.CharField(max_length=100,choices=RATING_CHOICES)
    overall_value = models.CharField(max_length=100,choices=RATING_CHOICES)
    suggestions = models.TextField(max_length= 150)

    def __str__(self):
        return self.full_name

    def username(self):
        return self.customer.username

    def Email(self):
        return self.customer.email


    

    def get_absolute_url(self):
        return reverse('ThankyouFeedback')

    
    
    
class Reservation(models.Model):
  

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null = True)
    full_name = models.CharField(max_length=50)
    booking_date = models.CharField(max_length= 20)
    booking_time = models.CharField(max_length= 20)
    total_person = models.IntegerField()
    contact_no = models.CharField(max_length=14)
    message = models.TextField(max_length= 50)

    def __str__(self):
        return self.full_name

    def username(self):
        return self.customer.username

    def Email(self):
        return self.customer.email


    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('TableConfirm')

    
    
    