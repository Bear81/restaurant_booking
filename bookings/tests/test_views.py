from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from bookings.models import Booking, Table
from django.utils import timezone


class BookingViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.table = Table.objects.create(table_number='1', capacity=4)
        self.client.login(username='testuser', password='12345')

    def test_create_booking_get(self):
        response = self.client.get(reverse('create_booking'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_form.html')

    def test_create_booking_post(self):
        datetime_str = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'table': self.table.id,
            'booking_datetime': timezone.now(),
            'number_of_guests': 2,
            'status': 'pending',
            'special_requests': 'Window seat'
        }
        response = self.client.post(reverse('create_booking'), data)
        print(response.context['form'].errors) #Debug
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().user, self.user)

    def test_update_booking_get(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='pending'
        )
        response = self.client.get(
            reverse('update_booking', args=[booking.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_form.html')

    def test_update_booking_post(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='pending'
        )
        datetime_str = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        data = {
            'table': self.table.id,
            'booking_datetime': datetime_str,
            'number_of_guests': 4,
            'status': 'confirmed',
            'special_requests': 'Near the window'
        }
        response = self.client.post(
            reverse('update_booking', args=[booking.pk]), data)
        print(response.context['form'].errors)
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.number_of_guests, 4)
        self.assertEqual(booking.status, 'confirmed')

    def test_cancel_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='pending'
        )
        response = self.client.post(
            reverse('cancel_booking', args=[booking.pk]))
        self.assertEqual(response.status_code, 302)
        booking.refresh_from_db()
        self.assertEqual(booking.status, 'cancelled')

    def test_booking_list(self):
        Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='pending'
        )
        response = self.client.get(reverse('booking_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking_list.html')
        self.assertEqual(len(response.context['bookings']), 1)
