from django.test import TestCase
from django.contrib.auth.models import User
from bookings.models import Booking, Table
from datetime import datetime

class TestBookingModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.table = Table.objects.create(table_number='A1', capacity=4)
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=datetime(2030, 1, 1, 19, 0),
            number_of_guests=2,
            special_requests='Window seat'
        )

    def test_str_method(self):
        expected = f"Booking for {self.user} on {self.booking.booking_datetime}"
        self.assertEqual(str(self.booking), expected)
