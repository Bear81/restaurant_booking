from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from bookings.models import Table, Booking


class TableModelTest(TestCase):

    def test_table_creation(self):
        table = Table.objects.create(table_number='1', capacity=4)
        self.assertEqual(table.table_number, '1')
        self.assertEqual(table.capacity, 4)
        self.assertTrue(isinstance(table, Table))
        self.assertEqual(str(table), 'Table 1 (Capacity: 4)')

    def test_table_number_unique(self):
        Table.objects.create(table_number='1', capacity=4)
        with self.assertRaises(Exception):
            # Should raise an error due to unique constraint
            Table.objects.create(table_number='1', capacity=6)


class BookingModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.table = Table.objects.create(table_number='1', capacity=4)

    def test_booking_creation(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='pending',
            special_requests='Window seat'
        )
        self.assertEqual(booking.user, self.user)
        self.assertEqual(booking.table, self.table)
        self.assertEqual(booking.number_of_guests, 2)
        self.assertEqual(booking.status, 'pending')
        self.assertEqual(
            str(booking), f"Booking for {self.user} on {booking.booking_datetime}")

    def test_status_choices(self):
        booking = Booking.objects.create(
            user=self.user,
            table=self.table,
            booking_datetime=timezone.now(),
            number_of_guests=2,
            status='confirmed'
        )
        self.assertEqual(booking.status, 'confirmed')

        with self.assertRaises(Exception):
            Booking.objects.create(
                user=self.user,
                table=self.table,
                booking_datetime=timezone.now(),
                number_of_guests=2,
                status='invalid_status'
            )  # Should raise an error because 'invalid_status' is not in STATUS_CHOICES
