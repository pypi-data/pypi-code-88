import pkgutil
import logging
import importlib


# Module logger
mogger = logging.getLogger("pza.plugins")


class Plugins:

    PREFIX="panduza_plg_"

    objects = { }

    ###########################################################################
    ###########################################################################

    def GetNames():
        return Plugins.objects.keys()

    ###########################################################################
    ###########################################################################

    def GetStatus():
        """
        To get the status of all the plugins
        """
        status = {}
        for name in Plugins.objects:
            mogger.debug("Request status of plugin %s", name)
            status[name] = Plugins.objects[name].GetStatus()
        return status

    ###########################################################################
    ###########################################################################

    def GetAdapters():
        """
        """
        adapters = {}
        for name in Plugins.objects:
            adapters.update(Plugins.objects[name].GetAdapters())

        return adapters

    ###########################################################################
    ###########################################################################

    def GetInterfaces():
        """
        """
        interfaces = {}
        for name in Plugins.objects:
            interfaces.update(Plugins.objects[name].GetAdapters())

        return interfaces

    ###########################################################################
    ###########################################################################

    def FindPluginFromAdapter(adapter_name):
        for name in Plugins.objects:
            if Plugins.objects[name].HasAdapter(adapter_name):
                return Plugins.objects[name]

        raise Exception("Cannot find the plugin from adapter (" + adapter_name + ")")

    ###########################################################################
    ###########################################################################

    def Init():
        """
        """

        #
        mogger.debug("Start plugin discovery")
        discovered_plugins = {
            name: importlib.import_module(name)
            for finder, name, ispkg
            in pkgutil.iter_modules()
            if name.startswith(Plugins.PREFIX)
        }
        mogger.debug("Discovered plugins: %s", str(discovered_plugins))

        #
        for plugin_name in discovered_plugins :

            mogger.info("Load plugin %s", plugin_name)

            plugin_package = __import__(plugin_name)
            plugin_obj = plugin_package.Plugin()

            plugin_obj.Init()
            Plugins.objects[plugin_obj.Name] = plugin_obj



