from .project import Project
from ..tools import sleep


class SD(Project):
    """
    """
    scriptName = 'com.dd.rclient/com.dd.rclient.ui.activity.MainActivity'

    def __init__(self, SN):
        super(SD, self).__init__(SN)

    def mainloop(self):
        instructions = [
            (913, 1768, 9, '启动滴滴助手'),
            (242, 1430, 2, '退出程序'),
            (685, 1070, 3, '确定'),
            (913, 1768, 9, '启动滴滴助手'),
            (565, 588, 2, '开始挂机'),
        ]
        while True:
            if self.adbIns.rebootPerDay([3]):
                self.adbIns.pressHomeKey()
                self.adbIns.taps(instructions)
            sleep(1200)
