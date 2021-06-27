import logging

from panduza.interfaces.io import direction

# Module logger
mogger = logging.getLogger("pza.plugin.devfs-gpio.sysgpio")



class SysGpio:


    def __init__(self, number) -> None:
        """
        """
        self.number = number

    ###########################################################################
    ###########################################################################

    def export(self):
        """
        """
        try:
            f = open("/sys/class/gpio/export", "w")
            f.write(str(self.number))
            f.close()
        except IOError as e:
            if e.errno == 16:
                mogger.warning("GPIO %s already exported", str(self.number))
            else:
                mogger.error("Error exporting GPIOs %s | %s", str(self.number), repr(e))
                raise Exception("Error exporting GPIOs %s | %s" % (str(self.number), repr(e)))

    ###########################################################################
    ###########################################################################

    def unexport(self):
        pass
        # int gpio::disable()
        # {
        #     string exportString;
        #     exportString+="echo \"";
        #     exportString+=static_cast<ostringstream*>( &(ostringstream() << gpionum) )->str();
        #     exportString+="\" > /sys/class/gpio/unexport";
        #     system(exportString.c_str());
        #     return 0;
        # }

    ###########################################################################
    ###########################################################################

    def set_value(self, val):
        try:
            path = "/sys/class/gpio/gpio%s/value" % self.number
            f = open(path, "w")
            f.write(str(val))
            f.close()
        except IOError as e:
            mogger.error("Unable to set value %s to GPIO %s (%s) | %s", str(val), self.number, path, repr(e))

    ###########################################################################
    ###########################################################################

    def get_value(self):
        """
        To get the value of the gpio
        """
        try:
            f = open("/sys/class/gpio/gpio%s/value" % self.number, "r")
            value = f.read(1)
            f.close()
            return int(value)
        except IOError as e:
            mogger.error("Unable to export get value %s", repr(e))

    ###########################################################################
    ###########################################################################

    def set_direction(self, direction):
        """
        """
        try:
            f = open("/sys/class/gpio/gpio%s/direction" % self.number, "w")
            f.write(direction)
            f.close()
        except IOError:
            mogger.error("Unable to export set value")

    ###########################################################################
    ###########################################################################

    def get_direction(self):
        """
        """
        try:
            f = open("/sys/class/gpio/gpio%s/direction" % self.number, "w")
            direction = f.read()
            f.close()
            return direction
        except IOError:
            mogger.error("Unable to export set value")




