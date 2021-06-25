from .logger import Logger
from .config import Config
from .providers import StoreProvider, ProviderManager
from .stages import Stages

class SecretProvider(StoreProvider):
    def list(self, stage, uninherited, format, decrypt):
        raise NotImplementedError()
    def add(self, stage, key, value):
        raise NotImplementedError()
    def delete(self, stage, key):
        raise NotImplementedError()
    def get(self, stage, key):
        raise NotImplementedError()

class SecretsClass():

    def validate_key(self, key):
        provider = ProviderManager.SecretProvider()
        Logger.info("Start validating secret key...")
        return provider.validate_key(key)

    def list(self, stage, uninherited, decrypt):
        project = Config.project
        application = Config.application
        provider = ProviderManager.SecretProvider()
        if uninherited:
            Logger.info(f"Start listing overridden SSM secrets: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            Logger.info(f"Start listing SSM secrets: project={project}, application={application}, stage={Stages.shorten(stage)}")
        return provider.list(project, application, stage, uninherited, decrypt)

    def add(self, stage, key, value):
        self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.SecretProvider()
        Logger.info(f"Start adding secrets: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.add(project, application, stage, key, value)

    def get(self, stage, key):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.SecretProvider()
        Logger.info(f"Start getting secret: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.get(project, application, stage, key)

    def delete(self, stage, key):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.SecretProvider()
        Logger.info(f"Start deleting secret: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.delete(project, application, stage, key)

Secrets = SecretsClass()
