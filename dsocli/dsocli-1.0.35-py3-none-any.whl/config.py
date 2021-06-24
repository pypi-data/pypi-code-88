
import yaml
import os
from .constants import *
from .logger import Logger
from .utils import *
from .version import __version__
from pathlib import Path
from .exceptions import DSOException
import imp
import sys

default_config = {
    'kind': 'dso/application/v1',
    'version': int(__version__.split('.')[0]),
    'project': 'default',
    'application': 'default',
    'parameter': {
        'provider': {
            'id': '',
            'spec': {}
        },
    },
    'secret': {
        'provider': {
            'id': '',
            'spec': {}
        },
    },
    'template': {
        'provider': {
            'id': '',
            'spec': {}
        },
        'render': {}
    }
}

class ConfigManager:
    @property
    def config_dir(self):
        return '.dso'

    @property
    def config_file(self):
        return 'dso.yml'

    @property
    def install_path(self):
        return os.path.dirname(os.path.abspath(__file__))
    
    working_dir = ''
    local_config = {}
    local_config_file_path = ''
    local_config_dir_path = ''
    global_config = {}
    global_config_file_path = ''
    global_config_dir_path = ''
    overriden_config = {}
    inherited_config = {}
    inherited_config_files = []
    merged_config = {}

    # def __init__(self):
    #     # path = os.path.join(os.path.expanduser("~"), self.config_dir, self.config_file)
    #     # if os.path.exists(path):
    #     #     self.__config = yaml.safe_load(open(path))

    def load_global_config(self):
        self.global_config_dir_path = os.path.join(Path.home(), self.config_dir)
        self.global_config_file_path = os.path.join(self.global_config_dir_path, self.config_file)

        if not os.path.exists(self.global_config_file_path):
            self.global_config = {}
            Logger.debug("Global DSO configuration not found.")
            return

        Logger.debug(f"Global DSO configuration found: path={self.global_config_file_path}")

        try:
            self.global_config = yaml.load(open(self.global_config_file_path, 'r', encoding='utf-8'), yaml.SafeLoader)
        except:
            raise DSOException(MESSAGES['InvalidDSOConfigurationFile'])

        self.update_merged_config()


    def load_local_config(self, show_warnings=True):
        self.local_config_dir_path = os.path.join(self.working_dir, self.config_dir)
        self.local_config_file_path = os.path.join(self.local_config_dir_path, self.config_file)

        if not os.path.exists(self.local_config_file_path):
            self.local_config = {}
            if show_warnings:
                Logger.warn(MESSAGES['NoDSOConfigFound'])
            return

        Logger.debug(f"Local DSO configuration found: path={self.local_config_file_path}")

        try:
            self.local_config = yaml.load(open(self.local_config_file_path, 'r', encoding='utf-8'), yaml.SafeLoader)
        except:
            raise DSOException(MESSAGES['InvalidDSOConfigurationFile'])

        self.update_merged_config()

    def load_inherited_config(self):

        for dir in Path(self.working_dir).resolve().parents:
            configFilePath = os.path.join(dir, self.config_dir, self.config_file)
            if os.path.exists(configFilePath):
                if not os.path.samefile(configFilePath, self.global_config_file_path):
                    Logger.debug(f"Inherited DSO configuration found: path={configFilePath}")
                    self.inherited_config_files.append(configFilePath)

        self.inherited_config = {}

        for configFile in reversed(self.inherited_config_files):
            try:
                config = yaml.load(open(configFile, 'r', encoding='utf-8'), yaml.SafeLoader)
            except:
                raise DSOException(MESSAGES['InvalidDSOConfigurationFile'])
            
            self.inherited_config = merge_dicts(config, self.inherited_config)

        self.update_merged_config()

    def override_config(self, config_overrides):

        self.overriden_config = {}

        if config_overrides:
            try:
                configs = config_overrides.split(',')
                for config in configs:
                    key = config.split('=')[0].strip()
                    value = config.split('=')[1].strip()
                    old = get_dict_item(self.merged_config, key.split('.'))
                    if not old:
                        Logger.warn(f"DSO configuration '{key}' was not found in the merged configuration.")
                    else:
                        Logger.warn(f"DSO configuration '{key}' was overriden from '{old}' to '{value or 'default'}'.")
                    set_dict_value(self.overriden_config, key.split('.'), value)
            except:
                raise DSOException(MESSAGES['InvalidConfigOverrides'])

        self.update_merged_config()


    def load(self, working_dir, config_overrides):
        self.working_dir = working_dir
        self.load_local_config()
        self.load_global_config()
        self.load_inherited_config()
        self.override_config(config_overrides)
        self.check_version()

    def check_version(self):
        if not int(self.merged_config['version']) == default_config['version']:
            if int(self.merged_config['version']) > default_config['version']:
                Logger.warn(MESSAGES['DSOConfigNewer'].format(default_config['version'], self.merged_config['version']))
            else:
                Logger.warn(MESSAGES['DSOConfigOlder'].format(default_config['version'], self.merged_config['version']))


    def get_provider_default_spec(self, provider_id):
        if provider_id in sys.modules:
            provider = sys.modules[provider_id]
            # provider = __import__(provider_id)
            # provider = imp.find_module(provider_id)
            # Logger.debug(f"Provider '{provider_id}' has already been loaded.")
        else:
            Logger.debug(f"Provider '{provider_id}' has not been loaded. Loading...")
            providerPackagePath = os.path.join(self.install_path, 'provider', provider_id)
            if not os.path.exists(providerPackagePath):
                raise DSOException(f"No provider found '{provider_id}'.")
            provider = imp.load_package(provider_id, providerPackagePath)
        
        return getattr(provider, 'default_spec', {})


    def update_merged_config(self):
        self.merged_config = default_config.copy()
        self.merged_config = merge_dicts(self.global_config, self.merged_config)
        self.merged_config = merge_dicts(self.inherited_config, self.merged_config)
        self.merged_config = merge_dicts(self.local_config, self.merged_config)
        self.merged_config = merge_dicts(self.overriden_config, self.merged_config)
        ### add missing default specs for each provider
        providers = ['parameter', 'secret', 'template']
        for provider in providers:
            providerId = self.merged_config[provider]['provider']['id']
            if providerId:
                save = self.merged_config[provider]['provider']['spec'].copy()
                self.merged_config[provider]['provider']['spec'] = self.get_provider_default_spec(f"{provider}/{providerId}")
                merge_dicts(save, self.merged_config[provider]['provider']['spec'])

    def flush_local_config(self):
        os.makedirs(self.local_config_dir_path, exist_ok=True)
        with open(self.local_config_file_path, 'w') as outfile:
            yaml.dump(self.local_config, outfile, sort_keys=False, indent=2)

    def flush_global_config(self):
        os.makedirs(self.global_config_dir_path, exist_ok=True)
        with open(self.global_config_file_path, 'w') as outfile:
            yaml.dump(self.global_config, outfile, sort_keys=False, indent=2)

    @property
    def application(self):
        if 'application' in self.merged_config:
            result = self.merged_config['application'] or 'default'
        else:
            result  = os.getenv('DSO_APPLICATION') or 'default'
        if self.project == 'default':
            if not result == 'default':
                Logger.warn(f"The specific context of application '{result}' was ignored because the global context was used.")
                result = 'default'
        return result.lower()

    @property
    def project(self):
        if 'project' in self.merged_config:
            result = self.merged_config['project'] or 'default'
        else:
            result  = os.getenv('DSO_PROJECT') or 'default'
        return result.lower()

    @property
    def parameter_provider(self):
        try:
            result = self.merged_config['parameter']['provider']['id']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Parameter'))
        return result

    @property
    def secret_provider(self):
        try:
            result = self.merged_config['secret']['provider']['id']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Secret'))
        return result

    @property
    def template_provider(self):
        try:
            result = self.merged_config['template']['provider']['id']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Template'))
        return result

    def parameter_spec(self, key=None):
        try:
            result = self.merged_config['parameter']['provider']['spec']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Parameter'))
        if not key:
            return result
        elif key in result:
            return result[key]
        else:
            return None

    def secret_spec(self, key=None):
        try:
            result = self.merged_config['secret']['provider']['spec']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Secret'))
        if not key:
            return result
        elif key in result:
            return result[key]
        else:
            return None

    def template_spec(self, key):
        try:
            result = self.merged_config['template']['provider']['spec']
        except KeyError:
            raise DSOException(MESSAGES['ProviderNotSet'].format('Template'))
        if not key:
            return result
        elif key in result:
            return result[key]
        else:
            return None

    def get_template_render_path(self, key=None):
        result = get_dict_item(self.local_config, ['template', 'render']) or {}
        if not key:
            return result
        else:
            return {x:result[x] for x in result if x==key}

    def register_template_custom_render_path(self, key, render_path):
        result = get_dict_item(self.local_config, ['template', 'render']) or {}
        # if os.path.isabs(render_path):
        #     raise DSOException(MESSAGES['AbsTemplateRenderPath'].format(render_path))
        if os.path.isdir(render_path):
            raise DSOException(MESSAGES['InvalidRenderPathExistingDir'].format(render_path))
        result[key] = render_path
        self.local_config['template']['render'] = result
        self.flush_local_config()

    def unregister_template_custom_render_path(self, key):
        result = get_dict_item(self.local_config, ['template', 'render'])
        if key in result:
            self.local_config['template']['render'].pop(key)
            self.flush_local_config()

    def get(self, key=None, scope=''):
        if key:
            Logger.info("Getting '{0}' from DSO configurations...".format(key))
        else:
            Logger.info("Getting DSO configurations...")

        if scope == 'local':
            usedConfig = merge_dicts(self.overriden_config, self.local_config.copy())
        elif scope == 'global':
            usedConfig = merge_dicts(self.overriden_config, self.global_config.copy())
        else:
            usedConfig = self.merged_config.copy()

        if key:
            result = get_dict_item(usedConfig, key.split('.'))
            if not result:
                raise DSOException(f"'{key}' has not been set in the DSO configurations.")
            return result
        else:
            return usedConfig

    def set(self, key, value, use_global):
        if use_global:
            Logger.info(f"Setting '{key}' to '{value}' in the global DSO configurations...")
            if not os.path.exists(self.local_config_file_path):
                raise DSOException("The global configuration has not been intitialized. Run 'dso config init --global' to initialize it.")

            set_dict_value(self.global_config, key.split('.'), value, overwrite_parent=True, overwrite_children=True)
            self.update_merged_config()
            self.flush_global_config()
        else:
            Logger.info(f"Setting '{key}' to '{value}' in the local DSO configurations...")
            if not os.path.exists(self.local_config_file_path):
                raise DSOException("The working directory has not been intitialized. Run 'dso config init' to initialize it.")

            set_dict_value(self.local_config, key.split('.'), value, overwrite_parent=True, overwrite_children=True)
            self.update_merged_config()
            self.flush_local_config()

    def delete(self, key, use_global):
        if use_global:
            Logger.info(f"Deleting '{key}' from the global DSO configurations...")
            parent = get_dict_item(self.global_config, key.split('.')[:-1])
            if parent and key.split('.')[-1] in parent:
                parent.pop(key.split('.')[-1])
                self.flush_global_config()
                self.update_merged_config()
            else:
                raise DSOException(f"'{key}' not found in the local DSO configuratoins.")

        else:
            Logger.info(f"Deleting '{key}' from the local DSO configurations...")
            parent = get_dict_item(self.local_config, key.split('.')[:-1])
            if parent and key.split('.')[-1] in parent:
                parent.pop(key.split('.')[-1])
                self.flush_local_config()
                self.update_merged_config()
            else:
                raise DSOException(f"'{key}' not found in the local DSO configuratoins.")

    def init(self, working_dir, init_config, config_overrides, use_local):
        Logger.info("Initializing DSO configurations...")
        self.working_dir = working_dir

        self.local_config_dir_path = os.path.join(self.working_dir, self.config_dir)
        self.local_config_file_path = os.path.join(self.local_config_dir_path, self.config_file)

        if os.path.exists(self.local_config_file_path):
            Logger.warn("The working directory has already been initialized.")

        config = {}
        
        ### use init_config instead of local/inherited config
        if init_config:
            config = merge_dicts(init_config, config)
            ### merge with existing local configuration?
            if use_local:
                Logger.debug("Merging local configuration...")
                self.load_local_config(False)
                config = merge_dicts(self.local_config, config)
        else:
            ### do not show warning if directory is not initialized yet
            self.load_local_config(False)
            config = merge_dicts(self.local_config, config)
            ### override locally inherited configuration?
            if use_local: 
                Logger.debug("Merging global configuration...")
                self.load_global_config()
                config = merge_dicts(self.global_config, config)

                Logger.debug("Merging inherited configuration...")
                self.load_inherited_config()
                config = merge_dicts(self.inherited_config, config)

        ### if config overrides, merge them to local
        if config_overrides:
            Logger.debug("Merging configuration overrides...")
            self.override_config(config_overrides)
            config = merge_dicts(self.overriden_config, config)

        self.local_config = config
        self.update_merged_config()

        self.flush_local_config()



Config = ConfigManager()

