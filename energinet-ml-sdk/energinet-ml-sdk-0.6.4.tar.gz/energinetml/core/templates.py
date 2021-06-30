import os
import sys
import tempfile
import subprocess
from jinja2 import Template

from energinetml.settings import (
    TEMPLATES_GIT_URL,
    TEMPLATES_SUBNET_WHITELIST,
    TEMPLATES_IP_WHITELIST,
)


class TemplateResolver(object):
    """
    TODO
    """

    class TemplateResolverError(Exception):
        """
        TODO
        """
        pass

    def get_default_env(self):
        """
        :rtype: typing.Dict[str, typing.Any]
        """
        return {}

    def clone_and_render(self, project_root_path, files, env):
        """
        Clones Git repository and renders templates using the provided
        environment variables.

        'files' parameter is an iterable of (src, dst) where 'src' is file path
        relative to Git repository root, and 'dst' is file path relative
        to project root.

        :param str project_root_path:
        :param typing.Iterable[typing.Tuple[str, str]] files:
        :param typing.Dict[str, typing.Any] env:
        """
        actual_env = self.get_default_env()
        actual_env.update(env)

        with tempfile.TemporaryDirectory() as clone_path:
            self.clone(clone_path)

            for src, dst in files:
                self.render(
                    src=os.path.join(clone_path, src),
                    dst=os.path.join(project_root_path, dst),
                    env=actual_env,
                )

    def clone(self, clone_path):
        """
        :param str clone_path:
        """
        try:
            subprocess.check_call(
                # args=['git', 'clone', TEMPLATES_GIT_URL, clone_path],
                args=['git', 'clone', '--single-branch', '--branch', 'webapp', TEMPLATES_GIT_URL, clone_path],  # noqa: E501
                stdout=sys.stdout,
                stderr=subprocess.STDOUT,
            )
        except subprocess.CalledProcessError:
            raise self.TemplateResolverError(
                'Failed to clone Git repo: %s' % TEMPLATES_GIT_URL)

    def render(self, src, dst, env):
        """
        Renders Jinja2 template file at 'src' and writes it to 'dst' using the
        provided environment variables. Creates directories if necessary.

        :param str src:
        :param str dst:
        :param typing.Dict[str, str] env:
        """
        dst_folder = os.path.split(dst)[0]

        with open(src) as f:
            template = Template(f.read())
            rendered = template.render(**env)

        if not os.path.isdir(dst_folder):
            os.makedirs(dst_folder)

        with open(dst, 'w') as f:
            f.write(rendered)


class DataSciencePlatformTemplates(TemplateResolver):
    """
    Templates specific for Data Science Platform.
    """
    def get_default_env(self):
        """
        :rtype: typing.Dict[str, typing.Any]
        """
        return {
            'subnetWhitelist': TEMPLATES_SUBNET_WHITELIST,
            'ipWhitelist': TEMPLATES_IP_WHITELIST,
        }

    def resolve(self, project_root_path, project_name,
                service_connection, resource_group):
        """
        :param str project_root_path:
        :param str project_name:
        :param str service_connection: DevOps Service Connection for
            deploying to resource group
        :param str resource_group: Azure Resource Group to deploy webapp to
        """
        files = (
            ('.gitignore', '.gitignore'),
            (
                os.path.join('.azuredevops', 'infrastructure.yml'),
                os.path.join('.azuredevops', 'infrastructure.yml'),
            ),
            (
                os.path.join('terraform', 'datascienceplatform', 'dev', 'main.tf'),
                os.path.join('terraform', 'dev', 'datascienceplatform.tf'),
            ),
        )

        env = {
            'serviceConnection': service_connection,
            'resourceGroup': resource_group,
            'projectName': project_name,
        }

        self.clone_and_render(
            project_root_path=project_root_path,
            files=files,
            env=env,
        )


class WebAppTemplateResolver(TemplateResolver):
    """
    Templates specific for Web Apps.
    """
    def resolve_web_app(self, project_root_path, kind, env):
        """
        :param str project_root_path:
        :param str kind:
        :param typing.Dict[str, typing.Any] env:
        """
        files = (
            ('.gitignore', '.gitignore'),
            (
                os.path.join('.azuredevops', 'infrastructure.yml'),
                os.path.join('.azuredevops', 'infrastructure.yml'),
            ),
            (
                os.path.join('.azuredevops', 'deploy-webapp.yml'),
                os.path.join('.azuredevops', 'deploy.yml'),
            ),
            (
                os.path.join('webapp', 'terraform', 'dev', 'main.tf'),
                os.path.join('terraform', 'dev', 'webapp.tf'),
            ),
            (
                os.path.join('webapp', kind, 'Dockerfile'),
                os.path.join('Dockerfile'),
            ),
            (
                os.path.join('webapp', kind, 'src', 'app.py'),
                os.path.join('src', 'app.py'),
            ),
            (
                os.path.join('webapp', kind, 'src', '__init__.py'),
                os.path.join('src', '__init__.py'),
            ),
            (
                os.path.join('webapp', kind, 'src', 'requirements.txt'),
                os.path.join('src', 'requirements.txt'),
            ),
        )

        self.clone_and_render(
            project_root_path=project_root_path,
            files=files,
            env=env,
        )

    def resolve(self, project_root_path, project_name,
                service_connection, resource_group):
        raise NotImplementedError


class ASGIWebAppTemplates(WebAppTemplateResolver):
    """
    Templates specific for ASGI Web Apps.
    """
    def resolve(self, project_root_path, project_name,
                service_connection, resource_group):
        """
        :param str project_root_path:
        :param str project_name:
        :param str service_connection: DevOps Service Connection for
            deploying to resource group
        :param str resource_group: Azure Resource Group to deploy webapp to
        """
        self.resolve_web_app(
            project_root_path=project_root_path,
            kind='ASGI',
            env={
                'serviceConnection': service_connection,
                'resourceGroup': resource_group,
                'projectName': project_name,
            }
        )


class WSGIWebAppTemplates(WebAppTemplateResolver):
    """
    Templates specific for ASGI Web Apps.
    """
    def resolve(self, project_root_path, project_name,
                service_connection, resource_group):
        """
        :param str project_root_path:
        :param str project_name:
        :param str service_connection: DevOps Service Connection for
            deploying to resource group
        :param str resource_group: Azure Resource Group to deploy webapp to
        """
        self.resolve_web_app(
            project_root_path=project_root_path,
            kind='WSGI',
            env={
                'serviceConnection': service_connection,
                'resourceGroup': resource_group,
                'projectName': project_name,
            }
        )
