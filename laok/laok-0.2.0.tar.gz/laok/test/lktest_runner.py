#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020/6/4 17:25:47

@author: LiuKuan
@copyright: Apache License, Version 2.0
'''
import inspect, sys, time, traceback, math, re, codecs
#===============================================================================
# 交互式运行 _lktest
#===============================================================================
FUNC_NAME = "_lktest"

__all__ = ['lktest_run']

def _time_run(kvfunc, catch_except=True):
    try:
        name = kvfunc[0]
        func = kvfunc[1]
        print( '%s==begin' % name)
        t0 = time.time()
        func()
    except SystemExit:
        exit(0)
    except Exception as e:
        if catch_except:
            print ( '\nexception in call function---->\n%s' % traceback.format_exc() )
        else:
            raise
    finally:
        elapse = time.time() - t0
        print ( '%s==end(time:%fs)\n' % (name, elapse) )

#从文件提取 _lktest名字,主要是用于排序
RE_PAT = re.compile(r"^def\s*(.*{})\(\):.*".format(FUNC_NAME))
def _find_file_lktests(filename):
    with codecs.open(filename, encoding='utf8') as f:
        for i,line in enumerate(f):
            res = RE_PAT.search(line)
            if res:
                yield i,res.group(1)

def lktest_run(run_opt='run_last', catch_except=True):
    '''
    :param run_opt: run_last/run_first/run_select/run_select_once/run_all/[name_lktest]
    :param catch_except:
    :return:
    '''

    # 获取所有 _lktest
    mainMod = sys.modules['__main__']
    kvList = [ (k,v) for k,v in inspect.getmembers(mainMod, inspect.isfunction)
               if k.endswith(FUNC_NAME) ]

    # 检测是否有测试用例
    if not kvList:
        print('there is no [name]{} here'.format(FUNC_NAME))
        return

    # 按照代码文本顺序排序
    kvOrder = {}
    for order, name in  _find_file_lktests(mainMod.__file__):
        kvOrder[name] = order
    kvList.sort(key = lambda pair: kvOrder[pair[0]])

    if run_opt == 'run_first':
        return _time_run(kvList[0], catch_except)
    elif run_opt == 'run_last':
        return _time_run(kvList[-1], catch_except)
    elif run_opt == 'run_all':
        for kv in kvList:
            _time_run(kv, catch_except)
    elif run_opt in ['run_select','run_select_once', '']:
        listLen = len(kvList)
        while True:
            w = math.ceil(math.log10(listLen))
            fmt = "<%0{}d>==%s".format(w)
            for i, kv in enumerate(kvList):
                print(fmt % (i, kv[0]))

            i = input('which test do you want to run , -1=quit , -2=run-all:')
            try:
                i = int(i)
            except:
                i = listLen - 1
            if i == -2:
                for kv in kvList:
                    _time_run(kv, catch_except)
                return
            elif i == -1:
                return
            else:
                i = (i + listLen) % listLen
                _time_run( kvList[i], catch_except)

            if run_opt == 'run_select_once':
                return
    else :
        for kv in kvList:
            if (isinstance(run_opt, str) and kv[0] == run_opt ) \
                    or (inspect.isfunction(run_opt) and kv[1] == run_opt):
                _time_run(kv, catch_except)
                break

