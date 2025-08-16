from django.test import TestCase
from django.contrib.auth.models import User
from bookings.models import Table
from website.forms import BookingForm

class TestBookingForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.table = Table.objects.create(table_number='A1', capacity=4)

    def test_form_missing_required_fields(self):
        form = BookingForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('user', form.errors)
        self.assertIn('booking_datetime', form.errors)
        self.assertIn('number_of_guests', form.errors)
