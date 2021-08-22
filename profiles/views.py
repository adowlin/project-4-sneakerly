from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Booking


def profile(request):
    """ Display user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    bookings = profile.bookings.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)


def booking_history(request, booking_number):
    booking = get_object_or_404(Booking, booking_number=booking_number)

    messages.info(request, (
        f'This is a past confirmation for order number {booking_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'booking': booking,
        'from_profile': True,
    }

    return render(request, template, context)
