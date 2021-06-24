import os
import re
import imp
import importlib.util
import sys
from .config import Config
from .constants import *
from .logger import Logger
from .exceptions import DSOException

class ProviderBase():
    def __init__(self, id):
        self.__id = id
    @property
    def id(self):
        return self.__id

class StoreProvider(ProviderBase):

    def validate_key(self, key):
        Logger.debug(f"Validating: key={key}")
        pattern = self.get_key_validator()
        if not re.match(pattern, key):
            raise DSOException(MESSAGES['InvalidKey'].format(key, pattern))

    def get_key_validator(self, key):
        raise NotImplementedError()


class ProviderManagerClass():
    __providers = {}

    # def load_all_providers(self):
    #     __import__(Config.root_path + 'lib/dso/provider')
    #     # importdir.do(os.path.dirname(__file__)+'/secret_providers', globals())
    #     # importdir.do(os.path.dirname(__file__)+'/template_providers', globals())

    def load_provider(self, provider_id):
        Logger.debug(f"Loading provider '{provider_id}'...")
        providerPackagePath = os.path.join(Config.install_path, 'provider', provider_id)
        if not os.path.exists(providerPackagePath):
            raise DSOException(f"No provider found for '{provider_id}'.")
        imp.load_package(provider_id, providerPackagePath)

    def register(self, provider: ProviderBase):
        if not provider.id in self.__providers:
            self.__providers[provider.id] = provider
            Logger.debug(f"Provider registered: id ={provider.id}")

    def get_provider(self, provider_id):
        if not provider_id in self.__providers:
            self.load_provider(provider_id)

        ### make sure provider has registered, and return it
        if provider_id in self.__providers:
            return self.__providers[provider_id] 
        else:
            raise DSOException(f"No provider has registered for '{provider_id}'.")

    def ParameterProvider(self):
        if not Config.parameter_provider:
            raise DSOException('Parameter provider has not been set.')
        return self.get_provider('parameter/' + Config.parameter_provider)

    def TemplateProvider(self):
        if not Config.template_provider:
            raise DSOException('Template provider has not been set.')
        return self.get_provider('template/' + Config.template_provider)

    def SecretProvider(self):
        if not Config.secret_provider:
            raise DSOException('Secret provider has not been set.')
        return self.get_provider('secret/' + Config.secret_provider)

ProviderManager = ProviderManagerClass()
