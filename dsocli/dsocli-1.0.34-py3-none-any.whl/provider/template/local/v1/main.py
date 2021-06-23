import os
import re
import yaml
import json
import glob
from pathlib import Path
import jinja2
from dsocli.logger import Logger
from dsocli.config import Config
from dsocli.providers import ProviderManager
from dsocli.templates import Templates, TemplateProvider
from dsocli.stages import Stages
from dsocli.constants import *
from dsocli.exceptions import DSOException


settings = {
    'templates_dir' : '{0}/templates'.format(Config.config_dir),
}

default_spec = {
}


class LocalTemplateProvider(TemplateProvider):
    def __init__(self):
        super().__init__('template/local/v1')

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

    @property
    def templates_root_path(self):
        return f"{Config.working_dir}/{settings['templates_dir']}"

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

    def get_key_validator(self):
        return r"^[a-zA-Z0-9_-]+(/[a-zA-Z0-9_-]+)*(.[a-zA-Z0-9_-]+)?$"

###--------------------------------------------------------------------------------------------

    def add(self, project, application, key, content):
        path = f"{self.templates_root_path}/{key}"
        os.makedirs(os.path.dirname(path), exist_ok=True)
        Logger.debug(f"Adding template: path={path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        return key

###--------------------------------------------------------------------------------------------

    def list(self, project, application):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.templates_root_path, encoding='utf-8'))
        templatesKeys = env.list_templates()
        renderPaths = Config.get_template_render_path()
        result = []
        renderBasePath = Templates.default_render_path
        for key in templatesKeys:
            if key in renderPaths:
                renderPath = renderPaths[key]
                if not (renderPath == '.' or renderPath.startswith(f'.{os.sep}')):
                    renderPath = os.path.join('./', renderPath)
            else:
                renderPath = os.path.join(renderBasePath, key)
            result.append({'Key': key, 'RenderTo': renderPath})

        return result

###--------------------------------------------------------------------------------------------

    def get(self,  project, application, key):
        path = f"{self.templates_root_path}/{key}"
        if not os.path.exists(path):
            raise DSOException(MESSAGES['TemplateNotFound'].format(key))
        Logger.debug(f"Getting template: path={path}")
        with open(path, 'r', encoding='utf-8') as f:
            result = f.read()
        return result

###--------------------------------------------------------------------------------------------

    def delete(self, project, application, key, recursive):
        result = []
        # m = re.match(r'^.*?([*][*/*|*/**]*)$', key)
        # globe = ''
        # if m:
        #     globe = m.groups()[0]
        #     key = key[:-len(globe)]
        path = f"{self.templates_root_path}/{key}"
        path = re.sub('^./', '', path)
        # if globe:
        #     path = './.dso/templates'
        #     globe = 'res*'
            # templates = Path(path).glob(globe)
        # if True:
        #     templates = glob.glob(path, recursive=True)
        #     print(templates)
        #     for item in templates:
        #         if not Path(item).is_file(): continue
        #         Logger.debug(f"Deleting template: path={str(item)}")
        #         os.remove(str(item))
        #         result.append(str(item)[len(re.sub('^./', '', self.templates_root_path))+1:])
        #     if not len(result):
        #         raise DSOException(f"No template found matching '{key}{globe}'.")
        # else:
        #     if not os.path.exists(path) or os.path.isdir(path):
        #         raise DSOException(MESSAGES['TemplateNotFound'].format(key))
        #     Logger.debug(f"Deleting template: path={path}")
        #     os.remove(path)
        #     result.append(path[len(re.sub('^./', '', self.templates_root_path))+1:])
        # return result
        # if '*' in key:
        #     if not (re.match(r'^.*?([*][*/*]?)+', key) or re.match(r'^.*?(.*)+$', key)):
        #         raise DSOException(f"No template found matching '{key}'.")
        for item in glob.glob(path, recursive=recursive):
            if not Path(item).is_file(): continue
            Logger.debug(f"Deleting template: path={str(item)}")
            os.remove(str(item))
            result.append(str(item)[len(re.sub('^./', '', self.templates_root_path))+1:])
        if not len(result):
            raise DSOException(f"No template found matching '{key}'.")
        return result

###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------
###--------------------------------------------------------------------------------------------

ProviderManager.register(LocalTemplateProvider())
