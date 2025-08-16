from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website import views as website_views
from bookings import views as bookings_views

class WebsiteUrlTests(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, website_views.home)

    def test_about_us_url_resolves(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func, website_views.about_us)

    def test_contact_us_url_resolves(self):
        url = reverse('contact_us')
        self.assertEqual(resolve(url).func, website_views.contact_us)

    def test_menu_list_url_resolves(self):
        url = reverse('menu_list')
        self.assertEqual(resolve(url).func, website_views.menu_list)

    def test_menu_detail_url_resolves(self):
        url = reverse('menu_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, website_views.menu_detail)

class BookingUrlTests(SimpleTestCase):
    def test_create_booking_url_resolves(self):
        url = reverse('create_booking')
        self.assertEqual(resolve(url).func, bookings_views.create_booking)

    def test_update_booking_url_resolves(self):
        url = reverse('update_booking', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, bookings_views.update_booking)

    def test_cancel_booking_url_resolves(self):
        url = reverse('cancel_booking', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, bookings_views.cancel_booking)

    def test_booking_list_url_resolves(self):
        url = reverse('booking_list')
        self.assertEqual(resolve(url).func, bookings_views.booking_list)
