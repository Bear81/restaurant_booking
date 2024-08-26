from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('menus/', views.menus, name='menus'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
]
