from pages.models import FoodMenu, Gallery, RestaurantDetail
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'



class AboutPageView(TemplateView):
    # context_object_name = 'About_page'
    # model = RestaurantDetail
    template_name = 'pages/about.html'
    extra_context={'About_page': RestaurantDetail.objects.all()}





class GalleryPageView(ListView):
    context_object_name = 'Gallery_list' # for rememebering the name of object_list which we will use in templates
    model = Gallery
    template_name = 'pages/gallery.html'


class MenuPageView(ListView):
    context_object_name = 'FoodMenu_list' # for rememebering the name of object_list which we will use in templates
    model = FoodMenu
    template_name = 'pages/menu.html'
