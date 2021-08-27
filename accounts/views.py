from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomerProfile
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.

# class ProfileView(LoginRequiredMixin, ListView):
#     context_object_name = 'profile_list' # for rememebering the name of object_list which we will use in templates
#     model = CustomerProfile
#     template_name = 'account/profile.html'
#     fields = "__all__"
  

#     login_url = 'account_login'# new
    
class ProfileView2(LoginRequiredMixin, DetailView):
    # context_object_name = 'profile_list' # for rememebering the name of object_list which we will use in templates
    model = CustomerProfile
    template_name = 'account/profile2.html'
    fields = "__all__"
  

    login_url = 'account_login'# new

    def get_object(self):
        profile = CustomerProfile.objects.get(profile_username=self.request.user)
        return get_object_or_404(CustomerProfile, pk=profile.id)

   

class ProfileUpdateView(UpdateView): # new
    model = CustomerProfile
    template_name = 'account/ProfileEdit.html'
    fields = ['full_name','contact_no','address','picture',]


    def get_object(self):
        places = CustomerProfile.objects.get(profile_username=self.request.user)
        return get_object_or_404(CustomerProfile, pk=places.id)


  
    # def ProfilePicture(self):
    #     return get_object_or_404(CustomerProfile, pp=self.request.picture)





