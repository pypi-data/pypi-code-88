import json

from awesomeTaskPy.log.loger import loger
import sys
contextObj=None
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]
class context():
    __taskInfo = None
    __log = None

    def __init__(self, taskInfo):
        self.__taskInfo = taskInfo
        self.__log = loger.instance(self.__taskInfo['taskId'])

    def getTaskInfo(self):
        return self.__taskInfo

    def getLoger(self):
        return self.__log
def getContext():
    global contextObj
    if contextObj!=None:
        return contextObj
    return context({"taskId":"test"})
def initContext():
    global contextObj
    if contextObj!=None:
        return contextObj
    params=1
    if len(sys.argv)>=2:
        taskId=sys.argv[1]
        global TASKINFOREPLACE
        inputPath = sys.path[0] + "/input" + "/" + taskId + "/input.log"
        data=open(inputPath,encoding='utf -8').read()
        params=json.loads(data)
    taskInfo=json.loads(params)
    contextObj=context(taskInfo)
