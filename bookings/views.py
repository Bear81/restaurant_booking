from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking, Table
from website.forms import BookingForm
from django.contrib import messages


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            # Get combined datetime from cleaned form data
            booking.booking_datetime = form.cleaned_data['booking_datetime']
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking created successfully!")
            return redirect('booking_list')  # or 'profile' or wherever you send users
        else:
            messages.error(request, "There was a problem with your booking.")
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form, 'booking': None})


@login_required
def update_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            booking.booking_datetime = form.cleaned_data['booking_datetime']
            booking.number_of_guests = form.cleaned_data['number_of_guests']
            booking.special_requests = form.cleaned_data['special_requests']
            booking.status = 'pending'  # reset status after edit
            booking.save()
            messages.success(request, "Booking updated successfully!")
            return redirect('booking_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = BookingForm(instance=booking)

    return render(request, 'bookings/booking_form.html', {'form': form, 'booking': booking})



@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    booking.status = 'cancelled'
    booking.save()
    return redirect('profile')


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

