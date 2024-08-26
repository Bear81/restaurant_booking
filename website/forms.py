from django import forms
from bookings.models import Booking


class BookingForm(forms.ModelForm):
    booking_datetime = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date', 'class': 'form-control'},
            time_attrs={'type': 'time', 'class': 'form-control'}
        )
    )

    class Meta:
        model = Booking
        fields = ['booking_datetime', 'number_of_guests', 'special_requests']
        
    def clean_booking_datetime(self):
        booking_datetime = self.cleaned_data.get('booking_datetime')
        if booking_datetime < timezone.now():
            raise forms.ValidationError(
                "The booking date and time cannot be in the past.")
        return booking_datetime
