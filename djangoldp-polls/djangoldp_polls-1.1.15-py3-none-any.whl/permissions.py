from djangoldp.permissions import LDPPermissions
from djangoldp.utils import is_authenticated_user
from djangoldp_polls.filters import PollFilterBackend

class VotePermissions(LDPPermissions):
	
	def get_object_permissions(self, request, view, obj):
		perms = super().get_object_permissions(request, view, obj)

		return perms


	def get_container_permissions(self, request, view, obj=None):
		perms = super().get_container_permissions(request, view, obj)

		return perms


class PollPermissions(LDPPermissions):
	with_cache = False
	filter_backends = [PollFilterBackend]

	def get_container_permissions(self, request, view, obj=None):
		perms = super().get_container_permissions(request, view, obj)

		if obj is None:
			return perms

        # Remove add to user who already voted
		from .models import Vote
		if 'add' in perms and obj is not None:
			if is_authenticated_user(request.user) and Vote.objects.filter(relatedPoll=obj.pk, user=request.user).exists():
				perms.remove('add')

		return perms