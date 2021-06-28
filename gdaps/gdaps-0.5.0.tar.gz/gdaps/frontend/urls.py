import os
from logging import getLogger

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.urls import path
from django.views.generic import TemplateView
from gdaps.frontend.conf import frontend_settings
from gdaps.frontend.api import current_engine

logger = getLogger(__file__)

try:
    template_name = get_template(current_engine().base_template).template.name
    root_urlpatterns = [
        path(
            "",
            TemplateView.as_view(template_name=template_name),
            name="app",
        )
        # path("", TemplateView.as_view(template_name="gdaps/application.html"), name="app")
    ]
    logger.critical(f"Using template {template_name} as Vue entry point loader")

except TemplateDoesNotExist:
    logger.critical(
        f" ✘ Template '{current_engine().base_template}' does not exist. Please create a template at this place for GDAPS to work properly."
    )
except TypeError:  # no template found, .name not applicable then
    logger.critical(
        f" ✘ Error while searching for '{current_engine().base_template}' template."
    )
