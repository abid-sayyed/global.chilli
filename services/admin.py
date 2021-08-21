from django.contrib import admin
from .models import Feedback, get_user_model

# Register your models here.

customer = get_user_model()

class  CustomerInline(admin.TabularInline):
    # readonly_fields = ['localname',]
    model = customer
    extra = 1
    # fieds = ('localname',)


class FeedbackAdmin(admin.ModelAdmin):
    inline = [CustomerInline]
    model = Feedback
    list_display=['username', 'quality_of_food', 'portion_size', 'ease_of_ordering', 'overall_value', 'suggestions','Email',]

    # @admin.display(description='Account', ordering='email')
    # def get_author_name(self, obj):
    #     return obj.customer.email


    # def get_author(self, obj):
    #     return obj.customer.email
    # get_author.short_description = 'Author'
    # get_author.admin_order_field = 'book__author'
    


    

admin.site.register(Feedback,FeedbackAdmin)
