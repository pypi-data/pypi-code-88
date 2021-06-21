from .project import Project
from ..tools import sleep


class HZDYX(Project):
    """
    """
    scriptName = 'anze.nb.hzdyx/com.stardust.autojs.inrt.SplashActivity'
    programName = 'com.ruiqugames.chinesechar/com.ruiqugames.chinesechar.MainActivity'

    def __init__(self):
        super(HZDYX, self).__init__('201')
        self.adbIns.reboot()
        self.adbIns.start(self.scriptName)
        sleep(6)
        self.adbIns.tap(798, 2159)
        self.adbIns.tap(287, 1492)

        super(HZDYX, self).__init__('202')
        self.adbIns.reboot()
        self.adbIns.start(self.scriptName)
        sleep(3)
        self.adbIns.tap(161, 1084)

    def mainloop(self):
        while True:
            sleep(30*60)
            self.__init__()
