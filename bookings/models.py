from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    table = models.OneToOneField('Table', on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField()
    number_of_guests = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), (
        'confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='pending')
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return f"Booking for {self.user} on {self.booking_datetime}"


class Table(models.Model):
    table_number = models.CharField(max_length='10', unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
