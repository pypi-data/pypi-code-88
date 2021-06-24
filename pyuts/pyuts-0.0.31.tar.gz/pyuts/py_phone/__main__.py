# -*- coding: UTF-8 -*-
import sys
from ..py_file.fileU import FileU
from ..py_recg.imgU import ImgU
from ..py_phone.phoneAutoU import PhoneAutoU


def printHelp():
    print("python3 -m pyuts.py_phone [projectName] [funName] args... ")
    print("  funName:addAction|addOption|doAction|doOption")

if __name__ == '__main__':
    """ python3 -m pyuts.py_phone.phoneAutoU.py [projectName] [funName] args... """
    projectName = sys.argv[1]
    pau = PhoneAutoU().init(projectName)
    funName = "help"
    if len(sys.argv) > 2:
        funName = sys.argv[2]
    if funName == "addAction":
        actionName = sys.argv[3]
        pau.addAction(actionName)
    elif funName == "addOption":
        # 动作名称
        actionName = sys.argv[3]
        # 操作名称
        optionName = sys.argv[4]
        # 参数
        args = None
        if len(sys.argv) > 5:
            args = sys.argv[5]
        # 是否清掉重新添加
        isReAdd = False
        if len(sys.argv) > 6:
            isReAdd = (sys.argv[6] in ["True","true"])
        pau.addOption(actionName,optionName,args,isReAdd)
    elif funName == "doAction":
        # 执行doAction
        # 动作名称
        actionName = sys.argv[3]
        pau.doAction(actionName)
    elif funName == "doOption":
        # 执行doOption
        optionName = sys.argv[3]
        # 图片路径
        if len(sys.argv) <= 4:
            print("please add imgPath or None")
            exit()
        imgPath = sys.argv[4]
        # 参数
        args = None
        if len(sys.argv) > 5:
            args = sys.argv[5]
        imgU = None if imgPath in [None,"None"] else ImgU.produce().initImg(imgPath)
        res = pau.doOption(imgU,optionName,args)
        if not isinstance(res, ImgU):
            print(res)
        else:
            res.show()
    else:
        printHelp()
        
        
    