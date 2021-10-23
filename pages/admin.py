from django.contrib import admin

from .models import FoodMenu, Gallery, HomepageMenu, RestaurantDetail
# Register your models here.


class HomepageMenuAdmin(admin.ModelAdmin):
    model = FoodMenu
    list_display = ['home_picture_first','title_first','home_picture_second','title_second','home_picture_third','title_third','foodmenu','title','price']

class FoodMenuAdmin(admin.ModelAdmin):
    model = FoodMenu
    list_display = ['foodmenu','title','price']



class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    list_display = ['GalleryPage','title']



class RestaurantDetailAdmin(admin.ModelAdmin):
    model = FoodMenu
    list_display = ['RestaurantName','LogoPicture','AboutPicture','TagLine','Discription','ContactNo','Email','Address']






admin.site.register(HomepageMenu, HomepageMenuAdmin)
admin.site.register(RestaurantDetail,RestaurantDetailAdmin)
admin.site.register(Gallery,GalleryAdmin)
