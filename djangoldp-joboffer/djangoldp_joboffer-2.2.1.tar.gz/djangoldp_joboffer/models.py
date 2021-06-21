from django.conf import settings
from django.db import models
from djangoldp_conversation.models import Conversation

from djangoldp.models import Model
from djangoldp_skill.models import Skill

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import re

job_fields = ["@id", "author", "title", "description", "creationDate", "skills", "budget", "duration", "earnBusinessProviding", "closingDate", "conversation"]
if 'djangoldp_community' in settings.DJANGOLDP_PACKAGES:
    job_fields += ['community']


class JobOffer(Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='jobOffers', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    budget = models.CharField(max_length=255, blank=True, null=True)
    earnBusinessProviding = models.BooleanField(default=False)
    skills = models.ManyToManyField(Skill, blank=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    closingDate = models.DateField(null=True)
    conversation = models.ManyToManyField(Conversation, blank=True)

    class Meta:
        auto_author = 'author'
        owner_field = 'author'
        nested_fields = ["skills", "conversation"]
        anonymous_perms = ["view"]
        authenticated_perms = ["inherit", "add"]
        owner_perms = ["inherit", "change", "delete"]
        container_path = 'job-offers/'
        serializer_fields = job_fields
        rdf_type = 'hd:joboffer'

    def __str__(self):
        try:
            return '{} -> {} ({})'.format(self.author.urlid, self.title, self.urlid)
        except:
            return self.urlid


def to_text(html):
  return re.sub('[ \t]+', ' ', strip_tags(html)).replace('\n ', '\n').strip()


@receiver(post_save, sender=JobOffer)
def send_mail_to_fnk(instance, created, **kwargs):
    if created and instance.earnBusinessProviding:
        if getattr(settings, 'JOBOFFER_SEND_MAIL_BP', False):
            message_html = render_to_string('joboffer/email.html', {
                "instance": instance
            })
            send_mail(
                "Une nouvelle offre demande un apport d'affaire",
                to_text(message_html),
                (getattr(settings, 'DEFAULT_FROM_EMAIL', False)\
                    or getattr(settings, 'EMAIL_HOST_USER', False)\
                    or "noreply@" + settings.JABBER_DEFAULT_HOST),
                getattr(settings, 'JOBOFFER_SEND_MAIL_BP'),
                fail_silently = True,
                html_message = message_html
            )