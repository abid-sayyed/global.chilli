from django .urls import path
from .views import ProfileDetailView, ProfileUpdateView
from django.contrib.auth import get_user_model


customer = get_user_model()
urlpatterns = [
    

    
    path('profile/',ProfileDetailView.as_view(), name= 'profile_detail'),
    path('profile/edit/',ProfileUpdateView.as_view(), name='profile_edit'), # new
    # path('profile/create/',ProfileCreateView.as_view(), name='profile_create'), # don't require, using signal instead of this

    
]
