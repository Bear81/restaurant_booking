from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_booking, name='create_booking'),
    path('update/<int:pk>/', views.update_booking, name='update_booking'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
    path('list/', views.booking_list, name='booking_list'),
]
