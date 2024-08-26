from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, Table
from website.forms import BookingForm


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Optionally send confirmation email here
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})


@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # Optionally send confirmation email here
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_form.html', {'form': form})


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'rejected'  # Adjusted to match your model's status choices
    booking.save()
    # Optionally send cancellation email here
    return redirect('booking_list')


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_list.html', {'bookings': bookings})


def booking_confirmation(request):
    return render(request, 'bookings/booking_confirmation.html')
