from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import CustomerProfile
from django.views.generic import UpdateView, DetailView
from django.shortcuts import get_object_or_404

# using this for try-except exception

# from django.shortcuts import redirect, render
# from django.contrib.auth import get_user_model
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages





# for creating instance (here means pk) for CustomerProfile model automatically using singals

from allauth.account.signals import user_signed_up
from django.dispatch import receiver 
from . models import  CustomerProfile

@receiver(user_signed_up)
def new_user_signup(sender, **kwargs):
    p = CustomerProfile(profile_username = kwargs['user'])
    p.save()


#using signal instead of this

# class ProfileCreateView(CreateView): # new
#     model = CustomerProfile
#     template_name = 'account/ProfileCreate.html'
#     fields = ['full_name','contact_no','address','picture',]


#     def form_valid(self, form):
#         app_model = form.save(commit=False)
#         app_model.profile_username = self.request.user
#         app_model.save()
#         return super().form_valid(form)

    
class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomerProfile
    template_name = 'account/profile.html'
    fields = "__all__"  
    login_url = 'account_login'  #for sending to login page if not login -- using LoginrequiredMixin for this
    
    def get_object(self):
            profile = CustomerProfile.objects.get(profile_username=self.request.user)
            return get_object_or_404(CustomerProfile, pk=profile.id)


class ProfileUpdateView(UpdateView): 
    model = CustomerProfile
    template_name = 'account/ProfileEdit.html'
    fields = ['full_name','contact_no','address','picture',]


    def get_object(self):
        places = CustomerProfile.objects.get(profile_username=self.request.user)
        return get_object_or_404(CustomerProfile, pk=places.id)

