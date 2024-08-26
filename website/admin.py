from django.contrib import admin
from .models import WebsiteImage

# Register your models here.


@admin.register(WebsiteImage)
class WebsiteImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_url')
    search_fields = ('name', 'category')
