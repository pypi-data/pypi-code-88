# this is the API of GDAPS itself.
import logging
import typing

from django.apps import AppConfig

from gdaps.exceptions import PluginError


class PluginMeta:
    """Inner class of GDAPS plugins.

    All GDAPS plugin AppConfig classes need to have an inner class named ``PluginMeta``. This
    PluginMeta provides some basic attributes and  methods that are needed when interacting with a
    plugin during its life cycle.

    .. code-block:: python

        from django.utils.translation import gettext_lazy as _
        from django.apps import AppConfig

        class FooPluginConfig(AppConfig):

            class PluginMeta:
                # the plugin machine "name" is taken from the Appconfig, so no name here
                verbose_name = _('Foo Plugin')
                author = 'Me Personally'
                description = _('A foo plugin')
                visible = True
                version = '1.0.0'
                compatibility = "myproject.core>=2.3.0"

    .. note::
        If ``PluginMeta`` is missing, the plugin is not recognized by GDAPS.
    """

    #: The version of the plugin, following `Semantic Versioning <https://semver.org/>`_. This is
    #: used for dependency checking as well, see ``compatibility``.
    version = "1.0.0"

    #: The verbose name, as shown to the user
    verbose_name = "My special plugin"

    #: The author of the plugin. Not translatable.
    author = "Me, myself and Irene"

    #: The email address of the author
    author_email = "me@example.com"

    #: A longer text to describe the plugin.
    description = ""

    #: A free-text category where your plugin belongs to.
    #: This can be used in your application to group plugins.
    category = "GDAPS"

    #: A boolean value whether the plugin should be visible, or hidden.
    #:
    #:     .. deprecated:: 0.4.2
    #:         Use `hidden` instead.
    visible = True

    #:A boolean value whether the plugin should be hidden, or visible. False by default.
    hidden = False

    #: A string containing one or more other plugins that this plugin is known being compatible with, e.g.
    #: "myproject.core>=1.0.0<2.0.0" - meaning: This plugin is compatible with ``myplugin.core`` from version
    #: 1.0.0 to 1.x - v2.0 and above is incompatible.
    #:
    #:         .. note:: Work In Progress.
    compatibility = "gdaps>=1.0.0"

    def install(self):
        """
        Callback to setup the plugin for the first time.

        This method is optional. If your plugin needs to install some data into the database at the first run,
        you can provide this method to ``PluginMeta``. It will be called when ``manage.py syncplugins`` is called and
        the plugin is run, but only for the first time.

        An example would be installing some fixtures, or providing a message to the user.
        """

    def initialize(self):
        """
        Callback to initialize the plugin.

        This method is optional. It is called and run at Django start once.
        If your plugin needs to make some initial checks, do them here, but make them quick, as they slow down
        Django's start.
        """


class PluginConfig(AppConfig):
    """Convenience class for GDAPS plugins to inherit from.

    While it is not strictly necessary to inherit from this class - duck typing is ok -
    it simplifies the type suggestions and autocompletion of IDEs like PyCharm, as PluginMeta is already declared here.
    """

    PluginMeta: PluginMeta = None


logger = logging.getLogger(__name__)


class InterfaceMeta(type):
    """Metaclass of Interfaces and Implementations

    This class follows Marty Alchin's principle of MountPoints.
    Thanks for his GREAT piece of software:
    http://martyalchin.com/2008/jan/10/simple-plugin-framework/
    """

    def __init__(cls, name, bases, dct) -> None:

        if not hasattr(cls, "_implementations"):
            # This branch only executes when processing the interface itself.
            # So, since this is a new plugin type, not an implementation, this
            # class shouldn't be registered as a plugin. Instead, it sets up a
            # list where plugins can be registered later.
            cls._implementations = []
            cls.__interface__ = True
            if not cls.__name__.startswith("I"):
                logger.warning(
                    f"WARNING: <{cls.__name__}>: Interface names should start with a capital 'I'."
                )
        else:
            cls.__interface__ = False
            # This must be a plugin implementation, which should be registered.
            # Simply appending it to the list is all that's needed to keep
            # track of it later.
            service = getattr(cls, "__service__", True)
            if service:
                plugin = cls()
            else:
                plugin = cls

            for base in bases:
                if hasattr(base, "_implementations"):
                    base._implementations.append(plugin)
                # else:
                #     raise PluginError(
                #         "A Plugin can't implement service AND non-service "
                #         "interfaces at the same time. "
                #     )

    def __iter__(mcs) -> typing.Iterable:
        """Returns an object with all enabled plugins, where you can iterate over."""
        return iter(
            # return only enabled plugins
            impl
            for impl in mcs._implementations
            if getattr(impl, "enabled", True)
        )

    def all_plugins(cls) -> typing.Iterable:
        """Returns all plugins, even if they are not enabled."""
        logger.warning(
            f"<Interface>.plugins() is deprecated. You cna iteate directly over {mcs.__name}."
        )
        return cls._implementations

    def plugins(mcs) -> typing.Iterable:
        """Returns all plugins, even if they are not enabled."""
        logger.warning(
            f"<Interface>.plugins() is deprecated and will be removed. Please iterate directly over the {mcs.__name__} class."
        )
        return mcs.__iter__()

    def __len__(self) -> int:
        """Return the number of plugins that implement this interface."""
        return len(
            [impl for impl in self._implementations if getattr(impl, "enabled", True)]
        )

    def __contains__(self, cls: type) -> bool:
        """Returns True if there is a plugin implementing this interface."""
        # TODO: test
        if getattr(self, "__service__", True):
            return cls in [type(impl) for impl in self._implementations]
        else:
            return cls in self._implementations

    def __repr__(self) -> str:
        """Returns a textual representation of the interface/implementation."""
        interface = True
        for base in self.__bases__:
            if type(base) == InterfaceMeta:
                return (
                    f"<Implementation '{self.__name__}' of Interface '{base.__name__}'>"
                )

        return f"<Interface '{self.__name__}'>"


# noinspection PyPep8Naming
def Interface(cls):
    """Decorator for classes that are interfaces.

    Declare an interface using the ``@Interface`` decorator, optionally add add attributes/methods to that class:

        .. code-block:: python

            @Interface
            class IFooInterface:
                def do_something(self):
                    pass

        You can choose whatever name you want for your interfaces, but we recommend you start the name with a capital "I".
        Read more about interfaces in the :ref:`Interfaces` section."""
    if type(cls) != type:
        raise TypeError(f"@Interface must decorate a class, not {type(cls)}")
    interface_meta = InterfaceMeta(cls.__name__, cls.__bases__, dict(cls.__dict__))
    return interface_meta


def require_app(app_config: AppConfig, required_app_name: str) -> None:
    """Helper function for AppConfig.ready() - checks if an app is installed.

    An ``ImproperlyConfigured`` Exception is raised if the required app is not present.

    :param app_config: the AppConfig which requires another app. usually use ``self`` here
            when called from AppConfig.ready()
    :param required_app_name: the required app name.
    """
    from django.apps import apps
    from django.core.exceptions import ImproperlyConfigured

    if app_config.name not in [app.name for app in apps.get_app_configs()]:
        raise ImproperlyConfigured(
            "The '{}' module relies on {}. Please add '{}' to your INSTALLED_APPS.".format(
                app_config.name, app_config.verbose_name, required_app_name
            )
        )
