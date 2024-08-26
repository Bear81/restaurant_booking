from django.contrib import admin
from .models import Booking, Table

# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_datetime', 'table',
                    'number_of_guests', 'status')
    list_filter = ('status', 'booking_datetime', 'table')
    search_fields = ('user__username', 'table__table_number')
    ordering = ('-booking_datetime',)


admin.site.register(Booking, BookingAdmin)
admin.site.register(Table)
