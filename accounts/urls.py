from django .urls import path
from .views import ProfileView2, ProfileUpdateView
from django.contrib.auth import get_user_model


customer = get_user_model()
urlpatterns = [
    

    
    path('profile/',ProfileView2.as_view(), name= 'profile_detail'),
    path('profile/<int:pk>/edit/',ProfileUpdateView.as_view(), name='profile_edit'), # new

    
]
