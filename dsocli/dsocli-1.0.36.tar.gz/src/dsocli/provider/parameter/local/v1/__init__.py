__package__ = 'dsocli.provider.parameter.local.v1'
from .main import LocalParameterProvider
from dsocli.providers import ProviderManager
ProviderManager.register(LocalParameterProvider())
