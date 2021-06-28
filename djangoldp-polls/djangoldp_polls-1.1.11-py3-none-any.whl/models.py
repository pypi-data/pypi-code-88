from django.conf import settings
from django.db import models, transaction
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.http import Http404
from rest_framework import serializers
import functools
from django.utils.timezone import localdate, timedelta
from django.template import loader

from django.core.mail import send_mail
from djangoldp.models import Model
from djangoldp.views import LDPViewSet
from djangoldp_conversation.models import Conversation
from djangoldp_circle.models import Circle
from djangoldp_notification.models import Notification
from djangoldp.activities.services import ActivityQueueService

from djangoldp_polls.permissions import *

# User = settings.AUTH_USER_MODEL
# User.name=User.get_full_name

#========================

#========================

class Tag (Model):
	name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Name")

	class Meta(Model.Meta):
		serializer_fields = ['@id','name']
		anonymous_perms = ['view']
		authenticated_perms = ['inherit','add']
		rdf_type = 'sib:tag'

	def __str__(self):
		return self.name


class PollOption (Model):
	name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Options available for a vote")

	class Meta(Model.Meta):
		serializer_fields = ['@id','name']
		nested_fields = ['userVote','relatedPollOptions']
		anonymous_perms = ['view','add']
		authenticated_perms =  ['inherit','add','delete','change']
		rdf_type = 'sib:polloption'


	def __str__(self):
		return self.name

def onMonthLater():
	return localdate() + timedelta(days=30)



class Poll (Model):
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='createdVotes', null=True, blank=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=250,verbose_name="Title", null=True, blank=True)
	image = models.URLField(verbose_name="Illustration", default="https://unpkg.com/@startinblox/component-poll@2.1/img/defaultpoll.png", null=True, blank=True)
	hostingOrganisation = models.CharField(max_length=250,verbose_name="Name of the hosting organisation", null=True, blank=True)
	startDate = models.DateField(verbose_name="Start date", blank=True, null=True) 
	endDate = models.DateField(verbose_name="End data", default=onMonthLater, null=True, blank=True)
	shortDescription = models.CharField(max_length=250,verbose_name="Short description", null=True, blank=True)
	longDescription = models.TextField(verbose_name="Long description", null=True, blank=True)
	tags = models.ManyToManyField(Tag, related_name='polls', blank=True)
	pollOptions = models.ManyToManyField(PollOption, related_name='relatedPollOptions', blank=True)
	debate = models.ManyToManyField(Conversation, related_name='polls', blank=True)
	circle = models.ForeignKey(Circle, blank=True, null=True, related_name="polls", on_delete=models.SET_NULL)
	creationDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
	authorNotificationOnComment = models.BooleanField(default=True)

	class Meta(Model.Meta):
		auto_author = 'author'
		serializer_fields = ['@id','created_at','debate','pollOptions','votes','author','title','image','circle',\
												'hostingOrganisation','startDate','endDate','shortDescription','longDescription','tags', 'authorNotificationOnComment']
		nested_fields = ['tags','votes','pollOptions','debate','circle']
		anonymous_perms = ['view','add']
		authenticated_perms = ['inherit']
		owner_perms = ['inherit','change','delete']
		owner_field = 'author'
		permission_classes = [PollPermissions]
		rdf_type = 'sib:poll'

	def __str__(self):
		return self.title

# used to execute func after a DB transaction is commited
# https://docs.djangoproject.com/en/dev/topics/db/transactions/#django.db.transaction.on_commit
def on_transaction_commit(func):
	def inner(*args, **kwargs):
		transaction.on_commit(lambda: func(*args, **kwargs))
	return inner

@receiver(post_save, sender=Poll)
@on_transaction_commit
def post_create_poll(sender, instance, **kwargs):

	# pollOptions list to generate
	model = ['À reformuler', 'À discuter', 'Favorable', 'Très favorable']

	# verify if the options list is already correct
	if len(instance.pollOptions.all()) != len(model) or not functools.reduce(lambda x, y : x and y, map(lambda p, q: p.name == q,instance.pollOptions.all(),model), True):
		# if not, clear it and create the right ones
		instance.pollOptions.clear()
		for option in model:
			instance.pollOptions.add( PollOption.objects.create(name=option) )
		# save the new list (will re-enter this function but the check avoid infinite loop)
		instance.save()

# I know this shouldn't live here, but putting it in views results in circular dependency problems
# https://git.startinblox.com/djangoldp-packages/djangoldp/issues/278
class VoteViewSet(LDPViewSet):
	def is_safe_create(self, user, validated_data, *args, **kwargs):
		try:
			if 'poll' in validated_data.keys():
				poll = Poll.objects.get(urlid=validated_data['poll']['urlid'])
			else:
				poll = self.get_parent()

			if Vote.objects.filter(relatedPoll=poll, user=user).exists():
				raise serializers.ValidationError('You may only vote on this poll once!')

		except Poll.DoesNotExist:
			return True
		except (KeyError, AttributeError):
			raise Http404('circle not specified with urlid')

		return True


class Vote (Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='votes', null=True, blank=True, on_delete=models.SET_NULL)
	chosenOption =  models.ForeignKey(PollOption, related_name='userVote', null=True, blank=True, on_delete=models.CASCADE)
	relatedPoll = models.ForeignKey(Poll, related_name='votes', null=True, blank=True, on_delete=models.CASCADE)
	creationDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	class Meta(Model.Meta):
		auto_author = "user"
		serializer_fields = ['@id','chosenOption','relatedPoll']
		nested_fields = []
		permission_classes = [VotePermissions]
		anonymous_perms = ['view','add','change']
		authenticated_perms =  ['inherit','add','delete']
		view_set = VoteViewSet
		rdf_type = 'sib:vote'

	def __str__(self):
		return self.chosenOption.__str__()

@receiver(m2m_changed, sender=Poll.debate.through)
def send_notification(instance, action, **kwargs):
	if action != 'post_add':
		return

	poll = instance.polls.all()[0]
	if instance.author_user.urlid == poll.author.urlid:
		return

	if not poll.authorNotificationOnComment:
		return

	# local inbox
	if poll.author.urlid.startswith(settings.SITE_URL):
		Notification.objects.create(
			user=poll.author,
			object=poll.urlid,
			type="Poll_debate",
			author=instance.author_user.urlid,
			summary="A commenté votre proposition."
		)
	# external inbox
	else:
		json = {
			"@context": settings.LDP_RDF_CONTEXT,
			"object": poll.urlid,
			"type": "creation",
			"author": instance.author_user.urlid,
			"summary": "A commenté votre proposition.",
			"emailNotificationTemplate": "poll_debate"
		}
		ActivityQueueService.send_activity(poll.author.urlid, json)

	# Send email
	html_message = loader.render_to_string(
		'debate_notification.html',
		{
			'author': poll.author.first_name + ' ' + poll.author.last_name,
			'pollName': poll.title,
			'link': (getattr(settings, 'INSTANCE_DEFAULT_CLIENT', False) or settings.JABBER_DEFAULT_HOST),
			'content': instance.title
		}
	)

	if poll.author.settings.receiveMail:
		send_mail(
			'Vous avez une nouvelle notification sur la République de l’ESS !',
			'Vous avez une nouvelle notification sur la République de l’ESS !',
			(getattr(settings, 'EMAIL_HOST_USER', False) or "noreply@" + settings.JABBER_DEFAULT_HOST),
			[poll.author.email],
			fail_silently=True,
			html_message=html_message
		)