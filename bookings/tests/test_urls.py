from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bookings.views import create_booking, update_booking, cancel_booking, booking_list


class TestBookingUrls(SimpleTestCase):

    def test_create_booking_url(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func, create_booking)

    def test_update_booking_url(self):
        url = reverse('update_booking', args=[1])
        self.assertEqual(resolve(url).func, update_booking)

    def test_cancel_booking_url(self):
        url = reverse('cancel_booking', args=[1])
        self.assertEqual(resolve(url).func, cancel_booking)

    def test_booking_list_url(self):
        url = reverse('booking_list')
        self.assertEqual(resolve(url).func, booking_list)
