import logging

from authlib.integrations.base_client import MismatchingStateError
from authlib.integrations.django_client import OAuth
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
from django.shortcuts import redirect

from .apps import APP_NAME
from .user_utils import user_from_claims

logger = logging.getLogger(__name__)

oauth = OAuth()
oauth.register(name="identity_provider")


def authenticate(request):
    redirect_uri = request.build_absolute_uri(reverse(f"{APP_NAME}:oidc-callback"))
    return oauth.identity_provider.authorize_redirect(request, redirect_uri)


def callback(request):
    try:
        token = oauth.identity_provider.authorize_access_token(request)
        userinfo = oauth.identity_provider.userinfo(token=token)
        user = user_from_claims(username_claim="preferred_username", claims=userinfo)
        if user is not None:
            auth.login(
                request, user, backend="django.contrib.auth.backends.ModelBackend"
            )
        return redirect(settings.LOGIN_REDIRECT_URL)
    except MismatchingStateError as e:
        logger.warning(
            "User likely tried to login using a URL including an expired session (in a bookmark). "
            "Details: %s",
            e,
            exc_info=True,
        )
        return redirect(settings.LOGIN_REDIRECT_URL)


def logout(request):
    auth.logout(request)
    provider_logout_endpoint = oauth.identity_provider.server_metadata.get(
        "end_session_endpoint"
    )
    return redirect(
        "{}?redirect_uri={}".format(
            provider_logout_endpoint,
            request.build_absolute_uri(settings.LOGOUT_REDIRECT_URL),
        )
        if provider_logout_endpoint
        else settings.LOGOUT_REDIRECT_URL
    )
