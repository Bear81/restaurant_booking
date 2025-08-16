from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Booking, Table
from datetime import datetime

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.table = Table.objects.create(table_number='A1', capacity=4)
        self.booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=datetime(2030, 1, 1, 19, 0),
            number_of_guests=2,
            status='pending',
            special_requests='Test view'
        )

    def test_profile_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_profile_logged_in(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
