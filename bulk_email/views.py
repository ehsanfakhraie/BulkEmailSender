from django.http import Http404
from django.shortcuts import render
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

from email_service import methods

# Create your views here.
from bulk_email.models import Receiver


def send_mail(request, pk):
    receiver = Receiver.objects.get(pk=pk)
    subject, to = 'چالش', receiver.email

    html_content = render_to_string('emails/template_1.html', {'name': receiver.name,
                                                               'publication': receiver.publication})  # render with dynamic value
    if 'send' in request.POST:
        methods.send_mail(subject, to, html_content)
    else:
        return render(request, 'chooser.html', {'html_content': html_content})
