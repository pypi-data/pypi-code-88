from .project import Project
from ..tools import sleep


class DYFD(Project):
    """
    """
    scriptName = 'com.com.fb.jiuyi/com.ds.daisi.activity.ElfinPayActivity'
    programName = 'com.ss.android.ugc.aweme/com.ss.android.ugc.aweme.splash.SplashActivity'

    def __init__(self):
        super(DYFD, self).__init__('401')
        self.adbIns.reboot()
        self.adbIns.tap(912, 1755, 9)
        self.adbIns.tap(579, 1575, 3)
        self.adbIns.tap(1072, 581)
        self.adbIns.tap(441, 589)

    def mainloop(self):
        pass
