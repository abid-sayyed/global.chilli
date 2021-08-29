from django .urls import path

from .views import HomePageView, AboutPageView, GalleryPageView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),

    path('about', AboutPageView.as_view(), name='about'),

    path('gallery/', GalleryPageView.as_view(), name='gallery'),

    # path('menu/',MenuPageView.as_view(), name='menu'),
    
]
