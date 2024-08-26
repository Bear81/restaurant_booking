from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('booking-confirmation/', views.booking_confirmation,
         name='booking_confirmation'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/<int:pk>/', views.menu_detail, name='menu_detail'),
]
