
import os
import re
import jinja2
from jinja2 import meta
from shutil import rmtree
from pathlib import Path
from .constants import *
from .config import Config
from .providers import StoreProvider, ProviderManager
from .parameters import Parameters
from .secrets import Secrets
from .logger import Logger
from .utils import clean_directory, merge_dicts, deflatten_dict
from .exceptions import DSOException
from .stages import Stages

class TemplateProvider(StoreProvider):
    def list(self):
        raise NotImplementedError()

    def add(self, key, content, render_path):
        raise NotImplementedError()

    def delete(self, key, starts_with):
        raise NotImplementedError()

    def get(self, key):
        raise NotImplementedError()

class TemplatesClass():

    @property
    def default_render_path(self):
        return Config.working_dir

    def list(self):
        project = Config.project
        application = Config.application
        provider = ProviderManager.TemplateProvider()
        Logger.info(f"Start listing templates: project={project}, application={application}")
        return provider.list(project, application)

    def add(self, key, content, render_path):
        self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.TemplateProvider()
        if render_path:
            # if '..' in render_path:
            #     raise DSOException(MESSAGES['InvalidRenderPath'].format(render_path))
            if '**' in render_path:
                render_path = render_path.replace('**', os.path.dirname(key))
            if '*' in render_path:
                render_path = render_path.replace('*', os.path.basename(key))
            if not re.match('^[A-Za-z0-9._/$-]+$', render_path):
                raise DSOException(MESSAGES['InvalidRenderPath'].format(render_path))
            if render_path == '.' or render_path == './':
                render_path = os.path.join(self.default_render_path, key)
            if os.path.isdir(render_path):
                raise DSOException(MESSAGES['InvalidRenderPathExistingDir'].format(render_path))
            if os.path.isabs(render_path):
                Logger.warn(f"Render path {render_path} is not releative to the application root.")
        try:
            Logger.info(f"Start adding template: project={project}, application={application}, key={key}, render_path={render_path}")
            result = provider.add(project, application, key, content)
        finally:
            if os.path.abspath(render_path) == os.path.abspath(os.path.join(self.default_render_path, key)):
                Config.unregister_template_custom_render_path(key)
            else:
                Config.register_template_custom_render_path(key, render_path)
        return result

    def get(self, key):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.TemplateProvider()
        Logger.info(f"Start getting template: project={project}, application={application}, key={key}")
        return provider.get(project, application, key)

    def delete(self, key, recursive):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.TemplateProvider()
        Logger.info(f"Start deleting template: project={project}, application={application}, key={key}")
        try:
            result = provider.delete(project, application, key, recursive)
        finally:
            Config.unregister_template_custom_render_path(key)
        return result

    def validate_key(self, key):
        provider = ProviderManager.TemplateProvider()
        Logger.info("Start validating template key...")
        return provider.validate_key(key)

    def render(self, stage, limit=''):
        project = Config.project
        application = Config.application
        Logger.info(f"Start rendering templates: project={project}, application={application}, stage={Stages.shorten(stage)}")

        if Stages.is_default(stage):
            Logger.warn("No stage has been provided for rendering templates, using 'default'.")

        Logger.info(MESSAGES['LoadingParameters'])
        parameters = Parameters.list(stage, uninherited=False)

        merged = deflatten_dict({x['Key']: x['Value'] for x in parameters['Parameters']})

        Logger.info(MESSAGES['LoadingSecrets'])
        secrets = Secrets.list(stage, uninherited=False, decrypt=True)

        Logger.info(MESSAGES['MerginParameters'])
        merge_dicts(deflatten_dict({x['Key']: x['Value'] for x in secrets['Secrets']}), merged)

        provider = ProviderManager.TemplateProvider()
        Logger.info(MESSAGES['LoadingTemplates'])
        templates = provider.list(project, application)
        renderPaths = Config.get_template_render_path()

        jinja_env = jinja2.Environment(undefined=jinja2.StrictUndefined)

        Logger.info(MESSAGES['RenderingTemplates'])
        rendered = []
        for item in templates:
            key = item['Key']

            if not key.startswith(limit): continue

            template = provider.get(project, application, key)
            Logger.debug(f"Rendering template: key={key}")
            try:
                template = jinja_env.from_string(template)
            except:
                Logger.error(f"Failed to load template: {key}")
                raise
            # undeclaredParams = jinja2.meta.find_undeclared_variables(env.parse(template))
            # if len(undeclaredParams) > 0:
            #     Logger.warn(f"Undecalared parameter(s) found:\n{set(undeclaredParams)}")
            try:
                renderedContent = template.render(merged)
            except:
                Logger.error(f"Failed to render template: {key}")
                raise

            if key in renderPaths:
                renderPath = renderPaths[key]
            else:
                renderPath = os.path.join(self.default_render_path, key)

            if not (renderPath == '.' or renderPath.startswith(f'.{os.sep}')):
                renderPath = os.path.join('./', renderPath)

            # outputFilePath = os.path.join(renderPath, key)
            # outputFilePath = os.path.join(renderPath, key)
            if os.path.dirname(renderPath):
                os.makedirs(os.path.dirname(renderPath), exist_ok=True)
            with open(renderPath, 'w', encoding='utf-8') as f:
                f.write(renderedContent)
            
            rendered.append(renderPath)

        return rendered


Templates = TemplatesClass()