from .project import Project
from ..tools import sleep


class IQ(Project):
    """
    """
    scriptName = 'com.kildare.nautor/com.stardust.autojs.execution.ScriptExecuteActivity'

    instances = []

    def __init__(self):
        super(IQ, self).__init__('201')

    def mainloop(self):
        while True:
            if self.adbIns.rebootPerHour():
                self.adbIns.tap(130, 235)
            sleep(1200)
