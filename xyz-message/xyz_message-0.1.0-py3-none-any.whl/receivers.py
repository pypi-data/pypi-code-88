# -*- coding:utf-8 -*-
from django.dispatch import receiver
from django.db.models.signals import post_save
from . import models, helper

@receiver(post_save, sender=models.Task)
def send_message_at_once(sender, **kwargs):
    task = kwargs.get('instance')
    if task.send_time is None and not task.is_sent:
        task.send()

