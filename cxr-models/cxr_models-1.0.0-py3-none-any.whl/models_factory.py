import functools
import keras_applications as ka

from .models import covxnet


class ModelsFactory:
    _models = {

        # CovXNet
        'covxnet': [covxnet.CovXNet],

    }

    @property
    def models(self):
        return self._models

    def models_names(self):
        return list(self.models.keys())

    @staticmethod
    def get_kwargs():
        return {}

    def inject_submodules(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            modules_kwargs = self.get_kwargs()
            new_kwargs = dict(list(kwargs.items()) + list(modules_kwargs.items()))
            return func(*args, **new_kwargs)

        return wrapper

    def get(self, name):
        if name not in self.models_names():
            raise ValueError('No such model `{}`, available models: {}'.format(
                name, list(self.models_names())))

        model_fn = self.models[name]
        model_fn = self.inject_submodules(model_fn)
        return model_fn