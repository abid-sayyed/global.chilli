from django.contrib import admin
from .models import Item, OrderItem, Order


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ['item_pic', 'item_name', 'price', 'discount_price', 'description']


class OrderItemAdmin(admin.ModelAdmin):
    model = OrderItem
    list_display = ['user','ordered','item','quantity']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['ordered','start_date','user','user_email','customer_full_name','contact_no','customer_address','item_list','get_total_price','payment_mode','Transaction_id']



admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
