from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


from .forms import CustomerCreationForm, CustomUserchangeForm


# Register your models here.

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomerCreationForm
    forms = CustomUserchangeForm
    model = CustomUser
    list_display = ['username', 'email',]



    

admin.site.register(CustomUser, CustomUserAdmin)
