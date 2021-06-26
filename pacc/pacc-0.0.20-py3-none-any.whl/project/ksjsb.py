from random import randint
from .project import Project
from ..tools import sleep, EMail
from datetime import datetime


class KSJSB(Project):

    programName = 'com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity'
    verificationCode = 'com.kuaishou.nebula/com.yxcorp.gifshow.webview.KwaiYodaWebViewActivity'
    liveStreaming = 'com.kuaishou.nebula/com.yxcorp.gifshow.detail.PhotoDetailActivity'
    userProfileActivity = 'com.kuaishou.nebula/com.yxcorp.gifshow.profile.activity.UserProfileActivity'

    def __init__(self, deviceSN):
        self.startTime = datetime.now()
        super(KSJSB, self).__init__(deviceSN)

    def tapFreeButton(self):
        super(KSJSB, self).tapFreeButton(540, 1706)

    def randomSwipe(self):
        r = randint(6, 30)
        x1 = randint(500, 560)
        y1 = randint(1500, 1590)
        x2 = randint(500, 560)
        y2 = randint(360, 560)
        self.adbIns.swipe(x1, y1, x2, y2)
        sleep(r)

    def openApp(self):
        super(KSJSB, self).openApp('com.kuaishou.nebula/com.yxcorp.gifshow.HomeActivity')

    def mainloop(self):
        self.adbIns.reboot()
        self.freeMemory()
        self.openApp()
        while True:
            self.randomSwipe()
            print('已运行：', datetime.now() - self.startTime, sep='')
            if (self.liveStreaming or self.userProfileActivity)\
                    in self.adbIns.getCurrentFocus():
                self.adbIns.reboot()
                self.freeMemory()
                self.openApp()
            elif self.verificationCode in self.adbIns.getCurrentFocus():
                EMail(self.adbIns.device.SN).sendVerificationCodeAlarm()
