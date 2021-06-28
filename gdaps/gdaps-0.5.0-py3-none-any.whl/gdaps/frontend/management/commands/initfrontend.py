import logging
import os

import django
from django.conf import settings
from django.template import Context
from django.utils.version import get_docs_version

from gdaps.conf import gdaps_settings
from gdaps.frontend.api import current_engine
from gdaps.frontend.conf import frontend_settings
from gdaps.management.templates import TemplateCommand

# this imported is needed to auto-recognize the plugin,
# even if it's not used directly.

logger = logging.getLogger(__name__)


class Command(TemplateCommand):
    """This command creates a frontend from a boilerplate code."""

    help = "Initializes a Django GDAPS application with a frontend."

    def handle(self, *args, **options):
        super().handle(*args, **options)
        frontend_dir = frontend_settings.FRONTEND_DIR

        # create a frontend/ directory in the Django root
        self.target_path = os.path.abspath(
            (os.path.join(settings.BASE_DIR, frontend_dir))
        )

        self.rewrite_template_suffixes = current_engine().rewrite_template_suffixes

        current_engine().check_install_prereq()

        self.create_directory(self.target_path)

        # run initialisation of engine
        current_engine().initialize(frontend_dir)

        project_version = "0.0.1"

        self.context = Context(
            {
                **options,
                "project_name": settings.PROJECT_NAME,
                "project_version": project_version,
                "project_title": gdaps_settings.PROJECT_TITLE,
                "frontend_dir": frontend_dir,
                "frontend_path": self.target_path,
                "docs_version": get_docs_version(),
                "django_version": django.__version__,
            },
            autoescape=False,
        )

        # add template subdir per engine
        self.templates.append(current_engine().template_global)
        logger.debug(f"Added template dir {current_engine().template_global}")
        self.copy_templates()

        # maintain a frontend's plugins list with all found plugin's frontends
        current_engine().update_plugins_list()
        # build
        # subprocess.check_call(
        #     "npm run build --prefix {base_dir}/{plugin}/frontend".format(
        #         plugin=target, base_dir=settings.BASE_DIR
        #     ),
        #     shell=True,
        # )

        # ask the user to be sure to copy the static files
        # subprocess.check_call('./manage.py collectstatic'.format(plugin=target, base_dir=settings.BASE_DIR), shell=True)
