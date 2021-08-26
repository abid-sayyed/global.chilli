from django.contrib import admin
from .models import Item, OrderItem, Order


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['ordered','start_date','user','user_email','customer_full_name','contact_no','customer_address','item_list','get_total_price','payment_mode','Transaction_id']



admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order,OrderAdmin)
