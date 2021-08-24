from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomerCreationForm, CustomUserchangeForm
from .models import CustomerProfile

# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    forms = CustomUserchangeForm
    model = CustomUser
    list_display = ['username', 'email',]



class CustomerProfileAdmin(admin.ModelAdmin):
    model = CustomerProfile(admin.ModelAdmin)
    list_display = ['profile_username', 'full_name','contact_no','address','picture']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)

