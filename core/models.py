from django.conf import settings
from django.db import models
from django.forms.models import modelformset_factory
from django.shortcuts import reverse
from accounts.models import CustomerProfile


class Item(models.Model):
    item_pic = models.ImageField(upload_to='FoodMenu/') # have used pillow for this
    item_name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.CharField(max_length = 200, blank = True, null= True)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "pk" : self.pk
        })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()

        
    
def all_item():
    ItemList = OrderItem.objects.all()
    return ItemList
    

class Order(models.Model):
    PAYMENT_CHOICES = [
        ('cod','Cash On Delivery'),
        ('upi','UPI'),
        ('googlepay','GPay'),
        ('paytm','Paytm'),
        ('banktransfer','Bank Transfer'),
        
        ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem,default= all_item)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add = True)
    ordered = models.BooleanField(default=False)
    payment_mode = models.CharField(max_length=20,choices= PAYMENT_CHOICES,blank= True)
    Transaction_id = models.CharField(max_length = 30,blank= True)
    profile  =  models.ForeignKey(CustomerProfile, on_delete= models.CASCADE,blank= True,null = True)
    confirm = models.BooleanField(default=True)



    def __str__(self):
        return self.user.username



    def user_email(self):
        return self.user.email

    def customer_full_name(self):
        if not self.profile:
            return None
        return self.profile.full_name

  
    def contact_no(self):
        if not self.profile:
            return None
        return self.profile.contact_no

    def customer_address(self):
        if not self.profile:
            return None
        return self.profile.address


    # def __str__(self):
    #     if not self.author:
    #         return "Anonymous"
    #     return self.author.username


   

    def item_list(self):
        return [p.item for p in self.items.all()]

    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total



    def get_absolute_url(self):
        return reverse('ThankyouFeedback')
