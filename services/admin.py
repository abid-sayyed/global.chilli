from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Feedback, Reservation

# Register your models here.

# customer = get_user_model()

# class  CustomerInline(admin.TabularInline):
#     # readonly_fields = ['localname',]
#     model = customer
#     extra = 1
#     # fieds = ('localname',)


class FeedbackAdmin(admin.ModelAdmin):
    # inline = [CustomerInline]
    model = Feedback
    list_display=['full_name','Email', 'quality_of_food', 'portion_size', 'ease_of_ordering', 'overall_value', 'suggestions',]

    # @admin.display(description='Account', ordering='email')
    # def get_author_name(self, obj):
    #     return obj.customer.email


    # def get_author(self, obj):
    #     return obj.customer.email
    # get_author.short_description = 'Author'
    # get_author.admin_order_field = 'book__author'
    

class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ['full_name','Email','booking_date','booking_time', 'total_person','contact_no','message']

admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Reservation, ReservationAdmin)
