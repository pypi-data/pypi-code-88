from random import randint
from .project import Project
from ..tools import sleep, EMail
from datetime import datetime


class KSJSB(Project):

    programName = 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity'
    verificationCode = 'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity'
    liveStreaming = 'com.kuaishou.nebula/com.yxcorp.gifshow.detail.PhotoDetailActivity'
    userProfileActivity = 'com.kuaishou.nebula/com.yxcorp.gifshow.profile.activity.UserProfileActivity'
    instances = []
    startTime = datetime.now()

    def __init__(self, deviceSN):
        super(KSJSB, self).__init__(deviceSN)
        self.sleepTime = 0

    def tapFreeButton(self):
        super(KSJSB, self).tapFreeButton(540, 1706)

    def randomSwipe(self):
        if self.sleepTime > 0:
            return
        x1 = randint(500, 560)
        y1 = randint(1500, 1590)
        x2 = randint(500, 560)
        y2 = randint(360, 560)
        self.adbIns.swipe(x1, y1, x2, y2)
        self.sleepTime += randint(6, 30)

    def openApp(self):
        super(KSJSB, self).openApp('com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity')

    def start(self):
        self.adbIns.reboot()
        self.freeMemory()
        self.openApp()

    @classmethod
    def mainloop(cls):
        cls.instances.append(cls('302'))
        cls.instances.append(cls('303'))
        for i in cls.instances:
            i.start()
        while True:
            st = randint(3, 9)
            for i in cls.instances:
                i.randomSwipe()
                i.sleepTime -= st
            print('已运行：', datetime.now() - cls.startTime, sep='')
            for i in cls.instances:
                if (i.liveStreaming or i.userProfileActivity)\
                        in i.adbIns.getCurrentFocus():
                    i.start()
                elif i.verificationCode in i.adbIns.getCurrentFocus():
                    EMail(i.adbIns.device.SN).sendVerificationCodeAlarm()
            sleep(st)
