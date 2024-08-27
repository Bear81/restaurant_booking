from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import WebsiteImage, MenuPost, RestaurantInfo

# Register your models here.


class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_details', 'opening_hours')


admin.site.register(RestaurantInfo, RestaurantInfoAdmin)


@admin.register(WebsiteImage)
class WebsiteImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_url')
    search_fields = ('name', 'category')


@admin.register(MenuPost)
class MenuPostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    summernote_fields = ('content',)
