from celery import shared_task
from django.core.mail import EmailMessage

from .utils import slack_send_message


@shared_task()
def send_mail_task(email, subject, message):
    msg = EmailMessage(subject=subject, body=message, bcc=[email])
    msg.content_subtype = "html"
    return msg.send()


@shared_task()
def send_message_slack_task(channel: str, message: str, id_user: str = ''):
    '''
    send messages slack
    :param channel: channel for send
    :param message: message send
    :param id_user: id user slack
    :return: (str) response
    '''
    res = slack_send_message(channel,message,id_user)
    return res