from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


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
