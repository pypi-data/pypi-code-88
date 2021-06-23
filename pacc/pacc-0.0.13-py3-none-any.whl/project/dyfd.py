from .project import Project
from ..tools import sleep


class DYFD(Project):
    """
    """
    scriptName = 'com.com.fb.jiuyi/com.ds.daisi.activity.ElfinPayActivity'
    programName = 'com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.splash.SplashActivity'

    def __init__(self):
        super(DYFD, self).__init__('401')

    def mainloop(self):
        while True:
            if self.adbIns.rebootPerHour():
                self.adbIns.tap(912, 1755, 9)  # 打开抖音福袋
                self.adbIns.tap(579, 1575, 3)  # 启动悬浮窗
                self.adbIns.tap(1072, 581, 3)  # 展开悬浮窗
                self.adbIns.tap(441, 589)  # 启动
            sleep(1200)

