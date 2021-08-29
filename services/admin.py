from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Feedback, Reservation



class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display=['full_name','Email', 'quality_of_food', 'portion_size', 'ease_of_ordering', 'overall_value', 'suggestions',]

  
    

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['full_name','Email','booking_date','booking_time', 'total_person','contact_no','message']




    

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Reservation, ReservationAdmin)
