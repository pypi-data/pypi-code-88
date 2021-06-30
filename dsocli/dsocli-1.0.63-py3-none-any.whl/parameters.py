from .logger import Logger
from .config import Config
from .providers import StoreProvider, ProviderManager
from .stages import Stages

class ParameterProvider(StoreProvider):
    def list(self, stage, uninherited, format):
        raise NotImplementedError()
    def add(self, stage, key, value):
        raise NotImplementedError()
    def delete(self, stage, key):
        raise NotImplementedError()
    def get(self, stage, key):
        raise NotImplementedError()

class ParametersClass():

    def validate_key(self, key):
        provider = ProviderManager.ParameterProvider()
        Logger.info("Start validating parameter key...")
        return provider.validate_key(key)

    def list(self, stage, uninherited):
        project = Config.project
        application = Config.application
        provider = ProviderManager.ParameterProvider()
        if uninherited:
            Logger.info(f"Start listing uninherited SSM parameters: project={project}, application={application}, stage={Stages.shorten(stage)}")
        else:
            Logger.info(f"Start listing SSM parameters: project={project}, application={application}, stage={Stages.shorten(stage)}")
        return provider.list(project, application, stage, uninherited)

    def add(self, stage, key, value):
        self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.ParameterProvider()
        Logger.info(f"Start adding parameter: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}, value={value}")
        return provider.add(project, application, stage, key, value)

    def get(self, stage, key, revision):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.ParameterProvider()
        Logger.info(f"Start getting parameter value: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.get(project, application, stage, key, revision)

    def history(self, stage, key):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.ParameterProvider()
        Logger.info(f"Start getting parameter history: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.history(project, application, stage, key)

    def delete(self, stage, key):
        # self.validate_key(key)
        project = Config.project
        application = Config.application
        provider = ProviderManager.ParameterProvider()
        Logger.info(f"Start deleting parameter: project={project}, application={application}, stage={Stages.shorten(stage)}, key={key}")
        return provider.delete(project, application, stage, key)

Parameters = ParametersClass()