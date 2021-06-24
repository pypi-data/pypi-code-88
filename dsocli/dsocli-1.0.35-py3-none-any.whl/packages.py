
from .config import Config
from .providers import ProviderManager

class Packages():
    @staticmethod
    def list(env):
        provider = ProviderManager.get_provider(config['application']['package']['provider'])
        provider.list(env)

    @staticmethod
    def create(env):
        provider = ProviderManager.get_provider(config['application']['package']['provider'])
        provider.add(env)

    @staticmethod
    def download(env):
        provider = ProviderManager.get_provider(config['application']['package']['provider'])
        provider.get(env, name)

    @staticmethod
    def delete(env):
        provider = ProviderManager.get_provider(config['application']['package']['provider'])
        provider.delete(env, name)
