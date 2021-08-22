from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ View to send an email to site owners from contact form submissions """
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
