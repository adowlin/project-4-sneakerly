from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    """ View to send an email to site owners from contact form submissions """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New message {form.cleaned_data["email"]}: \
                {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(
                email_subject, email_message,
                settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            messages.success(
                request, "Message sent successfully! \
                    We'll respond via email soon.")
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
