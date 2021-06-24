from ..input_outputs import WSGI as WSGIInputOutput
from ..di import StandardDependencies
from .build_context import build_context


class WSGI:
    _di = None
    _handler = None

    def __init__(self, di):
        self._di = di

    def configure(self, application):
        self._handler = self._di.build(application.handler_class, cache=False)
        self._handler.configure(application.handler_config)

    def __call__(self, env, start_response):
        if self._handler is None:
            raise ValueError("Cannot execute WSGI context without first configuring it")

        return self._handler(WSGIInputOutput(env, start_response))

def wsgi(
    application,
    di_class=StandardDependencies,
    bindings=None,
    binding_classes=None,
    binding_modules=None
):
    return build_context(
        WSGI,
        application,
        di_class,
        bindings=bindings,
        binding_classes=binding_classes,
        binding_modules=binding_modules
    )
