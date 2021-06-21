from ..adb import ADB


class Project:

    def __init__(self, deviceSN):
        self.adbIns = ADB(deviceSN)

    def tapFreeButton(self, x, y):
        self.adbIns.tap(x, y)

    def openApp(self, Activity):
        self.adbIns.start(Activity)

    def freeMemory(self):
        self.adbIns.pressHomeKey()
        self.adbIns.pressHomeKey()
        self.adbIns.pressMenuKey()
        self.tapFreeButton()

    def mainloop(self):
        pass
