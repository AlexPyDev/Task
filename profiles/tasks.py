from django.conf import settings

import requests
from celery import shared_task


@shared_task
def send_email_confirmation(recipient_mail, text):
    mail_subject = 'Account activation.'
    sender = getattr(settings, 'EMAIL_HOST_USER', None)
    r = requests.post(
        "https://api.mailgun.net/v3/sandbox4dcc7b1a3b0e4018bde85dd3592b0dfa.mailgun.org/messages",
        auth=("api", "3378ab16e772dd57a0f6be1fe4703ac3-2dfb0afe-25ec1a66"),
        data={"from": f"TestTask robot <{sender}>",
              "to": [recipient_mail],
              "subject": mail_subject,
              "text": text})
    print(r.json())
    return
