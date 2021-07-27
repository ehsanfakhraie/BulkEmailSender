from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

from email_service.models import EmailLog


def send_mail(subject, to, html_content, text_content=None):
    text = text_content or strip_tags(html_content)

    msg = EmailMultiAlternatives(subject, text_content, to=[to])

    msg.attach_alternative(html_content, "text/html")
    msg.send()

    EmailLog.objects.create(to=to, subject=subject, body_text=text, body_html=html_content)
