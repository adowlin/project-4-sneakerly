from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Booking


@login_required
def profile(request):
    """ Display user's profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    bookings = profile.bookings.all()

    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)

        profile_data = {
            'default_full_name': request.POST['default_full_name'],
            'default_phone_number': request.POST['default_phone_number'],
            'default_postcode': request.POST['default_postcode'],
            'default_town_or_city': request.POST['default_town_or_city'],
            'default_street_address1': request.POST[
                'default_street_address1'],
            'default_street_address2': request.POST[
                'default_street_address2'],
            'default_county': request.POST['default_county'],
        }
        form = UserProfileForm(profile_data, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information Updated Successfully!!')
    else:
        try:
            profile_data = {
                'full_name': profile.default_full_name,
                'email': profile.user.email,
                'phone_number': profile.default_phone_number,
                'postcode': profile.default_postcode,
                'town_or_city': profile.default_town_or_city,
                'street_address1': profile.default_street_address1,
                'street_address2': profile.default_street_address2,
                'county': profile.default_county,
            }
            form = UserProfileForm(initial=profile_data, instance=profile)
        except UserProfile.DoesNotExist:
            form = UserProfileForm(instance=profile)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)


@login_required
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
