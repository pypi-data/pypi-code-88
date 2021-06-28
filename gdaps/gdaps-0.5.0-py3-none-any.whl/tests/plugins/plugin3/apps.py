from django.apps import AppConfig


class Plugin3Meta:
    verbose_name = "Plugin 3"
    version = "blah_foo"
    dependencies = ["plugin2"]


class Plugin3Config(AppConfig):

    name = "tests.plugins.plugin3"
    PluginMeta = Plugin3Meta
