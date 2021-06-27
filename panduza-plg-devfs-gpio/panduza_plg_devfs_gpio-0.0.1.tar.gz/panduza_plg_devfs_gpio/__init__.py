import glob
import json
import logging
from .sysgpio import SysGpio

# Module logger
mogger = logging.getLogger("pza.plugin.devfs-gpio")


class Plugin():
    
    #
    Name = "devfs-gpio"

    #
    Adapters = { "sys": {} }

    # Plugin status
    # - STANDBY (wait to be started)
    # - RUNNING (is running properly)
    # - WARNING (is running but all the features may not be ok)
    # - ERROR   (not running at all due to an error)
    Status = "STANDBY"

    # To provide a string to display when status is WARNING or ERROR
    ErrorString = ""

    ###########################################################################
    ###########################################################################

    @staticmethod
    def Init():
        """
        Function to initialize the plugin
        
        [INTERFACE PLUGIN] MANDATORY
        """

        # Check if the conf file exists
        conf_files = glob.glob("/etc/panduza/"+ Plugin.Name +"-*.json")
        if len(conf_files) < 1:
            Plugin.UpStatus("ERROR", "No conf file found in (/etc/panduza/"+ Plugin.Name +"-*.json)")
            return

        # Parse the first conf file found
        conf_filename = conf_files[0]
        mogger.info("Parse conf file (%s)", conf_filename)

        # Opening JSON file
        f = open(conf_filename)
        # Parse conf
        conf_data = json.load(f)
        # Closing file
        f.close()

        # 
        warning = False
        for gpio in conf_data["gpios"]:
            Plugin.Adapters["sys"][ gpio["name"] ] = {
                "type": "io",
                "number": gpio["number"],
                "help": gpio["help"],
            }
            sysgpio = SysGpio(gpio["number"])
            try:
                sysgpio.export()
            except Exception as e:
                if not warning:
                    Plugin.UpStatus("WARNING", repr(e))
                    warning = True
                else:
                    Plugin.PushBackErrorString(repr(e))
    
        if not warning:
            Plugin.UpStatus("RUNNING")

    ###########################################################################
    ###########################################################################

    @staticmethod
    def GetStatus():
        """
        Return the global status of the plugin
        
        [INTERFACE PLUGIN] MANDATORY
        """
        interface_count = 0
        for adpater in Plugin.Adapters:
            interface_count += len(Plugin.Adapters[adpater].keys())
        return {
            "status": Plugin.Status,
            "error_string": Plugin.ErrorString,
            "interface_count": interface_count
            }

    ###########################################################################
    ###########################################################################

    @staticmethod
    def GetInterfaces():
        """
        [INTERFACE PLUGIN] MANDATORY
        """
        return Plugin.Adapters

    @staticmethod
    def GetAdapters():
        """
        [INTERFACE PLUGIN] MANDATORY
        """
        return Plugin.Adapters

    ###########################################################################
    ###########################################################################

    @staticmethod
    def HasAdapter(adapter_name):
        if adapter_name in Plugin.Adapters:
            return True
        else:
            return False

    ###########################################################################
    ###########################################################################

    @staticmethod
    def IoDirectionRead(adapter, interface):
        """
        """
        gpio_number = Plugin.Adapters[adapter][interface]["number"]
        sysgpio = SysGpio( gpio_number )
        return sysgpio.get_direction()
        # raise Exception("Interface " + adapter + "/" + interface + " not managed")

    ###########################################################################
    ###########################################################################

    @staticmethod
    def IoDirectionWrite(adapter, interface, direction):
        """
        """
        gpio_number = Plugin.Adapters[adapter][interface]["number"]

        sysgpio = SysGpio( gpio_number )
        sysgpio.set_direction(direction)

        raise Exception("Interface " + adapter + "/" + interface + " not managed")


    ###########################################################################
    ###########################################################################

    @staticmethod
    def IoValueRead(adapter, interface):
        """
        """
        gpio_number = Plugin.Adapters[adapter][interface]["number"]
        sysgpio = SysGpio( gpio_number )
        value = sysgpio.get_value()
        return value

    ###########################################################################
    ###########################################################################

    @staticmethod
    def IoValueWrite(adapter, interface, value):
        gpio_number = Plugin.Adapters[adapter][interface]["number"]

        sysgpio = SysGpio( gpio_number )
        try:
            sysgpio.set_value(value)
        except Exception as e:
            return { "status": "ERROR" }

        return { "status": "SUCCESS" }

    ###########################################################################
    ###########################################################################

    @staticmethod
    def UpStatus(status, error_string = ""):
        """
        Helper function to change the plugin status value
        """
        Plugin.Status = status
        Plugin.ErrorString = error_string
        if   Plugin.Status == "WARNING":
            mogger.warning(error_string)
        elif Plugin.Status == "ERROR":
            mogger.error(error_string)

    ###########################################################################
    ###########################################################################

    @staticmethod
    def PushBackErrorString(error_string):
        """
        """
        Plugin.ErrorString = Plugin.ErrorString  + " ; " + str(error_string)
