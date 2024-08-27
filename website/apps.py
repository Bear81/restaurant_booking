from django.apps import AppConfig
from django.contrib import admin


class WebsiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'website'

    def ready(self):
        admin.site.site_header = "Restaurant Booking Admin"
        admin.site.site_title = "Restaurant Booking Admin Portal"
        admin.site.index_title = "Welcome to the Restaurant Booking Management"
