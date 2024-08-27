from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import home, about_us, contact_us, menu_list, menu_detail


class TestWebsiteUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_about_us_url(self):
        url = reverse('about_us')
        self.assertEqual(resolve(url).func, about_us)

    def test_contact_us_url(self):
        url = reverse('contact_us')
        self.assertEqual(resolve(url).func, contact_us)

    def test_menu_list_url(self):
        url = reverse('menu_list')
        self.assertEqual(resolve(url).func, menu_list)

    def test_menu_detail_url(self):
        # Test with an example primary key
        url = reverse('menu_detail', args=[1])
        self.assertEqual(resolve(url).func, menu_detail)
