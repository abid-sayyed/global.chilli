from accounts.models import CustomUser
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your models here.


class Feedback(models.Model):
    RATING_CHOICES = [
        ('excellent','Excellent'),
        ('good','Good'),
        ('average','Average'),
        ('poor','Poor'),
        
        ]
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,blank=True)
    quality_of_food = models.CharField(max_length=100,choices= RATING_CHOICES)
    portion_size = models.CharField(max_length=100,choices= RATING_CHOICES)
    ease_of_ordering = models.CharField(max_length=100,choices=RATING_CHOICES)
    overall_value = models.CharField(max_length=100,choices=RATING_CHOICES)
    suggestions = models.TextField(max_length= 150)

    def username(self):
        return self.customer.username

    def Email(self):
        return self.customer.email


    def __str__(self):
        return self.suggestions

    def get_absolute_url(self):
        return reverse('ThankyouFeedback')

    