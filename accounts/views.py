from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomerProfile
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages




# Create your views here.

# class ProfileView(LoginRequiredMixin, ListView):
#     context_object_name = 'profile_list' # for rememebering the name of object_list which we will use in templates
#     model = CustomerProfile
#     template_name = 'account/profile.html'
#     fields = "__all__"
  

#     login_url = 'account_login'# new



class ProfileCreateView(CreateView): # new
    model = CustomerProfile
    template_name = 'account/ProfileCreate.html'
    fields = ['full_name','contact_no','address','picture',]

    # def get_object(self):
    #     places = CustomerProfile.objects.get(profile_username=self.request.user)
    #     return get_object_or_404(CustomerProfile, pk=places.id)

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.profile_username = self.request.user
        # profile = CustomerProfile.objects.get(profile_username=self.request.user)
     
        # app_model.profile =Order.object.get(profile=self.request.CustomerProfile)# Or explicit model 
        # app_model.profile = get_object_or_404(CustomerProfile, pk=profile.id)
        app_model.save()
        return super().form_valid(form)




    # def get_object(self):
    #     profile = CustomerProfile.objects.get(profile_username=self.request.user)
    #     return get_object_or_404(CustomerProfile, pk=profile.id)

    
class ProfileView2(LoginRequiredMixin, DetailView):
    # context_object_name = 'profile_list' # for rememebering the name of object_list which we will use in templates
    model = CustomerProfile
    template_name = 'account/profile2.html'
    fields = "__all__"  
    login_url = 'account_login'# new
    
    def get_object(self):
        try:
            profile = CustomerProfile.objects.get(profile_username=self.request.user)
            return get_object_or_404(CustomerProfile, pk=profile.id)
        except:
            return redirect('profile_create')

            # messages.error(self.request, "you did not fill the profile detail")
            # return redirect("profile_create")
            






   

class ProfileUpdateView(UpdateView): # new
    model = CustomerProfile
    template_name = 'account/ProfileEdit.html'
    fields = ['full_name','contact_no','address','picture',]


    def get_object(self):
        try:
            places = CustomerProfile.objects.get(profile_username=self.request.user)
            return get_object_or_404(CustomerProfile, pk=places.id)
        except ObjectDoesNotExist:
            messages.error(self.request, "you did not fill the profile detail yet ,please fill it before proceeding further")
            return redirect('profile_create')
        except:
            redirect('profile_create')


  
    # def ProfilePicture(self):
    #     return get_object_or_404(CustomerProfile, pp=self.request.picture)





