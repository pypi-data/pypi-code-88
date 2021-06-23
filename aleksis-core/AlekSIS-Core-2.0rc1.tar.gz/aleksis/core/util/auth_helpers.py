"""Helpers/overrides for django-allauth."""

from django.conf import settings
from django.http import HttpRequest

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from oauth2_provider.oauth2_validators import OAuth2Validator

from .core_helpers import get_site_preferences, has_person


class OurSocialAccountAdapter(DefaultSocialAccountAdapter):
    """Customised adapter that recognises other authentication mechanisms."""

    def validate_disconnect(self, account, accounts):
        """Validate whether or not the socialaccount account can be safely disconnected.

        Honours other authentication backends, i.e. ignores unusable passwords if LDAP is used.
        """
        if "django_auth_ldap.backend.LDAPBackend" in settings.AUTHENTICATION_BACKENDS:
            # Ignore upstream validation error as we do not need a usable password
            return None

        # Let upstream decide whether we can disconnect or not
        return super().validate_disconnect(account, accounts)


class OurAccountAdapter(DefaultAccountAdapter):
    """Customised adapter to allow to disable signup."""

    def is_open_for_signup(self, request):
        return get_site_preferences()["auth__signup_enabled"]


class CustomOAuth2Validator(OAuth2Validator):
    def get_additional_claims(self, request):
        django_request = HttpRequest()
        django_request.META = request.headers

        claims = {
            "preferred_username": request.user.username,
        }

        if "profile" in request.scopes:
            if has_person(request.user):
                claims["given_name"] = request.user.person.first_name
                claims["family_name"] = request.user.person.last_name
                claims["profile"] = django_request.build_absolute_uri(
                    request.user.person.get_absolute_url()
                )
                if request.user.person.photo:
                    claims["picture"] = django_request.build_absolute_uri(
                        request.user.person.photo.url
                    )
            else:
                claims["given_name"] = request.user.first_name
                claims["family_name"] = request.user.last_name

        if "email" in request.scopes:
            if has_person(request.user):
                claims["email"] = request.user.person.email
            else:
                claims["email"] = request.user.email

        if "address" in request.scopes and has_person(request.user):
            claims["address"] = {
                "street_address": request.user.person.street
                + " "
                + request.user.person.housenumber,
                "locality": request.user.person.place,
                "postal_code": request.user.person.postal_code,
            }

        return claims
