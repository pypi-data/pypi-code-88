#!/usr/bin/env Python
# coding=utf-8
#作者： tony
'''本类用来动态创建类的实例'''
class InstanceActivator:
    '''动态创建类的实例。
    [Parameter]
    class_name - 类的全名（包括模块名）
    *args - 类构造器所需要的参数(list)
    *kwargs - 类构造器所需要的参数(dict)
    [Return]
    动态创建的类的实例
    [Example]
    class_name = 'knightmade.logging.Logger'
    logger = Activator.createInstance(class_name, 'logname')
    '''
    @staticmethod
    def createInstance(class_name, *args, **kwargs):
        (module_name, class_name) = class_name.rsplit('.', 1)
        module_meta = __import__(module_name, globals(), locals(), [class_name])
        class_meta = getattr(module_meta, class_name)
        object = class_meta(*args, **kwargs)
        return object