import os
from enum import Enum
from functools import cached_property
from dataclasses import dataclass, field

from energinetml.settings import (
    DEFAULT_LOCATION,
    PACKAGE_NAME,
    PACKAGE_VERSION,
)

from .configurable import Configurable
from .requirements import RequirementList
from .webapp import WsgiWebApp, AsgiWebApp
from .templates import ASGIWebAppTemplates, WSGIWebAppTemplates


@dataclass
class Project(Configurable):
    """
    TODO
    """
    CONFIG_FILE_NAME = 'project.json'
    REQUIREMENTS_FILE_NAME = 'requirements.txt'

    @classmethod
    def create(cls, *args, **kwargs):
        """
        :rtype: Project
        """
        project = super(Project, cls).create(*args, **kwargs)

        # Create requirements.txt file
        with open(project.requirements_file_path, 'w') as f:
            f.write('%s==%s\n' % (PACKAGE_NAME, PACKAGE_VERSION))

        return project

    @property
    def requirements_file_path(self):
        """
        Absolute path to requirements.txt file.

        :rtype: str
        """
        return self.get_file_path(self.REQUIREMENTS_FILE_NAME)

    @cached_property
    def requirements(self):
        """
        Returns a list of project requirements from requirements.txt.

        :rtype: RequirementList
        """
        if os.path.isfile(self.requirements_file_path):
            return RequirementList.from_file(self.requirements_file_path)
        else:
            return RequirementList()


# -- Machine Learning --------------------------------------------------------


@dataclass
class MachineLearningProject(Project):
    name: str
    subscription_id: str
    resource_group: str
    workspace_name: str
    vnet_name: str
    subnet_name: str
    location: str = field(default=DEFAULT_LOCATION)

    @property
    def vnet_resourcegroup_name(self):
        """
        The resource group where the VNET is located, typically
        the same as the workspace.
        """
        return self.resource_group

    def default_model_path(self, model_name):
        """
        Returns default absolute path to folder where new models
        should be created at.

        :param str model_name:
        :rtype: str
        """
        return self.get_file_path(model_name)


# -- Web Apps ----------------------------------------------------------------


class WebAppProjectKind(str, Enum):
    ASGI = 'ASGI'
    WSGI = 'WSGI'


@dataclass
class WebAppProject(Project):
    name: str
    kind: WebAppProjectKind

    RESOLVERS = {
        WebAppProjectKind.ASGI: ASGIWebAppTemplates(),
        WebAppProjectKind.WSGI: WSGIWebAppTemplates(),
    }

    ENGINES = {
        WebAppProjectKind.ASGI: AsgiWebApp(),
        WebAppProjectKind.WSGI: WsgiWebApp(),
    }

    def get_template_resolver(self):
        """
        :rtype: energinetml.core.templates.WebAppTemplateResolver
        """
        if self.kind in self.RESOLVERS:
            return self.RESOLVERS[self.kind]
        raise RuntimeError

    def get_engine(self):
        """
        :rtype: energinetml.core.webapp.WebAppEngine
        """
        if self.kind in self.ENGINES:
            return self.ENGINES[self.kind]
        raise RuntimeError

    @property
    def dockerfile_path(self):
        """
        :rtype: str
        """
        return os.path.join(self.path, 'Dockerfile')
