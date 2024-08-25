from django.db import models

# Create your models here.
class RestaurantInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_details = models.TextField()
    opening_hours = models.TextField()
    description = models.TextField(blank=True)
    about_us = models.TextField(blank=True)

    def __str__(self):
        return self.name
