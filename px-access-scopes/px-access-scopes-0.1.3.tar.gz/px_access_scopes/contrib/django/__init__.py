"""Django application for a little bit easier access scopes integration.
"""

from .scopes import *
from .aggregates import *

default_app_config = 'px_access_scopes.contrib.django.apps.AccessScopesConfig'
