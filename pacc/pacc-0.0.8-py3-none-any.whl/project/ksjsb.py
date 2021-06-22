from random import randint
from .project import Project



class KSJSB(Project):

    def __init__(self, deviceSN):
        super(KSJSB, self).__init__(deviceSN)

    def tapFreeButton(self):
        super(KSJSB, self).tapFreeButton(540, 1706)

    def randomSwipe(self):
        r = randint(6, 30)
        x1 = randint(200, 700)
        y1 = randint(1363, 1477)
        x2 = randint(200, 700)
        y2 = randint(552, 709)
        self.adbIns.swipe(x1, y1, x2, y2)

    def openApp(self):
        super(KSJSB, self).openApp('com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity')

    def mainloop(self):
        self.freeMemory()
        self.openApp()


