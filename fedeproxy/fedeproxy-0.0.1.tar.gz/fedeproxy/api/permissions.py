from allauth.socialaccount import models
from django.conf import settings
from rest_framework import permissions

from fedeproxy.common.gitlab import GitLab


#
# The only justification for making this function instead of using the method is
# for testing purposes. It is really difficult to mock the IsFedeproxyGroupMember.has_permission
# because the contet in which IsFedeproxyGroupMember is instantiated is hard to predict.
#
def has_permission(request, view):
    account = models.SocialAccount.objects.get(user=request.user)
    social_token = models.SocialToken.objects.get(account=account)
    gitlab = GitLab(settings.FEDEPROXY_GITLAB_URL)
    gitlab.set_token(social_token.token)
    return gitlab.is_self_member_of_group("fedeproxy")


class IsFedeproxyGroupMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return has_permission(request, view)
